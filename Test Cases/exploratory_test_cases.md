# Jumia Kenya — Exploratory Test Cases

**Website:** https://www.jumia.co.ke/  
**Tester:** Immaculata Chepkirui  
**Date:** July 2025  
**Total Test Cases:** 50  
**Tool:** Manual / Browser  

---

## Test Case Summary

| Test ID | Scenario | Status | Priority |
|---------|----------|--------|----------|
| TC-001 | Homepage loads successfully | PASS | High |
| TC-002 | Hero banner images render without broken links | PASS | Medium |
| TC-003 | Category navigation menu displays all main categories | PASS | High |
| TC-004 | Flash Sale countdown timer is displayed and counts down | PASS | Medium |
| TC-005 | Search returns relevant results for a valid keyword | PASS | High |
| TC-006 | Search with an empty query does not break the page | PASS | Medium |
| TC-007 | Search with a non-existent product shows a no results message | PASS | Medium |
| TC-008 | Search autocomplete suggestions appear while typing | PASS | Low |
| TC-009 | Search results can be filtered by category | PASS | High |
| TC-010 | Search results can be sorted by price low to high | PASS | Medium |
| TC-011 | Product detail page shows complete product information | PASS | High |
| TC-012 | Product image gallery allows switching between images | PASS | Medium |
| TC-013 | Discounted product shows both original and discounted price | PASS | Medium |
| TC-014 | Add to Wishlist button is visible on product page | PASS | Low |
| TC-015 | Product seller name and rating are displayed | PASS | Low |
| TC-016 | Adding a product to the cart works correctly | PASS | High |
| TC-017 | Cart page displays added items correctly | PASS | High |
| TC-018 | Quantity of an item in the cart can be increased | PASS | High |
| TC-019 | Item can be removed from the cart | PASS | High |
| TC-020 | Cart persists items after page refresh | PASS | Medium |
| TC-021 | New user can register with valid details | PASS | High |
| TC-022 | Registration fails when a duplicate email is used | PASS | High |
| TC-023 | Registered user can log in with correct credentials | PASS | High |
| TC-024 | Login fails with incorrect password | PASS | High |
| TC-025 | Login form validates empty fields | PASS | Medium |
| TC-026 | Forgot Password link navigates to password reset page | PASS | Medium |
| TC-027 | Clicking a top-level category navigates to correct listing page | PASS | High |
| TC-028 | Jumia logo returns user to homepage | PASS | Medium |
| TC-029 | Footer links are functional — Help Center | PASS | Low |
| TC-030 | Breadcrumb navigation works on a category page | PASS | Low |
| TC-031 | Price range filter narrows down results correctly | PASS | High |
| TC-032 | Brand filter returns only products from selected brand | PASS | Medium |
| TC-033 | Pagination navigates to correct next page of results | PASS | Medium |
| TC-034 | Multiple filters can be applied simultaneously | PASS | Medium |
| TC-035 | Checkout page requires login for unauthenticated users | PASS | High |
| TC-036 | Checkout shows correct order summary including item prices | PASS | High |
| TC-037 | Pay on Delivery option is available as a payment method | PASS | High |
| TC-038 | Delivery address can be added during checkout | PASS | High |
| TC-039 | Flash Sales page loads and displays current sale items | PASS | Medium |
| TC-040 | Out-of-stock flash sale items are clearly marked | PASS | Medium |
| TC-041 | Homepage displays correctly at mobile viewport 375px | PASS | High |
| TC-042 | Product listing page adapts to tablet viewport 768px | PASS | Medium |
| TC-043 | Help Center page loads and displays FAQ categories | PASS | Low |
| TC-044 | WhatsApp chat link opens correctly | PASS | Low |
| TC-045 | Logged-in user can add a product to the wishlist | PASS | Medium |
| TC-046 | Wishlist page shows all saved products | PASS | Medium |
| TC-047 | 404 page displays correctly for a non-existent URL | PASS | Medium |
| TC-048 | Page load completes without JS console errors on homepage | PASS | Low |
| TC-049 | Newsletter subscription with valid email works | PASS | Low |
| TC-050 | Newsletter subscription fails without accepting terms | PASS | Low |

---

## Detailed Test Cases

### TC-001 — Homepage loads successfully

| Field | Detail |
|-------|--------|
| **Scenario** | Homepage Load |
| **Preconditions** | User has internet access; browser is open |
| **Steps** | 1. Open https://www.jumia.co.ke/ in a browser |
| **Expected Result** | Page loads within a reasonable time; Jumia logo, navigation bar, category menu, hero banner and product sections are all visible |
| **Actual Result** | Page loaded successfully. Logo, top nav, category menu, hero banner and promotional sections all displayed correctly |
| **Status** | PASS |
| **Priority** | High |

---

### TC-002 — Hero banner images render without broken links

| Field | Detail |
|-------|--------|
| **Scenario** | Homepage Load |
| **Preconditions** | Homepage is loaded |
| **Steps** | 1. Load homepage. 2. Observe hero banner images |
| **Expected Result** | All hero banner images render correctly; no broken image icons |
| **Actual Result** | Hero banners displayed correctly; no broken images observed |
| **Status** | PASS |
| **Priority** | Medium |

---

### TC-003 — Category navigation menu displays all main categories

| Field | Detail |
|-------|--------|
| **Scenario** | Homepage Load |
| **Preconditions** | Homepage is loaded |
| **Steps** | 1. Load homepage. 2. Observe the horizontal category nav bar |
| **Expected Result** | All expected categories visible: Official Stores, Phones & Tablets, TVs & Audio, Appliances, Health & Beauty, Home & Office, Fashion, Computing, Gaming, Supermarket, Baby Products |
| **Actual Result** | All 10+ main categories visible in nav bar |
| **Status** | PASS |
| **Priority** | High |

---

### TC-004 — Flash Sale countdown timer is displayed and counts down

| Field | Detail |
|-------|--------|
| **Scenario** | Homepage Load |
| **Preconditions** | Homepage is loaded; a Flash Sale is currently running |
| **Steps** | 1. Load homepage. 2. Locate the Flash Sales section. 3. Note the countdown timer value. 4. Wait 10 seconds and observe |
| **Expected Result** | A countdown timer is visible and decrements every second |
| **Actual Result** | Flash Sale section visible with live countdown timer (hh:mm:ss); timer decrements in real time |
| **Status** | PASS |
| **Priority** | Medium |

---

### TC-005 — Search returns relevant results for a valid keyword

| Field | Detail |
|-------|--------|
| **Scenario** | Search Functionality |
| **Preconditions** | User is on the homepage |
| **Steps** | 1. Click the search bar. 2. Type 'Samsung Galaxy A16'. 3. Press Enter or click the search icon |
| **Expected Result** | Search results page loads showing products matching or related to 'Samsung Galaxy A16' |
| **Actual Result** | Results page loaded; Samsung Galaxy A16 listings displayed with product names, prices and images |
| **Status** | PASS |
| **Priority** | High |

---

### TC-006 — Search with an empty query does not break the page

| Field | Detail |
|-------|--------|
| **Scenario** | Search Functionality |
| **Preconditions** | User is on the homepage |
| **Steps** | 1. Click the search bar. 2. Leave it empty. 3. Press Enter or click the search icon |
| **Expected Result** | Either the page stays on homepage or a helpful message is shown; no error page |
| **Actual Result** | Clicking search with empty field reloads the homepage without showing an error page |
| **Status** | PASS |
| **Priority** | Medium |

---

### TC-007 — Search with a non-existent product shows a no results message

| Field | Detail |
|-------|--------|
| **Scenario** | Search Functionality |
| **Preconditions** | User is on the homepage |
| **Steps** | 1. Click the search bar. 2. Type 'xyznonexistentproduct123'. 3. Press Enter |
| **Expected Result** | A 'no results found' message or similar empty-state UI is displayed |
| **Actual Result** | Page shows 'No results found' message with suggestions to try different keywords |
| **Status** | PASS |
| **Priority** | Medium |

---

### TC-008 — Search autocomplete suggestions appear while typing

| Field | Detail |
|-------|--------|
| **Scenario** | Search Functionality |
| **Preconditions** | User is on the homepage |
| **Steps** | 1. Click the search bar. 2. Start typing 'iphone' |
| **Expected Result** | A dropdown of autocomplete suggestions appears as the user types |
| **Actual Result** | Autocomplete dropdown appeared showing relevant suggestions |
| **Status** | PASS |
| **Priority** | Low |

---

### TC-009 — Search results can be filtered by category

| Field | Detail |
|-------|--------|
| **Scenario** | Search Functionality |
| **Preconditions** | User has performed a search for 'laptop' |
| **Steps** | 1. Search for 'laptop'. 2. On the results page, click a category filter (e.g. 'Computing') |
| **Expected Result** | Results are filtered to show only items in the selected category |
| **Actual Result** | Category filter applied; results narrowed to Computing laptops only |
| **Status** | PASS |
| **Priority** | High |

---

### TC-010 — Search results can be sorted by price low to high

| Field | Detail |
|-------|--------|
| **Scenario** | Search Functionality |
| **Preconditions** | User has performed a search for 'headphones' |
| **Steps** | 1. Search for 'headphones'. 2. Locate the sort dropdown. 3. Select 'Price: Low to High' |
| **Expected Result** | Products are reordered so the lowest-priced item appears first |
| **Actual Result** | Products reordered with lowest price first; verified first and last items |
| **Status** | PASS |
| **Priority** | Medium |

---

> **Note:** TC-011 through TC-050 follow the same format. Full details are available in the Excel file:  
> [`Test Cases/Jumia_Exploratory_Test_Cases.xlsx`](./Jumia_Exploratory_Test_Cases.xlsx)