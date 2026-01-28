# AI-Dev-Workflow Tutorial Project

## Project Overview

This is an educational tutorial repository for learning AI-assisted development workflows. The project teaches students how to build technology solutions using Cursor, Claude Code, GitHub, and Jira following professional development practices.

## Project Purpose

The tutorial demonstrates a complete, end-to-end workflow:
1. **PRD** → Product Requirements Document defines what to build
2. **spec-kit** → AI-assisted tooling refines requirements into technical plans
3. **Jira** → Task tracking and project management
4. **Code** → Building with AI assistance (Claude Code)
5. **Git/GitHub** → Version control and collaboration
6. **Deploy** → Making solutions publicly accessible (Streamlit Community Cloud)

## What You Will Build

A **Streamlit sales dashboard** for a fictional e-commerce retailer (ShopSmart) that displays:
- 2 KPI scorecards (Total Sales, Number of Orders)
- 1 line chart (sales trend over time)
- 2 bar charts (sales by category and region)

## Project Structure

```
ai-dev-workflow-tutorial/
├── README.md                    # Main tutorial overview and quick start
├── CLAUDE.md                    # This file - project context for AI assistants
├── docs/                        # Tutorial documentation
│   ├── 00-overview.md          # Tutorial objectives and workflow overview
│   ├── 01-session-1-setup.md   # Account creation and tool installation
│   ├── 02-terminal-basics.md   # Command line reference (optional)
│   ├── 03-git-concepts.md      # Git version control reference (optional)
│   ├── 04-session-2-workflow.md # Complete development workflow
│   ├── 05-troubleshooting.md   # Common issues and solutions
│   ├── 06-capstone-project-dev-environment.md # Capstone setup guide
│   ├── 07-faq.md               # Frequently asked questions
│   └── 08-glossary.md          # Key terms and definitions
├── prd/                         # Product Requirements Documents
│   └── ecommerce-analytics.md  # PRD for the sales dashboard project
└── data/                        # Sample datasets
    └── sales-data.csv          # Sales transaction data for the dashboard
```

## Key Files

### Documentation
- **README.md**: Start here. Provides overview, prerequisites, and links to all documentation.
- **docs/00-overview.md**: Deep dive into tutorial objectives, workflow, and key concepts.
- **docs/01-session-1-setup.md**: Step-by-step setup instructions for accounts and tools.
- **docs/04-session-2-workflow.md**: The main workflow tutorial (spec-kit → Jira → code → deploy).

### Requirements
- **prd/ecommerce-analytics.md**: Complete Product Requirements Document for the Streamlit dashboard. Includes:
  - Problem statement and goals
  - User stories
  - Functional and non-functional requirements
  - Data specification
  - Technical approach
  - Acceptance criteria

### Data
- **data/sales-data.csv**: Sample sales transaction data with columns:
  - `date`: Transaction date
  - `order_id`: Unique order identifier
  - `product`: Product name
  - `category`: Product category (Electronics, Accessories, Audio, Wearables, Smart Home)
  - `region`: Geographic region (North, South, East, West)
  - `quantity`: Units sold
  - `unit_price`: Price per unit
  - `total_amount`: Total transaction value

## Technology Stack

- **Python 3.11+**: Programming language
- **Streamlit**: Web application framework for dashboards
- **Pandas**: Data processing and manipulation
- **Plotly**: Interactive charting library
- **Git/GitHub**: Version control
- **Jira**: Task tracking
- **spec-kit**: Spec-driven development toolkit
- **Claude Code**: AI assistant for development

## Development Workflow

### Session 1: Setup
1. Create accounts (GitHub, Atlassian/Jira, Claude Pro)
2. Install tools (Cursor, Git, Python, uv, spec-kit, Claude Code)
3. Fork and clone repository
4. Initialize Claude Code (creates this file)

### Session 2: Build Dashboard
1. Connect Atlassian MCP server to Claude Code
2. Use spec-kit to create specification and plan from PRD
3. Create Jira issues from spec-kit tasks
4. Build Streamlit dashboard with Claude Code assistance
5. Commit changes with Jira keys (e.g., `ECOM-1: add sales dashboard`)
6. Push to GitHub
7. Deploy to Streamlit Community Cloud

## Naming Conventions

- **Jira Project Key**: `ECOM` (uppercase)
- **Jira Issues**: `ECOM-1`, `ECOM-2`, etc.
- **Commit Messages**: `ECOM-1: description of changes`

## How to Work with This Project

### For Students
1. Read documentation in order: `00-overview.md` → `01-session-1-setup.md` → `04-session-2-workflow.md`
2. Follow setup instructions in Session 1
3. Complete the workflow in Session 2 to build the dashboard
4. Reference troubleshooting and FAQ docs as needed

### For AI Assistants
When helping with this project:
- **Understand the workflow**: This is a tutorial, so explain concepts and best practices
- **Follow the PRD**: The dashboard requirements are in `prd/ecommerce-analytics.md`
- **Use proper naming**: Commit messages should include Jira keys (e.g., `ECOM-1:`)
- **Maintain traceability**: Link code changes to Jira issues
- **Reference documentation**: Point students to relevant docs when appropriate

### Building the Dashboard

The dashboard should:
1. Load data from `data/sales-data.csv`
2. Display two KPI cards at the top:
   - Total Sales (formatted as currency)
   - Total Orders (formatted as number)
3. Show a line chart of sales trend over time
4. Show two bar charts:
   - Sales by category (sorted by value)
   - Sales by region (sorted by value)

Expected values (approximate):
- Total Sales: ~$650,000 - $700,000
- Total Orders: 482

## Key Concepts

### Traceability
Every code change should be traceable to a Jira issue:
```
Jira Issue: ECOM-1 "Create sales dashboard"
     ↓
Commit: "ECOM-1: add sales dashboard with KPIs and charts"
     ↓
Push: Code on GitHub, linked to Jira
     ↓
Deploy: Dashboard live on Streamlit Community Cloud
```

### Spec-Driven Development
1. Start with PRD (requirements)
2. Use spec-kit to create technical specification
3. Generate plan and tasks
4. Create Jira issues from tasks
5. Implement with AI assistance
6. Deploy and verify

## Common Tasks

### Initial Setup
- Verify all tools are installed: `git --version`, `python --version`, `uv --version`, `specify --help`, `claude --version`
- Ensure repository is forked and cloned
- Verify Jira project exists (ECOM)

### Building Features
- Reference PRD for requirements
- Create Jira issue for the feature
- Build with AI assistance
- Commit with Jira key in message
- Push to GitHub
- Update Jira issue with commit hash and GitHub link

### Troubleshooting
- Check `docs/05-troubleshooting.md` for common issues
- Verify tool installations
- Check Git configuration
- Ensure Python environment is correct

## Next Steps

After initialization:
1. Complete Session 1 setup if not done
2. Move to Session 2 workflow
3. Use spec-kit to create specification from PRD
4. Build the dashboard following the workflow

## Additional Resources

- Streamlit docs: https://docs.streamlit.io
- Plotly docs: https://plotly.com/python/
- Pandas docs: https://pandas.pydata.org/docs/
- Git docs: https://git-scm.com/doc
- GitHub docs: https://docs.github.com

---

*This file helps AI assistants understand the project context and provide better assistance during development.*
