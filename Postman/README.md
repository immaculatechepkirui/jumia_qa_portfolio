# Jumia Kenya — Postman API Tests

**Collection:** `Jumia_API_Tests.json`  
**Tool:** Postman  
**Tester:** Immaculata Chepkirui  
**Date:** July 2026  
**Endpoints tested:** 11 requests across 3 folders  

---

## How to Import and Run

1. Open Postman
2. Click **Import**
3. Select `Jumia_API_Tests.json`
4. Click **Run collection** → **Run manually**

---

## Collection Structure

### Search (4 requests)
| Request | Method | Endpoint | Purpose |
|---------|--------|----------|---------|
| Valid keyword | GET | /catalog/?q=samsung | TC-005: Confirms search returns results |
| Empty keyword | GET | /catalog/?q= | TC-006: Confirms no 500 error on empty search |
| Non-existent product | GET | /catalog/?q=xyznonexistent... | TC-007: Confirms no-results message returned |
| Price filter | GET | /catalog/?q=phone&price=10000-30000 | TC-031: Confirms filtered results load |

### Product Pages (3 requests)
| Request | Method | Endpoint | Purpose |
|---------|--------|----------|---------|
| Product detail | GET | /samsung-galaxy-a16-...html | TC-011: Confirms product page loads with price |
| Category page | GET | /phones-tablets/ | TC-027: Confirms category listing loads |
| Flash Sales | GET | /flash-sales/ | TC-039: Confirms Flash Sales page loads |

### Navigation & Error Handling (4 requests)
| Request | Method | Endpoint | Purpose |
|---------|--------|----------|---------|
| Homepage | GET | / | TC-001: Confirms 200 and Jumia branding |
| 404 page | GET | /this-page-does-not-exist-xyz | TC-047: Confirms 404 not 500 |
| Help Center | GET | /sp-help/ | TC-043: Confirms Help Center loads |
| Cart (unauth) | GET | /cart/ | TC-017: Confirms cart page loads without error |

---

## Key Findings

| Finding | Detail |
|---------|--------|
| Search response time | First search request returned in 17,349ms — significantly above the 5,000ms threshold. Indicates slow server-side rendering under load. Related to BUG-005 (performance). |
| Add to Cart button | Not present in raw HTML response — rendered by JavaScript after page load. This is expected behaviour for SPAs but means the button cannot be validated via HTTP-level API testing alone. Validated via Playwright instead (test_cart.py). |
| 404 handling | Non-existent URLs return 404 correctly — no 500 server errors observed. |
| Empty search | Returns 200 without crashing — graceful handling confirmed. |

---

## Notes

- All tests use a `{{base_url}}` variable set to `https://www.jumia.co.ke`
- Jumia does not expose a public REST API — these tests validate HTTP-level behaviour of the web application endpoints
- JavaScript-rendered content (cart button, autocomplete) cannot be tested at this level — use the Playwright suite for those