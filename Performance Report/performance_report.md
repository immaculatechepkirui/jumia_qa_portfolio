# Jumia Kenya — Performance Report

**Tool:** Google Lighthouse 13.3.0  
**Date:** July 14, 2026  
**Tester:** Immaculata Chepkirui  
**Device emulated:** Moto G Power  
**Network throttling:** Slow 4G  
**Mode:** Initial page load, single page session  

---

## Audit Scores

| Category | Score | Rating |
|----------|-------|--------|
| Performance | 31/100 | 🔴 Poor |
| Accessibility | 92/100 | 🟢 Good |
| Best Practices | 58/100 | 🔴 Poor |
| SEO | 92/100 | 🟢 Good |

---

## Core Web Vitals

| Metric | Value | Threshold (Good) | Rating |
|--------|-------|-----------------|--------|
| First Contentful Paint (FCP) | 2.8s | < 1.8s | 🔴 Poor |
| Largest Contentful Paint (LCP) | 7.7s | < 2.5s | 🔴 Poor |
| Total Blocking Time (TBT) | 9,230ms | < 200ms | 🔴 Poor |
| Cumulative Layout Shift (CLS) | 0.005 | < 0.1 | 🟢 Good |
| Speed Index (SI) | 23.2s | < 3.4s | 🔴 Poor |

> **Note:** Chrome extensions and stored IndexedDB data may have negatively affected
> these scores. Results should be re-run in a clean incognito window for a more
> accurate baseline. These scores should therefore be treated as a worst-case
> indication rather than a definitive benchmark.

---

## Key Issues Found

### 1. Performance (31/100) — Critical

The page is severely underperforming on mobile, particularly under slower network
conditions typical of Kenyan mobile users.

**Root causes identified by Lighthouse:**

| Issue | Estimated Saving |
|-------|-----------------|
| Improve image delivery | 2,624 KiB |
| Reduce unused JavaScript | 2,621 KiB |
| Avoid enormous network payloads (total: 4,666 KiB) | — |
| Minify JavaScript | 681 KiB |
| Use efficient cache lifetimes | 1,212 KiB |
| Render-blocking requests | 370 ms |
| Document request latency | 690 ms |
| Legacy JavaScript | 41 KiB |

**Additional diagnostics:**

- JavaScript execution time: **15.6 seconds**
- Main-thread work: **38.0 seconds**
- Long main-thread tasks: **20 found**

**Recommendations:**
- Convert and compress hero banner images to WebP format.
- Implement lazy loading (`loading="lazy"`) for all below-the-fold images.
- Defer or async-load non-critical third-party scripts (ads, analytics).
- Enable JavaScript minification and tree-shaking in the build pipeline.
- Implement a CDN caching strategy for static assets.

---

### 2. Best Practices (58/100) — Poor

**Issues identified:**

| Issue | Detail |
|-------|--------|
| Deprecated APIs | 1 warning found |
| Third-party cookies | 148 cookies detected |
| No effective CSP | Site is not protected against XSS via Content Security Policy |
| No strong HSTS policy | HTTP Strict Transport Security not enforced |
| No COOP header | Origin isolation not enforced via Cross-Origin Opener Policy |
| No Trusted Types | DOM-based XSS mitigation not implemented |

**Recommendations:**
- Audit and remove deprecated API usage.
- Review third-party cookie usage for GDPR/data privacy compliance.
- Implement a Content Security Policy header.
- Enforce HSTS with a minimum 1-year max-age directive.

---

### 3. Accessibility (92/100) — Good

Accessibility is the strongest category. Minor issues found:

| Issue | Detail |
|-------|--------|
| Colour contrast | Some foreground/background colour combinations fail WCAG AA ratio |
| Touch target size | Some interactive elements are too small or too close together for mobile |
| Redundant image alt text | Some images have alt text that duplicates visible text nearby |
| Identical links | Multiple links with the same label point to different destinations |

**Recommendations:**
- Review and fix colour contrast on promotional banners and secondary text.
- Increase touch target sizes to a minimum of 44x44px as per WCAG 2.5.5.
- Audit alt text on product images to ensure it is descriptive and unique.

---

### 4. SEO (92/100) — Good

SEO is well-implemented overall. One issue found:

| Issue | Detail |
|-------|--------|
| robots.txt not valid | Lighthouse was unable to download the robots.txt file during the audit |

**Recommendations:**
- Verify that robots.txt is publicly accessible and correctly formatted.
- Note: Core Web Vitals (Performance scores above) directly impact Google Search
  ranking — the poor Performance score is therefore also an SEO concern beyond
  the 92/100 Lighthouse SEO score.

---

## Summary & Priority Recommendations

| Priority | Recommendation | Expected Impact |
|----------|---------------|----------------|
| 🔴 High | Compress and convert images to WebP | Largest single saving: 2,624 KiB |
| 🔴 High | Remove or defer unused JavaScript | 2,621 KiB saving; reduces TBT significantly |
| 🔴 High | Re-run audit in incognito for clean baseline | Removes extension/cache interference |
| 🟡 Medium | Implement CSP and HSTS headers | Improves security posture and Best Practices score |
| 🟡 Medium | Fix colour contrast issues | Improves Accessibility for low-vision users |
| 🟢 Low | Fix robots.txt availability | Ensures crawlers can access directives reliably |

---

## Observations on Market Context

Jumia Kenya's primary user base accesses the platform predominantly via mobile devices
on variable 3G/4G connections. The 7.7s LCP and 23.2s Speed Index recorded under
Slow 4G throttling are therefore directly relevant to a large portion of real users —
not just an edge case. Performance optimisation should be treated as a business-critical
priority, not merely a technical concern.