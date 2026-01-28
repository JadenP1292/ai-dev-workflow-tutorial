# Quickstart: ShopSmart Sales Dashboard

This guide walks you through setting up and running the sales dashboard locally.

## Prerequisites

- Python 3.11 or higher
- uv package manager (recommended) or pip
- Git

## Setup

### 1. Clone the Repository (if not already done)

```bash
git clone <your-fork-url>
cd ai-dev-workflow-tutorial
```

### 2. Create Virtual Environment

Using uv (recommended):
```bash
uv venv
```

Or using Python directly:
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

macOS/Linux:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

Using uv:
```bash
uv pip install -r requirements.txt
```

Or using pip:
```bash
pip install -r requirements.txt
```

## Running the Dashboard

### Local Development

```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`.

### Expected Output

When the dashboard loads successfully, you should see:

| Component | Expected Value |
|-----------|----------------|
| Total Sales | ~$650,000 - $700,000 |
| Total Orders | 482 |
| Trend Chart | 12 months of data points |
| Category Chart | 5 bars (Electronics, Audio, etc.) |
| Region Chart | 4 bars (North, South, East, West) |

## Verification Checklist

- [ ] Dashboard loads without errors
- [ ] Both KPI cards display formatted values
- [ ] Line chart shows monthly sales trend
- [ ] Category bar chart is sorted highest to lowest
- [ ] Region bar chart is sorted highest to lowest
- [ ] Hovering over charts shows tooltips with exact values

## Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"

Ensure your virtual environment is activated and dependencies are installed:
```bash
source .venv/bin/activate
uv pip install -r requirements.txt
```

### "FileNotFoundError: data/sales-data.csv"

Verify the data file exists:
```bash
ls data/sales-data.csv
```

### Dashboard shows $0 / 0 orders

Check that the CSV file contains data (not just headers):
```bash
wc -l data/sales-data.csv
# Should show ~483 lines (1 header + 482 transactions)
```

### Charts not rendering

Ensure Plotly is installed:
```bash
uv pip install plotly
```

## Deployment to Streamlit Community Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository and branch
5. Set main file path to `app.py`
6. Click "Deploy"

Your dashboard will be available at a public URL like:
`https://<your-app>.streamlit.app`

## Project Files

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application |
| `requirements.txt` | Python dependencies |
| `data/sales-data.csv` | Sales transaction data |

## Next Steps

After verifying the dashboard works locally:

1. Make any desired customizations
2. Commit changes with Jira key: `git commit -m "ECOM-1: add sales dashboard"`
3. Push to GitHub: `git push origin 001-sales-dashboard`
4. Deploy to Streamlit Community Cloud
5. Share the public URL with stakeholders
