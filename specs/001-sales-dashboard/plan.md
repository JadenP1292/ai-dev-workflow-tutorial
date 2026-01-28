# Implementation Plan: ShopSmart Sales Dashboard

**Branch**: `001-sales-dashboard` | **Date**: 2026-01-27 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-sales-dashboard/spec.md`

## Summary

Build an interactive sales analytics dashboard for ShopSmart that displays key business metrics (Total Sales, Total Orders) and visualizations (sales trend line chart, category bar chart, region bar chart). The dashboard loads transaction data from a CSV file and presents it in a professional, executive-ready format accessible via web browser.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: Streamlit (web framework), Pandas (data processing), Plotly (interactive charts)
**Storage**: CSV file (data/sales-data.csv) - read-only
**Testing**: Manual testing via Streamlit local server; verify calculations against source data
**Target Platform**: Web browsers (Chrome, Firefox, Safari, Edge) via Streamlit Community Cloud
**Project Type**: Single project (standalone Streamlit application)
**Performance Goals**: Dashboard loads within 5 seconds; charts render within 2 seconds
**Constraints**: No authentication; public URL access; ~1,000 transactions; 12 months of data
**Scale/Scope**: Single-page dashboard; 4 stakeholder roles; read-only data display

## Constitution Check

*GATE: Must pass before implementation. All principles verified.*

| Principle | Status | Verification |
|-----------|--------|--------------|
| I. Code Simplicity and Readability | ✅ PASS | Single-file app with clear function names; PEP 8 compliant |
| II. User-Friendly Interactive Visualizations | ✅ PASS | Plotly provides tooltips; clear titles/labels planned |
| III. Python Best Practices | ✅ PASS | Type hints where beneficial; vectorized Pandas ops; f-strings |
| IV. Virtual Environment Isolation | ✅ PASS | Using uv; requirements.txt for dependencies |

**Technology Stack Compliance**:
- Python 3.11+ ✅
- Streamlit ✅
- Plotly ✅
- Pandas ✅
- uv for package management ✅
- Streamlit Community Cloud deployment ✅

## Project Structure

### Documentation (this feature)

```text
specs/001-sales-dashboard/
├── spec.md              # Feature specification
├── plan.md              # This file (implementation plan)
├── quickstart.md        # Developer setup and run guide
└── checklists/
    └── requirements.md  # Specification quality checklist
```

### Source Code (repository root)

```text
ai-dev-workflow-tutorial/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies for deployment
├── pyproject.toml           # Project configuration (optional, for uv)
├── .gitignore               # Excludes venv, __pycache__, etc.
├── data/
│   └── sales-data.csv       # Source transaction data (existing)
├── docs/                    # Tutorial documentation (existing)
├── prd/                     # Product requirements (existing)
└── specs/                   # Feature specifications (existing)
```

**Structure Decision**: Single-file Streamlit application (`app.py`) at repository root. This is the simplest structure for a dashboard with no backend API, following Constitution Principle I (simplicity) and Streamlit Community Cloud deployment conventions.

## Implementation Approach

### Data Flow

```text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  sales-data.csv │────▶│  Pandas         │────▶│  Streamlit UI   │
│  (data/)        │     │  DataFrame      │     │  (app.py)       │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                              │
                              ▼
                   ┌─────────────────────────────────────┐
                   │  Aggregations                       │
                   │  • Total Sales (sum of total_amount)│
                   │  • Total Orders (count of order_id) │
                   │  • Monthly sales (groupby date)     │
                   │  • Category sales (groupby category)│
                   │  • Region sales (groupby region)    │
                   └─────────────────────────────────────┘
```

### Application Structure

The `app.py` file will be organized into clear sections:

1. **Imports and Configuration** - Library imports, page config
2. **Data Loading** - Function to load and cache CSV data
3. **Data Processing** - Functions for KPI calculations and aggregations
4. **Chart Creation** - Functions for each Plotly visualization
5. **Main Layout** - Streamlit components arranged per spec (KPIs → trend → bars)

### Key Functions

| Function | Purpose | Returns |
|----------|---------|---------|
| `load_data()` | Load CSV into DataFrame with caching | pd.DataFrame |
| `calculate_total_sales(df)` | Sum of total_amount column | float |
| `calculate_total_orders(df)` | Count of unique order_id values | int |
| `get_monthly_sales(df)` | Aggregate sales by month | pd.DataFrame |
| `get_sales_by_category(df)` | Aggregate and sort by category | pd.DataFrame |
| `get_sales_by_region(df)` | Aggregate and sort by region | pd.DataFrame |
| `create_trend_chart(df)` | Build Plotly line chart | go.Figure |
| `create_category_chart(df)` | Build Plotly bar chart | go.Figure |
| `create_region_chart(df)` | Build Plotly bar chart | go.Figure |

### UI Layout

```text
┌─────────────────────────────────────────────────────────────┐
│  🛒 ShopSmart Sales Dashboard                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────────────┐    ┌─────────────────────┐       │
│   │  💰 Total Sales      │    │  📦 Total Orders     │       │
│   │     $XXX,XXX.XX     │    │        XXX          │       │
│   └─────────────────────┘    └─────────────────────┘       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   📈 Sales Trend Over Time                                  │
│   [Line Chart - Monthly aggregation]                        │
│                                                             │
├──────────────────────────┬──────────────────────────────────┤
│                          │                                  │
│  📊 Sales by Category    │  🗺️ Sales by Region              │
│  [Bar Chart - Sorted]    │  [Bar Chart - Sorted]           │
│                          │                                  │
└──────────────────────────┴──────────────────────────────────┘
```

## Dependencies

### requirements.txt

```text
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.18.0
```

### Development Setup

```bash
# Create virtual environment with uv
uv venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Run locally
streamlit run app.py
```

## Error Handling Strategy

| Scenario | Handling |
|----------|----------|
| CSV file not found | Display friendly error message with st.error() |
| Empty data file | Show KPIs as $0 / 0; display info message on charts |
| Invalid data values | Use pd.to_numeric with errors='coerce'; skip NaN rows |
| Single category/region | Charts render correctly with single bar |

## Deployment

### Streamlit Community Cloud

1. Push code to GitHub repository
2. Connect repository to Streamlit Community Cloud
3. Configure main file path: `app.py`
4. Deploy and obtain public URL

### Required Files for Deployment

- `app.py` - Main application
- `requirements.txt` - Dependencies
- `data/sales-data.csv` - Source data

## Mapping to Specification

| Spec Requirement | Implementation |
|------------------|----------------|
| FR-001: Total Sales display | `calculate_total_sales()` + st.metric |
| FR-002: Total Orders display | `calculate_total_orders()` + st.metric |
| FR-003: Sales trend line chart | `create_trend_chart()` + st.plotly_chart |
| FR-004: Category bar chart (sorted) | `create_category_chart()` + st.plotly_chart |
| FR-005: Region bar chart (sorted) | `create_region_chart()` + st.plotly_chart |
| FR-006: Interactive tooltips | Plotly default hover behavior |
| FR-007: Load from CSV | `load_data()` with @st.cache_data |
| FR-008: Handle CSV columns | Pandas dtype handling in load_data() |
| FR-009: Professional title | st.title() with ShopSmart branding |
| FR-010: Layout ordering | Streamlit component order in main() |

## Complexity Tracking

> No constitution violations. Implementation follows all principles.

| Check | Result |
|-------|--------|
| Single file app | ✅ Simplest viable structure |
| No external APIs | ✅ CSV data only |
| No authentication | ✅ Public access as specified |
| Standard libraries only | ✅ Streamlit, Pandas, Plotly (approved stack) |
