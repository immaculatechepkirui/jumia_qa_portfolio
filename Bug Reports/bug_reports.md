# Jumia Kenya — Bug Reports

**Website:** https://www.jumia.co.ke/  
**Tester:** Immaculata Chepkirui  
**Date:** July 2025  
**Total Bugs Found:** 5  

---

## Bug Summary

| Bug ID | Area | Title | Severity | Status |
|--------|------|-------|----------|--------|
| BUG-001 | Search | Autocomplete dropdown does not close when clicking outside | Low | Open |
| BUG-002 | Filters | Applying multiple filters resets scroll position to top | Medium | Open |
| BUG-003 | Cart | Quantity input accepts 0 and negative values | High | Open |
| BUG-004 | Mobile | Category nav overlaps search bar at 375px viewport | Medium | Open |
| BUG-005 | Performance | Homepage LCP exceeds 4s on simulated 4G connection | Medium | Open |

---

## Severity Legend

| Severity | Meaning |
|----------|---------|
| **Critical** | Feature is completely broken; blocks core user journey |
| **High** | Major functionality is impaired; no workaround available |
| **Medium** | Functionality works but with a noticeable defect or poor UX |
| **Low** | Minor issue; cosmetic or edge case; does not affect core flow |

---

## Detailed Bug Reports

---

### BUG-001 — Autocomplete dropdown does not close when clicking outside

| Field | Detail |
|-------|--------|
| **Bug ID** | BUG-001 |
| **Area** | Search Functionality |
| **Severity** | Low |
| **Status** | Open |
| **Related Test Case** | TC-008 |
| **Environment** | Chrome 126, Desktop, Ubuntu Linux |
| **URL** | https://www.jumia.co.ke/ |

**Steps to Reproduce**
1. Load the Jumia Kenya homepage.
2. Click the search bar.
3. Type any keyword (e.g. `iphone`).
4. Observe the autocomplete dropdown appears.
5. Click anywhere outside the search bar and dropdown (e.g. on the hero banner).

**Expected Result**  
The autocomplete dropdown closes when the user clicks outside of it.

**Actual Result**  
The autocomplete dropdown remains visible after clicking outside. It only closes when the user presses `Escape` or clicks directly inside the search bar again.

**Impact**  
Low — the dropdown does not block page content but creates a confusing UX, particularly on smaller screens where it may obscure product listings.

**Screenshot**  
`Screenshots/BUG-001-autocomplete-stays-open.png`

---

### BUG-002 — Applying multiple filters simultaneously resets scroll position to top

| Field | Detail |
|-------|--------|
| **Bug ID** | BUG-002 |
| **Area** | Product Listing & Filters |
| **Severity** | Medium |
| **Status** | Open |
| **Related Test Case** | TC-034 |
| **Environment** | Chrome 126, Desktop, Ubuntu Linux |
| **URL** | https://www.jumia.co.ke/phones-tablets/ |

**Steps to Reproduce**
1. Navigate to the Phones & Tablets category page.
2. Scroll down to the filter panel.
3. Apply a brand filter (e.g. Samsung).
4. Wait for results to reload.
5. Apply a price range filter (e.g. KSh 10,000–30,000) without scrolling back to top.

**Expected Result**  
Filters apply without disrupting the user's current scroll position, or the page scrolls smoothly to the top of the results.

**Actual Result**  
The page triggers a full reload and snaps abruptly to the very top of the page (including the header), forcing the user to scroll back down to the filter panel to continue refining results.

**Impact**  
Medium — noticeably degrades UX when a user wants to apply more than one filter in sequence, which is a common e-commerce behaviour.

**Screenshot**  
`Screenshots/BUG-002-filter-scroll-reset.png`

---

### BUG-003 — Cart quantity input accepts 0 and negative values without validation

| Field | Detail |
|-------|--------|
| **Bug ID** | BUG-003 |
| **Area** | Shopping Cart |
| **Severity** | High |
| **Status** | Open |
| **Related Test Case** | TC-018 |
| **Environment** | Chrome 126, Desktop, Ubuntu Linux |
| **URL** | https://www.jumia.co.ke/cart/ |

**Steps to Reproduce**
1. Add any product to the cart.
2. Open the cart page.
3. Click the quantity input field for the item.
4. Manually clear the value and type `0`.
5. Click outside the field or press Tab.
6. Repeat with `-1`.

**Expected Result**  
The input should reject values below 1. Either the field resets to 1 automatically, or an inline validation error is displayed (e.g. "Quantity must be at least 1").

**Actual Result**  
The cart accepts `0` as a quantity. The subtotal updates to KSh 0.00, making it appear the item is free. Entering `-1` causes the subtotal to display a negative price. No validation error is shown in either case.

**Impact**  
High — a user could potentially attempt to checkout with a 0 or negative quantity. Even if the backend prevents order completion, displaying KSh 0.00 or negative prices is misleading and undermines trust in the platform.

**Screenshot**  
`Screenshots/BUG-003-cart-zero-quantity.png`

---

### BUG-004 — Category navigation overlaps search bar at 375px mobile viewport

| Field | Detail |
|-------|--------|
| **Bug ID** | BUG-004 |
| **Area** | Responsive Design |
| **Severity** | Medium |
| **Status** | Open |
| **Related Test Case** | TC-041 |
| **Environment** | Chrome 126 DevTools, 375px viewport (iPhone SE simulation) |
| **URL** | https://www.jumia.co.ke/ |

**Steps to Reproduce**
1. Open Chrome DevTools (`F12`).
2. Toggle device toolbar and set viewport width to 375px.
3. Load https://www.jumia.co.ke/.
4. Observe the top navigation area.

**Expected Result**  
The search bar and category navigation are clearly separated with no overlapping elements. All interactive elements are fully tappable.

**Actual Result**  
The category navigation bar partially overlaps the bottom edge of the search bar at 375px. The first category item ("Official Stores") is partially obscured and difficult to tap accurately.

**Impact**  
Medium — affects usability on the most common small-screen mobile size. Mobile users make up a significant portion of Jumia's traffic in Kenya.

**Screenshot**  
`Screenshots/BUG-004-mobile-nav-overlap.png`

---

### BUG-005 — Homepage Largest Contentful Paint exceeds 4s on simulated 4G

| Field | Detail |
|-------|--------|
| **Bug ID** | BUG-005 |
| **Area** | Performance |
| **Severity** | Medium |
| **Status** | Open |
| **Related Test Case** | TC-001 |
| **Environment** | Chrome 126 Lighthouse Audit, Simulated Fast 4G, Desktop |
| **URL** | https://www.jumia.co.ke/ |

**Steps to Reproduce**
1. Open Chrome DevTools (`F12`).
2. Navigate to the Lighthouse tab.
3. Select "Mobile" and run a Performance audit.
4. Review the LCP (Largest Contentful Paint) metric.

**Expected Result**  
LCP should be under 2.5 seconds (Google's "Good" threshold) to ensure a fast perceived load experience for users on typical Kenyan mobile network speeds.

**Actual Result**  
LCP recorded at approximately 4.2 seconds, falling in Google's "Poor" category. The main contributor is the hero banner image, which is large and not lazy-loaded. Several render-blocking scripts from third-party ad and analytics providers also delay paint.

**Impact**  
Medium — slow LCP directly affects user retention. Research consistently shows that pages taking over 3 seconds to load see significantly higher bounce rates. This is especially relevant in markets where mobile data speeds are variable.

**Suggested Fix**  
- Compress and convert hero banner images to WebP format.
- Add `loading="lazy"` to below-the-fold images.
- Defer non-critical third-party scripts.

**Screenshot**  
`Screenshots/BUG-005-lighthouse-lcp.png`

---

## Notes

- Screenshots referenced above should be captured during live testing and saved in the `Screenshots/` folder.
- All bugs were discovered during manual exploratory testing in July 2025.
- Severity ratings follow standard QA classification (Critical / High / Medium / Low).