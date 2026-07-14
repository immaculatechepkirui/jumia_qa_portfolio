# Jumia Kenya — QA Portfolio Project

A end-to-end quality assurance portfolio project for [Jumia Kenya](https://www.jumia.co.ke/), East Africa's largest e-commerce platform. This project demonstrates a structured QA process covering manual exploratory testing, bug reporting, test automation, API testing, and performance analysis.

---

## Project Overview

|
 Item 
|
 Detail 
|
|
------
|
--------
|
|
**
Website tested
**
|
 https://www.jumia.co.ke/ 
|
|
**
Tester
**
|
 Immaculata Chepkirui 
|
|
**
Testing type
**
|
 Exploratory, Functional, Regression, API, Performance 
|
|
**
Automation tool
**
|
 Playwright (Python) 
|
|
**
API tool
**
|
 Postman 
|
|
**
Performance tool
**
|
 Google Lighthouse 
|
|
**
Total test cases
**
|
 50 
|

---

## Repository Structure
jumia_qa_portfolio/
│
├── README.md # You are here
│
├── Test Plan/
│ └── test_plan.md # Scope, objectives, risk areas, entry/exit criteria
│
├── Test Cases/
│ ├── exploratory_test_cases.md # All 50 test cases in Markdown
│ └── Jumia_Exploratory_Test_Cases.xlsx # Full test cases with formatting
│
├── Bug Reports/
│ └── bug_reports.md # Bugs found during exploratory testing
│
├── Playwright/
│ ├── tests/ # Automated test scripts
│ │ ├── test_homepage.py
│ │ ├── test_search.py
│ │ └── test_cart.py
│ ├── screenshots/ # Auto-captured on test failure
│ └── requirements.txt # Python dependencies
│
├── Postman/
│ └── Jumia_API_Tests.json # Exported Postman collection
│
├── Performance Report/
│ └── performance_report.md # Lighthouse audit findings
│
└── Screenshots/
└── # Manual testing evidence


---

## Testing Areas Covered

| Area | Test Cases | Automation |
|------|-----------|------------|
| Homepage Load | TC-001 – TC-004 | ✅ |
| Search Functionality | TC-005 – TC-010 | ✅ |
| Product Detail Page | TC-011 – TC-015 | ❌ Manual only |
| Shopping Cart | TC-016 – TC-020 | ✅ |
| User Registration & Login | TC-021 – TC-026 | ❌ Manual only |
| Navigation | TC-027 – TC-030 | ❌ Manual only |
| Product Listing & Filters | TC-031 – TC-034 | ❌ Manual only |
| Checkout & Payment | TC-035 – TC-038 | ❌ Manual only |
| Flash Sales | TC-039 – TC-040 | ❌ Manual only |
| Responsive Design | TC-041 – TC-042 | ❌ Manual only |
| Help & Support | TC-043 – TC-044 | ❌ Manual only |
| Wishlist | TC-045 – TC-046 | ❌ Manual only |
| Error Handling | TC-047 – TC-048 | ❌ Manual only |
| Newsletter | TC-049 – TC-050 | ❌ Manual only |

---

## How to Run the Automated Tests

### Prerequisites

- Python 3.10+
- pip

### Setup

```bash
# Clone the repository
git clone git@github.com:immaculatechepkirui/jumia_qa_portfolio.git
cd jumia_qa_portfolio

# Install dependencies
pip install -r Playwright/requirements.txt

# Install Playwright browsers
playwright install chromium
```

### Run all tests

```bash
pytest Playwright/tests/
```

### Run a specific test file

```bash
pytest Playwright/tests/test_search.py
```

### Run with headed browser (visible window)

```bash
pytest Playwright/tests/ --headed
```

Screenshots are saved automatically to `Playwright/screenshots/` on test failure.

---

## Key Findings

| # | Area | Finding | Severity |
|---|------|---------|---------|
| BUG-001 | Search | Autocomplete dropdown does not close when clicking outside it | Low |
| BUG-002 | Filters | Applying multiple filters simultaneously causes a page reload that resets scroll position to top | Medium |
| BUG-003 | Cart | Quantity input accepts 0 and negative values without validation | High |
| BUG-004 | Mobile | Category nav overlaps search bar at 375px viewport on some browsers | Medium |
| BUG-005 | Performance | Homepage LCP (Largest Contentful Paint) exceeds 4s on a simulated 4G connection | Medium |

Full details in [`Bug Reports/bug_reports.md`](./Bug%20Reports/bug_reports.md).

---

## Performance Summary

Tested with Google Lighthouse 13.3.0 on an emulated Moto G Power with Slow 4G throttling.

| Metric | Score | Rating |
|--------|-------|--------|
| Performance | 31/100 | 🔴 Poor |
| Accessibility | 92/100 | 🟢 Good |
| Best Practices | 58/100 | 🔴 Poor |
| SEO | 92/100 | 🟢 Good |

Full report in [`Performance Report/performance_report.md`](./Performance%20Report/performance_report.md).

---

## Skills Demonstrated

- ✅ Exploratory testing methodology
- ✅ Writing structured test cases (Test ID, preconditions, steps, expected vs actual)
- ✅ Bug reporting with severity classification
- ✅ Test automation with Playwright and Python
- ✅ API testing with Postman
- ✅ Performance auditing with Lighthouse
- ✅ Documentation in Markdown
- ✅ Version control with Git and GitHub

---

## Author

**Immaculata Chepkirui**  git