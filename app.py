"""
ShopSmart Sales Dashboard
A Streamlit dashboard for visualizing e-commerce sales data.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="ShopSmart Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)


# =============================================================================
# Data Loading (Phase 2: Foundational)
# =============================================================================

@st.cache_data
def load_data() -> pd.DataFrame:
    """
    Load sales data from CSV file with caching for performance.

    Returns:
        pd.DataFrame: Sales transaction data with parsed dates

    Raises:
        FileNotFoundError: If the data file is not found
    """
    try:
        df = pd.read_csv("data/sales-data.csv")
        # Parse date column
        df["date"] = pd.to_datetime(df["date"])
        return df
    except FileNotFoundError:
        raise FileNotFoundError("Sales data file not found at data/sales-data.csv")


# =============================================================================
# KPI Calculations (Phase 3: User Story 1 - ECOM-1)
# =============================================================================

def calculate_total_sales(df: pd.DataFrame) -> float:
    """
    Calculate the total sales from all transactions.

    Args:
        df: DataFrame containing sales data with 'total_amount' column

    Returns:
        float: Sum of all total_amount values
    """
    return df["total_amount"].sum()


def calculate_total_orders(df: pd.DataFrame) -> int:
    """
    Calculate the total number of unique orders.

    Args:
        df: DataFrame containing sales data with 'order_id' column

    Returns:
        int: Count of unique order IDs
    """
    return df["order_id"].nunique()


# =============================================================================
# Data Aggregation (Phase 4: User Story 2 - ECOM-2)
# =============================================================================

def get_monthly_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate sales data by month for trend analysis.

    Args:
        df: DataFrame containing sales data with 'date' and 'total_amount' columns

    Returns:
        pd.DataFrame: Monthly aggregated sales with 'month' and 'sales' columns,
                      sorted chronologically
    """
    monthly = df.groupby(df["date"].dt.to_period("M"))["total_amount"].sum().reset_index()
    monthly.columns = ["month", "sales"]
    monthly["month"] = monthly["month"].dt.to_timestamp()
    return monthly.sort_values("month")


# =============================================================================
# Data Aggregation (Phase 5: User Story 3 - ECOM-3)
# =============================================================================

def get_sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate sales data by product category.

    Args:
        df: DataFrame containing sales data with 'category' and 'total_amount' columns

    Returns:
        pd.DataFrame: Category aggregated sales with 'category' and 'sales' columns,
                      sorted by sales descending
    """
    category_sales = df.groupby("category")["total_amount"].sum().reset_index()
    category_sales.columns = ["category", "sales"]
    return category_sales.sort_values("sales", ascending=False)


# =============================================================================
# Data Aggregation (Phase 6: User Story 4 - ECOM-4)
# =============================================================================

def get_sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate sales data by geographic region.

    Args:
        df: DataFrame containing sales data with 'region' and 'total_amount' columns

    Returns:
        pd.DataFrame: Region aggregated sales with 'region' and 'sales' columns,
                      sorted by sales descending
    """
    region_sales = df.groupby("region")["total_amount"].sum().reset_index()
    region_sales.columns = ["region", "sales"]
    return region_sales.sort_values("sales", ascending=False)


# =============================================================================
# Chart Creation (Phase 4: User Story 2 - ECOM-2)
# =============================================================================

def create_trend_chart(monthly_df: pd.DataFrame) -> px.line:
    """
    Create a line chart showing sales trend over time.

    Args:
        monthly_df: DataFrame with 'month' and 'sales' columns

    Returns:
        plotly.graph_objects.Figure: Interactive line chart
    """
    fig = px.line(
        monthly_df,
        x="month",
        y="sales",
        title="Sales Trend Over Time",
        labels={"month": "Month", "sales": "Sales ($)"},
        markers=True
    )
    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales ($)",
        hovermode="x unified"
    )
    fig.update_traces(
        hovertemplate="<b>%{x|%B %Y}</b><br>Sales: $%{y:,.2f}<extra></extra>"
    )
    return fig


# =============================================================================
# Chart Creation (Phase 5: User Story 3 - ECOM-3)
# =============================================================================

def create_category_chart(category_df: pd.DataFrame) -> px.bar:
    """
    Create a bar chart showing sales by product category.

    Args:
        category_df: DataFrame with 'category' and 'sales' columns

    Returns:
        plotly.graph_objects.Figure: Interactive bar chart
    """
    fig = px.bar(
        category_df,
        x="category",
        y="sales",
        title="Sales by Category",
        labels={"category": "Category", "sales": "Sales ($)"},
        color="sales",
        color_continuous_scale="Blues"
    )
    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Sales ($)",
        showlegend=False,
        coloraxis_showscale=False
    )
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>"
    )
    return fig


# =============================================================================
# Chart Creation (Phase 6: User Story 4 - ECOM-4)
# =============================================================================

def create_region_chart(region_df: pd.DataFrame) -> px.bar:
    """
    Create a bar chart showing sales by geographic region.

    Args:
        region_df: DataFrame with 'region' and 'sales' columns

    Returns:
        plotly.graph_objects.Figure: Interactive bar chart
    """
    fig = px.bar(
        region_df,
        x="region",
        y="sales",
        title="Sales by Region",
        labels={"region": "Region", "sales": "Sales ($)"},
        color="sales",
        color_continuous_scale="Greens"
    )
    fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Sales ($)",
        showlegend=False,
        coloraxis_showscale=False
    )
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>"
    )
    return fig


# =============================================================================
# Main Application
# =============================================================================

def main():
    """Main application entry point."""
    st.title("🛒 ShopSmart Sales Dashboard")

    # Load data with error handling
    try:
        df = load_data()
    except FileNotFoundError as e:
        st.error(f"⚠️ {e}")
        st.info("Please ensure the sales data file exists at data/sales-data.csv")
        return

    # ==========================================================================
    # KPI Section (ECOM-1: Display KPI Metrics)
    # ==========================================================================

    # Calculate KPIs
    total_sales = calculate_total_sales(df)
    total_orders = calculate_total_orders(df)

    # Display KPIs in two columns
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="💰 Total Sales",
            value=f"${total_sales:,.2f}"
        )

    with col2:
        st.metric(
            label="📦 Total Orders",
            value=f"{total_orders:,}"
        )

    # ==========================================================================
    # Trend Chart Section (ECOM-2: Sales Trend Over Time)
    # ==========================================================================

    st.divider()

    # Calculate monthly sales and create trend chart
    monthly_sales = get_monthly_sales(df)
    trend_chart = create_trend_chart(monthly_sales)
    st.plotly_chart(trend_chart, use_container_width=True)

    # ==========================================================================
    # Category and Region Charts Section (ECOM-3 & ECOM-4)
    # ==========================================================================

    st.divider()

    # Create two columns for side-by-side charts
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        # Category breakdown chart
        category_sales = get_sales_by_category(df)
        category_chart = create_category_chart(category_sales)
        st.plotly_chart(category_chart, use_container_width=True)

    with chart_col2:
        # Region breakdown chart
        region_sales = get_sales_by_region(df)
        region_chart = create_region_chart(region_sales)
        st.plotly_chart(region_chart, use_container_width=True)


if __name__ == "__main__":
    main()
