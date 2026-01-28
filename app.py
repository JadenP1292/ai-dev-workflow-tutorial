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


if __name__ == "__main__":
    main()
