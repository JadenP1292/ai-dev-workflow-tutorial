<!--
Sync Impact Report
==================
Version change: N/A → 1.0.0 (Initial creation)

Modified principles: N/A (new constitution)

Added sections:
- Core Principles (4 principles)
- Technology Stack section
- Development Workflow section
- Governance section

Removed sections: N/A

Templates requiring updates:
- .specify/templates/plan-template.md ✅ (Constitution Check section aligns with principles)
- .specify/templates/spec-template.md ✅ (Requirements section compatible)
- .specify/templates/tasks-template.md ✅ (Phase structure compatible)

Follow-up TODOs: None
-->

# E-Commerce Analytics Dashboard Constitution

## Core Principles

### I. Code Simplicity and Readability

All code MUST be simple, readable, and self-documenting. This is non-negotiable for a learning-focused project.

- Functions MUST have single, clear responsibilities
- Variable and function names MUST be descriptive (e.g., `calculate_total_sales`, not `calc`)
- Code MUST follow PEP 8 style guidelines
- Complex logic MUST include inline comments explaining the "why"
- Avoid premature optimization—clarity takes precedence over cleverness

**Rationale**: This project serves as an educational tutorial. Code must be accessible to learners and maintainable by developers of varying skill levels.

### II. User-Friendly Interactive Visualizations

All dashboard visualizations MUST prioritize user experience and accessibility.

- Charts MUST have clear, descriptive titles and axis labels
- Interactive tooltips MUST display exact values on hover
- Color schemes MUST be professional and accessible
- Layout MUST be intuitive with KPIs prominently displayed at the top
- All visualizations MUST render within 2 seconds

**Rationale**: The dashboard serves non-technical stakeholders (executives, managers). Visualizations must communicate insights immediately without requiring technical knowledge.

### III. Python Best Practices

All Python code MUST adhere to established best practices and conventions.

- Use type hints for function parameters and return values where beneficial
- Handle exceptions gracefully with informative error messages
- Use Pandas efficiently for data operations (vectorized operations over loops)
- Organize imports following PEP 8 (standard library, third-party, local)
- Use f-strings for string formatting
- Avoid global variables; pass data explicitly through function parameters

**Rationale**: Following Python conventions ensures the codebase remains professional, maintainable, and serves as a good example for learners.

### IV. Virtual Environment Isolation

All project dependencies MUST be managed through Python virtual environments.

- Project MUST use `uv` for dependency management
- Dependencies MUST be explicitly declared in `pyproject.toml` or `requirements.txt`
- Virtual environment MUST NOT be committed to version control
- README MUST include clear instructions for environment setup
- All development and execution MUST occur within the virtual environment

**Rationale**: Dependency isolation prevents conflicts with system Python and other projects, ensures reproducibility, and aligns with professional development practices.

## Technology Stack

This section defines the approved technology choices for the project.

| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| Language | Python | 3.11+ | Core programming language |
| Framework | Streamlit | Latest | Web dashboard framework |
| Visualization | Plotly | Latest | Interactive charts |
| Data Processing | Pandas | Latest | Data manipulation |
| Package Manager | uv | Latest | Dependency management |
| Version Control | Git/GitHub | N/A | Source control and collaboration |
| Deployment | Streamlit Community Cloud | N/A | Public hosting |

**Constraints**:
- No additional frameworks beyond those listed without explicit justification
- All dependencies MUST be compatible with Streamlit Community Cloud deployment
- Prefer standard library solutions before adding external dependencies

## Development Workflow

This section defines the required workflow for all development activities.

### Code Organization
- Main application file: `app.py` or `dashboard.py` at repository root
- Data files: `data/` directory
- Documentation: `docs/` directory

### Commit Standards
- Commit messages MUST include Jira issue key (e.g., `ECOM-1: add sales KPI cards`)
- Each commit SHOULD represent a logical, complete unit of work
- Commits MUST NOT include broken or non-functional code

### Testing Approach
- Manual testing through Streamlit local server during development
- Verify all charts render correctly with sample data
- Confirm KPI values match expected calculations
- Test in multiple browsers before deployment

### Deployment Requirements
- Dashboard MUST be deployable to Streamlit Community Cloud
- Deployed application MUST be accessible via public URL
- Deployment MUST NOT require environment variables or secrets for basic functionality

## Governance

This constitution establishes the guiding principles for the E-Commerce Analytics Dashboard project. All code contributions and design decisions MUST align with these principles.

### Amendment Process
1. Proposed changes MUST be documented with rationale
2. Changes to Core Principles require team discussion
3. All amendments MUST update the version number and Last Amended date

### Versioning Policy
- **MAJOR**: Changes to core principles that affect existing code
- **MINOR**: New sections or expanded guidance added
- **PATCH**: Clarifications and wording improvements

### Compliance
- All pull requests SHOULD be reviewed against these principles
- Constitution violations MUST be addressed before merge
- When principles conflict, prioritize in order: I, II, III, IV

**Version**: 1.0.0 | **Ratified**: 2026-01-27 | **Last Amended**: 2026-01-27
