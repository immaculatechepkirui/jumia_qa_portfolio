# Jumia Kenya — Test Plan

**Project:** Jumia Kenya E-Commerce Platform QA  
**Tester:** Immaculata Chepkirui  
**Date:** July 2026  
**Version:** 1.0  

---

## 1. Objective

To evaluate the functional correctness, usability, performance, and API behaviour
of the Jumia Kenya e-commerce platform (jumia.co.ke) from the perspective of an
end user, and to document all findings in a structured, reproducible format
suitable for a development team to act on.

---

## 2. Scope

### In Scope
- Homepage load and key UI elements
- Search functionality (keyword search, filters, sorting, autocomplete)
- Product detail pages (information completeness, pricing, images)
- Shopping cart (add, update quantity, remove, persistence)
- User authentication (registration, login, password reset)
- Category navigation and breadcrumbs
- Product listing filters (price, brand, pagination)
- Checkout flow (auth gate, order summary, delivery address, payment options)
- Flash Sales page
- Responsive design (mobile 375px, tablet 768px)
- Help & Support pages
- Wishlist functionality
- Error handling (404 pages, form validation)
- Newsletter subscription
- Performance audit (Lighthouse)
- API-level HTTP behaviour (status codes, response times, error handling)

### Out of Scope
- Backend database or server-side code
- Payment processing (no real transactions executed)
- Third-party integrations (M-Pesa, Visa, Mastercard APIs)
- Admin/vendor portal
- Jumia mobile app (iOS/Android)
- Load testing or stress testing
- Security penetration testing

---

## 3. Test Approach

This project uses a combination of three testing approaches:

**Exploratory Testing**  
Systematic manual exploration of the platform covering 14 functional areas,
executing 50 test cases and documenting actual vs expected results.

**Automated Functional Testing**  
Playwright (Python) scripts automating critical user flows — homepage, search,
and cart — run against Chromium with pytest as the test runner.

**API Testing**  
Postman collection testing HTTP-level behaviour of 11 endpoints covering search,
product pages, navigation, and error handling.

**Performance Testing**  
Google Lighthouse audit run on the homepage under Slow 4G throttling on an
emulated Moto G Power device.

---

## 4. Test Environment

| Component | Detail |
|-----------|--------|
| Application under test | https://www.jumia.co.ke |
| Browser | Google Chrome 126 |
| Operating system | Ubuntu Linux 24.04 |
| Device | HP EliteBook 845 G8 |
| Automation framework | Playwright 1.61.0 + pytest 9.1.1 |
| API tool | Postman |
| Performance tool | Google Lighthouse 13.3.0 |
| Mobile emulation | Chrome DevTools — 375px (iPhone SE), 768px (iPad) |
| Network emulation | Slow 4G (Lighthouse audit) |

---

## 5. Entry Criteria

Testing begins when:
- The application is accessible at https://www.jumia.co.ke without a maintenance page
- A stable internet connection is available
- Chrome browser and Playwright are installed and verified
- Postman is installed and the collection is imported

---

## 6. Exit Criteria

Testing is complete when:
- All 50 manual test cases have been executed and results recorded
- All Playwright automated tests have been run and results documented
- All Postman requests have been run and results documented
- All bugs found have been logged with severity, steps to reproduce, and expected vs actual results
- The Lighthouse performance audit has been completed and findings documented

---

## 7. Test Deliverables

| Deliverable | Location |
|-------------|----------|
| Test Plan | `Test Plan/test_plan.md` |
| Manual Test Cases (Markdown) | `Test Cases/exploratory_test_cases.md` |
| Manual Test Cases (Excel) | `Test Cases/Jumia_KE_Exploratory_Test_Cases.xlsx` |
| Bug Reports | `Bug Reports/bug_reports.md` |
| Playwright Test Scripts | `Playwright/tests/` |
| Postman Collection | `Postman/Jumia_API_Tests.json` |
| Postman Documentation | `Postman/README.md` |
| Performance Report | `Performance Report/performance_report.md` |

---

## 8. Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Jumia website content changes between test runs | Selectors break in Playwright | Use href-based and structural selectors rather than text-based where possible |
| Network latency affects response time assertions | False failures in Postman | Set generous timeouts (20s) reflecting real-world conditions |
| Newsletter popup and banners block UI interactions | Automated tests fail | Implement `dismiss_overlays()` helper in all test files |
| Autocomplete suppressed in headless browsers | TC-008 cannot be automated reliably | Marked `xfail` with documented reason; verified manually in headed mode |
| Cart is empty during checkout test | TC-035 cannot execute | Marked as `skipped` with documented precondition; login required to add items |
| Jumia homepage never reaches `networkidle` state | Playwright timeouts | Use `domcontentloaded` + explicit `wait_for_timeout()` instead |
| JavaScript-rendered content not in raw HTTP response | Postman cannot assert on dynamic UI elements | Validate JS-rendered elements via Playwright; validate static HTML via Postman |

---

## 9. Bug Severity Classification

| Severity | Definition |
|----------|------------|
| Critical | Core user journey completely broken; no workaround |
| High | Major functionality impaired; no workaround available |
| Medium | Functionality works but with a noticeable defect or poor UX |
| Low | Minor or cosmetic issue; does not affect core flows |

---

## 10. Summary of Results

| Area | Total TCs | Passed | Failed | Automated |
|------|-----------|--------|--------|-----------|
| Homepage | 4 | 4 | 0 | ✅ |
| Search | 6 | 6 | 0 | ✅ |
| Product Detail | 5 | 5 | 0 | ✅ |
| Shopping Cart | 5 | 5 | 0 | ✅ |
| User Auth | 6 | 6 | 0 | ❌ |
| Navigation | 4 | 4 | 0 | ✅ |
| Filters | 4 | 4 | 0 | ❌ |
| Checkout | 4 | 4 | 0 | ✅ |
| Flash Sales | 2 | 2 | 0 | ❌ |
| Responsive | 2 | 2 | 0 | ❌ |
| Help & Support | 2 | 2 | 0 | ❌ |
| Wishlist | 2 | 2 | 0 | ❌ |
| Error Handling | 2 | 2 | 0 | ❌ |
| Newsletter | 2 | 2 | 0 | ❌ |
| **Total** | **50** | **50** | **0** | **8 areas** |

**Bugs found:** 5 (1 High, 3 Medium, 1 Low)  
**Automated tests:** 16 total — 14 passed, 1 skipped, 1 xfailed  
**API tests:** 11 endpoints — results in `Postman/README.md`  
**Performance score:** 31/100 (Poor) — full report in `Performance Report/`