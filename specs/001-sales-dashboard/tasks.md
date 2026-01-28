# Tasks: ShopSmart Sales Dashboard

**Input**: Design documents from `/specs/001-sales-dashboard/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Not explicitly requested in specification. Manual testing via Streamlit local server.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `app.py` at repository root (per plan.md)
- **Data**: `data/sales-data.csv` (existing)
- **Dependencies**: `requirements.txt` at repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and Python environment setup

- [x] T001 Create requirements.txt with streamlit>=1.28.0, pandas>=2.0.0, plotly>=5.18.0 in repository root
- [x] T002 Create virtual environment using uv and install dependencies
- [x] T003 Create app.py with imports (streamlit, pandas, plotly.express) and page configuration in repository root
- [x] T004 [P] Update .gitignore to exclude .venv/, __pycache__/, .streamlit/ if not already present

**Checkpoint**: Environment ready - can run `streamlit run app.py` without errors

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Data loading infrastructure that ALL user stories depend on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Implement load_data() function with @st.cache_data decorator to load data/sales-data.csv in app.py
- [x] T006 Add error handling in load_data() for missing file scenario with st.error() message in app.py
- [x] T007 Add date column parsing in load_data() using pd.to_datetime() in app.py
- [x] T008 Implement main() function skeleton with st.title("ShopSmart Sales Dashboard") in app.py
- [x] T009 Add data loading call in main() with error state handling in app.py

**Checkpoint**: Foundation ready - dashboard loads CSV data and displays title. User story implementation can now begin.

---

## Phase 3: User Story 1 - View Key Business Metrics (Priority: P1) 🎯 MVP

**Goal**: Display Total Sales and Total Orders KPIs prominently at the top of the dashboard

**Independent Test**: Load dashboard and verify Total Sales shows ~$650,000-$700,000 formatted as currency, Total Orders shows 482 formatted with separators

### Implementation for User Story 1

- [x] T010 [US1] Implement calculate_total_sales(df) function that returns sum of total_amount column in app.py
- [x] T011 [US1] Implement calculate_total_orders(df) function that returns count of unique order_id values in app.py
- [x] T012 [US1] Add KPI display section using st.columns(2) for side-by-side layout in app.py
- [x] T013 [US1] Display Total Sales using st.metric() with currency formatting (${:,.2f}) in app.py
- [x] T014 [US1] Display Total Orders using st.metric() with number formatting ({:,}) in app.py
- [x] T015 [US1] Verify KPI calculations match expected values (~$650K-$700K sales, 482 orders)

**Checkpoint**: User Story 1 complete - KPIs visible and accurate. This is a functional MVP.

---

## Phase 4: User Story 2 - Analyze Sales Trends Over Time (Priority: P2)

**Goal**: Display line chart showing monthly sales trends with interactive tooltips

**Independent Test**: Load dashboard and verify line chart shows 12 data points (one per month), chronologically ordered, with tooltips on hover

### Implementation for User Story 2

- [ ] T016 [US2] Implement get_monthly_sales(df) function that groups by month and sums total_amount in app.py
- [ ] T017 [US2] Implement create_trend_chart(monthly_df) function using plotly.express.line() in app.py
- [ ] T018 [US2] Configure trend chart with title "Sales Trend Over Time", x-axis label "Month", y-axis label "Sales ($)" in app.py
- [ ] T019 [US2] Add trend chart to dashboard layout using st.plotly_chart() with use_container_width=True in app.py
- [ ] T020 [US2] Verify trend chart displays 12 months of data in chronological order with working tooltips

**Checkpoint**: User Story 2 complete - Trend analysis available. Dashboard now shows KPIs + trend.

---

## Phase 5: User Story 3 - Compare Sales by Product Category (Priority: P3)

**Goal**: Display bar chart showing sales by category, sorted highest to lowest with interactive tooltips

**Independent Test**: Load dashboard and verify bar chart shows 5 categories (Electronics, Accessories, Audio, Wearables, Smart Home), sorted by sales value descending

### Implementation for User Story 3

- [ ] T021 [US3] Implement get_sales_by_category(df) function that groups by category, sums total_amount, and sorts descending in app.py
- [ ] T022 [US3] Implement create_category_chart(category_df) function using plotly.express.bar() in app.py
- [ ] T023 [US3] Configure category chart with title "Sales by Category", x-axis label "Category", y-axis label "Sales ($)" in app.py
- [ ] T024 [US3] Add category chart to dashboard layout in left column using st.plotly_chart() in app.py
- [ ] T025 [US3] Verify category chart displays all 5 categories sorted by value with working tooltips

**Checkpoint**: User Story 3 complete - Category analysis available. Dashboard now shows KPIs + trend + categories.

---

## Phase 6: User Story 4 - Compare Sales by Geographic Region (Priority: P4)

**Goal**: Display bar chart showing sales by region, sorted highest to lowest with interactive tooltips

**Independent Test**: Load dashboard and verify bar chart shows 4 regions (North, South, East, West), sorted by sales value descending

### Implementation for User Story 4

- [ ] T026 [US4] Implement get_sales_by_region(df) function that groups by region, sums total_amount, and sorts descending in app.py
- [ ] T027 [US4] Implement create_region_chart(region_df) function using plotly.express.bar() in app.py
- [ ] T028 [US4] Configure region chart with title "Sales by Region", x-axis label "Region", y-axis label "Sales ($)" in app.py
- [ ] T029 [US4] Add region chart to dashboard layout in right column (beside category chart) using st.plotly_chart() in app.py
- [ ] T030 [US4] Verify region chart displays all 4 regions sorted by value with working tooltips

**Checkpoint**: User Story 4 complete - All 4 user stories implemented. Full dashboard functionality achieved.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements and deployment preparation

- [ ] T031 Add professional styling with consistent color scheme across all charts in app.py
- [ ] T032 Add empty state handling for charts when data has no records in app.py
- [ ] T033 Verify dashboard loads within 5 seconds performance target
- [ ] T034 Test dashboard in Chrome, Firefox, Safari, and Edge browsers
- [ ] T035 Run quickstart.md validation checklist to confirm all acceptance criteria met
- [ ] T036 Prepare for Streamlit Community Cloud deployment (verify requirements.txt and app.py are at root)

**Checkpoint**: Dashboard production-ready. All success criteria met.

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1: Setup
    ↓
Phase 2: Foundational (BLOCKS all user stories)
    ↓
Phase 3: User Story 1 (P1) ──┬── Phase 4: User Story 2 (P2)
                             │
                             ├── Phase 5: User Story 3 (P3)
                             │
                             └── Phase 6: User Story 4 (P4)
                                          ↓
                                   Phase 7: Polish
```

### User Story Dependencies

- **User Story 1 (P1)**: Depends on Phase 2 only - No dependencies on other stories
- **User Story 2 (P2)**: Depends on Phase 2 only - Can run in parallel with US1
- **User Story 3 (P3)**: Depends on Phase 2 only - Can run in parallel with US1, US2
- **User Story 4 (P4)**: Depends on Phase 2 only - Can run in parallel with US1, US2, US3

### Within Each User Story

1. Data processing function first (get_* or calculate_*)
2. Chart creation function second (create_*_chart)
3. Layout integration third (st.plotly_chart or st.metric)
4. Verification last

### Parallel Opportunities

- T003 and T004 can run in parallel (different files)
- All user stories (Phase 3-6) can run in parallel after Phase 2 completes
- Within Phase 7, T031-T034 can run in parallel

---

## Parallel Example: After Foundational Phase

```bash
# All user stories can start simultaneously after Phase 2:
Task: T010-T015 (User Story 1: KPIs)
Task: T016-T020 (User Story 2: Trend Chart)
Task: T021-T025 (User Story 3: Category Chart)
Task: T026-T030 (User Story 4: Region Chart)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T009)
3. Complete Phase 3: User Story 1 (T010-T015)
4. **STOP and VALIDATE**: Dashboard shows KPIs - this is a working MVP!
5. Deploy to Streamlit Community Cloud if desired

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add User Story 1 → Deploy/Demo (MVP with KPIs!)
3. Add User Story 2 → Deploy/Demo (adds trend chart)
4. Add User Story 3 → Deploy/Demo (adds category breakdown)
5. Add User Story 4 → Deploy/Demo (adds region breakdown)
6. Polish → Final release

### Single Developer Strategy (Recommended)

Execute phases sequentially in priority order:
1. Phase 1 → Phase 2 → Phase 3 (MVP) → Phase 4 → Phase 5 → Phase 6 → Phase 7

---

## Task Summary

| Phase | Description | Task Count |
|-------|-------------|------------|
| Phase 1 | Setup | 4 tasks |
| Phase 2 | Foundational | 5 tasks |
| Phase 3 | User Story 1 (KPIs) | 6 tasks |
| Phase 4 | User Story 2 (Trend) | 5 tasks |
| Phase 5 | User Story 3 (Category) | 5 tasks |
| Phase 6 | User Story 4 (Region) | 5 tasks |
| Phase 7 | Polish | 6 tasks |
| **Total** | | **36 tasks** |

---

## Notes

- All tasks modify `app.py` (single-file architecture per constitution)
- [P] tasks = can run in parallel with other [P] tasks in same phase
- [USn] label maps task to specific user story for Jira traceability
- Each user story is independently testable after completion
- Commit after each phase or logical group of tasks
- Use Jira key format: `ECOM-X: description` for all commits
