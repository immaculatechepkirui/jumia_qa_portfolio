What else can I do apart from explatory test for Jumia to make this a projecxt worth putting in my QA CV?


Synthesized practical strategies to elevate QA portfolio beyond exploratory testing
Synthesized practical strategies to elevate QA portfolio beyond exploratory testing
Great instinct to think beyond the exercise — exploratory testing alone is entry-level. Here's what would genuinely impress a QA hiring manager:

1. Write a formal Test Plan document
A one-page doc covering scope, objectives, test environment, entry/exit criteria, and risk areas. It shows you understand QA process, not just execution. This is what senior QAs write before any testing begins.

2. Build a bug report log
During your Jumia testing, you almost certainly noticed real issues (broken filters, UI glitches, slow load times, inconsistent pricing display). Document them properly: Bug ID, severity, steps to reproduce, expected vs actual, screenshots. Even 5 well-written bug reports demonstrate more skill than 50 shallow test cases.

3. Write automated tests with Playwright or Selenium
Pick 3–5 of your highest-priority test cases (login, search, add to cart) and automate them in Python with Playwright. This is the single biggest CV differentiator — "I tested Jumia manually and wrote automation for critical flows" immediately puts you in a different tier.

4. Do API testing with Postman
Jumia has underlying APIs driving its search, cart and product pages. Use browser devtools (Network tab) to capture the API calls, then replay and test them in Postman — test edge cases, invalid inputs, response times. Export your Postman collection as a JSON file to include in your project repo.

5. Write a Performance/UX observation report
Note page load times, image optimisation issues, Core Web Vitals (use Lighthouse in Chrome devtools). A short written summary showing you think about user experience quality, not just functional correctness, shows QA maturity.

6. Package it all on GitHub
Put everything in a repo: your test plan, bug report log, Playwright scripts, Postman collection, and a clean README.md explaining your approach. A link to a GitHub repo on your CV is concrete evidence — not just a claim.

The realistic minimum for a strong CV entry would be items 2 + 3 + 6 — a bug report, some automation, and a GitHub repo. That combination shows you can find issues and prevent regressions, which is exactly what employers hire junior QAs to do.

Want me to help you set up the Playwright project structure or write the test plan template?

How is this approach?   Instead of linking directly to the Excel file, create a GitHub repository called something like:

jumia-qa-testing

Include:

README.md
Test Plan.pdf
Exploratory Test Cases.xlsx
Bug Reports/
Playwright/
Postman/
Performance Report.pdf
Screenshots/

Then, in your portfolio:

GitHub → points to the repository (shows your overall QA process and version control).
Test Cases → links directly to the Excel file in your portfolio or repository.

This approach demonstrates not only testing skills but also organization, documentation, and software engineering practices—qualities that recruiters for QA and SDET roles value highly.

Show more

Validated repository structure for demonstrating comprehensive QA expertise
Validated repository structure for demonstrating comprehensive QA expertise
Solid plan — the structure is clean and professional. A few honest thoughts on it:

What's strong about it

The folder structure mirrors how real QA teams organise work. Anyone reviewing your repo immediately sees you understand the full QA lifecycle, not just test case writing.
Separating Bug Reports, Playwright, Postman and Performance into their own folders makes each deliverable independently linkable — useful if a recruiter only cares about your automation skills, for example.
Having both a GitHub link and a direct Excel link in your portfolio is smart. Not every recruiter clicks through to GitHub.
One thing to reconsider
PDFs for the Test Plan and Performance Report are fine for sharing, but consider keeping the source (a .md file or a Word doc) in the repo too. PDFs aren't version-controllable in a meaningful way — if a recruiter is technically sharp, they notice when a repo contains only binary files.

What will make or break the repo
The README is actually the most important file. A weak README makes the whole thing look like a homework dump. A strong one should cover: what Jumia is (one line), the scope of your testing, the tools you used, how to run the Playwright tests locally, and what bugs you found. That README is often the only thing a busy recruiter reads.

Suggested repo name tweak
jumia-qa-portfolio reads slightly better than jumia-qa-testing — "portfolio" signals intentionality, whereas "testing" sounds like an assignment. Small thing but worth considering.

Realistic sequencing
Don't try to build everything at once. A suggested order:

Set up the repo and push the Excel file first (done)
Write the README
Add bug reports
Add Playwright scripts
Add Postman collection
Write the Test Plan and Performance Report last, since they synthesise everything else
Want me to help you draft the README or set up the Playwright project?

immah@immah-HP-EliteBook-845-G8-Notebook-PC:~$ git clone git@github.com:immaculatechepkirui/jumia_qa_portfolio.git
Cloning into 'jumia_qa_portfolio'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.
immah@immah-HP-EliteBook-845-G8-Notebook-PC:~$ cd jumia_qa_portfolio
immah@immah-HP-EliteBook-845-G8-Notebook-PC:~/jumia_qa_portfolio$ ls
README.md
immah@immah-HP-EliteBook-845-G8-Notebook-PC:~/jumia_qa_portfolio$ 
  Lets work on adding the excel sheet but I think the .md version is better then after that we write the readme, give me the commands, the content but do not get into my repo or terminal and do it. I prefer when I get the commands and content of files or directories from you because i will learn and understand.

Show more
Perfect workflow. Let's do this step by step.

Step 1 — Create the folder structure

Run these commands inside your jumia_qa_portfolio directory:

bash
mkdir -p "Bug Reports" "Playwright/tests" "Playwright/screenshots" "Postman" "Performance Report" "Screenshots" "Test Plan"
Then verify it looks right:

bash
ls
Step 2 — Copy your Excel file into the repo

Assuming your Excel file is in your Downloads folder:

bash
cp ~/Downloads/Jumia_Exploratory_Test_Cases.xlsx "Test Cases/Jumia_Exploratory_Test_Cases.xlsx"
Wait — first create the Test Cases folder:

bash
mkdir "Test Cases"
cp ~/Downloads/Jumia_Exploratory_Test_Cases.xlsx "Test Cases/Jumia_Exploratory_Test_Cases.xlsx"
Step 3 — Create the Markdown version of the test cases

Create the file:

bash
touch "Test Cases/exploratory_test_cases.md"
Then open it in VS Code:

bash
code "Test Cases/exploratory_test_cases.md"
Paste this content:

markdown
# Jumia Kenya — Exploratory Test Cases

**Website:** https://www.jumia.co.ke/  
**Tester:** Immaculata Chepkirui  
**Date:** July 2025  
**Total Test Cases:** 50  
**Tool:** Manual / Browser  

---

## Test Case Summary

|
 Test ID 
|
 Scenario 
|
 Status 
|
 Priority 
|
|
---------
|
----------
|
--------
|
----------
|
|
 TC-001 
|
 Homepage loads successfully 
|
 PASS 
|
 High 
|
|
 TC-002 
|
 Hero banner images render without broken links 
|
 PASS 
|
 Medium 
|
|
 TC-003 
|
 Category navigation menu displays all main categories 
|
 PASS 
|
 High 
|
|
 TC-004 
|
 Flash Sale countdown timer is displayed and counts down 
|
 PASS 
|
 Medium 
|
|
 TC-005 
|
 Search returns relevant results for a valid keyword 
|
 PASS 
|
 High 
|
|
 TC-006 
|
 Search with an empty query does not break the page 
|
 PASS 
|
 Medium 
|
|
 TC-007 
|
 Search with a non-existent product shows a no results message 
|
 PASS 
|
 Medium 
|
|
 TC-008 
|
 Search autocomplete suggestions appear while typing 
|
 PASS 
|
 Low 
|
|
 TC-009 
|
 Search results can be filtered by category 
|
 PASS 
|
 High 
|
|
 TC-010 
|
 Search results can be sorted by price low to high 
|
 PASS 
|
 Medium 
|
|
 TC-011 
|
 Product detail page shows complete product information 
|
 PASS 
|
 High 
|
|
 TC-012 
|
 Product image gallery allows switching between images 
|
 PASS 
|
 Medium 
|
|
 TC-013 
|
 Discounted product shows both original and discounted price 
|
 PASS 
|
 Medium 
|
|
 TC-014 
|
 Add to Wishlist button is visible on product page 
|
 PASS 
|
 Low 
|
|
 TC-015 
|
 Product seller name and rating are displayed 
|
 PASS 
|
 Low 
|
|
 TC-016 
|
 Adding a product to the cart works correctly 
|
 PASS 
|
 High 
|
|
 TC-017 
|
 Cart page displays added items correctly 
|
 PASS 
|
 High 
|
|
 TC-018 
|
 Quantity of an item in the cart can be increased 
|
 PASS 
|
 High 
|
|
 TC-019 
|
 Item can be removed from the cart 
|
 PASS 
|
 High 
|
|
 TC-020 
|
 Cart persists items after page refresh 
|
 PASS 
|
 Medium 
|
|
 TC-021 
|
 New user can register with valid details 
|
 PASS 
|
 High 
|
|
 TC-022 
|
 Registration fails when a duplicate email is used 
|
 PASS 
|
 High 
|
|
 TC-023 
|
 Registered user can log in with correct credentials 
|
 PASS 
|
 High 
|
|
 TC-024 
|
 Login fails with incorrect password 
|
 PASS 
|
 High 
|
|
 TC-025 
|
 Login form validates empty fields 
|
 PASS 
|
 Medium 
|
|
 TC-026 
|
 Forgot Password link navigates to password reset page 
|
 PASS 
|
 Medium 
|
|
 TC-027 
|
 Clicking a top-level category navigates to correct listing page 
|
 PASS 
|
 High 
|
|
 TC-028 
|
 Jumia logo returns user to homepage 
|
 PASS 
|
 Medium 
|
|
 TC-029 
|
 Footer links are functional — Help Center 
|
 PASS 
|
 Low 
|
|
 TC-030 
|
 Breadcrumb navigation works on a category page 
|
 PASS 
|
 Low 
|
|
 TC-031 
|
 Price range filter narrows down results correctly 
|
 PASS 
|
 High 
|
|
 TC-032 
|
 Brand filter returns only products from selected brand 
|
 PASS 
|
 Medium 
|
|
 TC-033 
|
 Pagination navigates to correct next page of results 
|
 PASS 
|
 Medium 
|
|
 TC-034 
|
 Multiple filters can be applied simultaneously 
|
 PASS 
|
 Medium 
|
|
 TC-035 
|
 Checkout page requires login for unauthenticated users 
|
 PASS 
|
 High 
|
|
 TC-036 
|
 Checkout shows correct order summary including item prices 
|
 PASS 
|
 High 
|
|
 TC-037 
|
 Pay on Delivery option is available as a payment method 
|
 PASS 
|
 High 
|
|
 TC-038 
|
 Delivery address can be added during checkout 
|
 PASS 
|
 High 
|
|
 TC-039 
|
 Flash Sales page loads and displays current sale items 
|
 PASS 
|
 Medium 
|
|
 TC-040 
|
 Out-of-stock flash sale items are clearly marked 
|
 PASS 
|
 Medium 
|
|
 TC-041 
|
 Homepage displays correctly at mobile viewport 375px 
|
 PASS 
|
 High 
|
|
 TC-042 
|
 Product listing page adapts to tablet viewport 768px 
|
 PASS 
|
 Medium 
|
|
 TC-043 
|
 Help Center page loads and displays FAQ categories 
|
 PASS 
|
 Low 
|
|
 TC-044 
|
 WhatsApp chat link opens correctly 
|
 PASS 
|
 Low 
|
|
 TC-045 
|
 Logged-in user can add a product to the wishlist 
|
 PASS 
|
 Medium 
|
|
 TC-046 
|
 Wishlist page shows all saved products 
|
 PASS 
|
 Medium 
|
|
 TC-047 
|
 404 page displays correctly for a non-existent URL 
|
 PASS 
|
 Medium 
|
|
 TC-048 
|
 Page load completes without JS console errors on homepage 
|
 PASS 
|
 Low 
|
|
 TC-049 
|
 Newsletter subscription with valid email works 
|
 PASS 
|
 Low 
|
|
 TC-050 
|
 Newsletter subscription fails without accepting terms 
|
 PASS 
|
 Low 
|

---

## Detailed Test Cases

### TC-001 — Homepage loads successfully

|
 Field 
|
 Detail 
|
|
-------
|
--------
|
|
**
Scenario
**
|
 Homepage Load 
|
|
**
Preconditions
**
|
 User has internet access; browser is open 
|
|
**
Steps
**
|
1.
 Open https://www.jumia.co.ke/ in a browser 
|
|
**
Expected Result
**
|
 Page loads within a reasonable time; Jumia logo, navigation bar, category menu, hero banner and product sections are all visible 
|
|
**
Actual Result
**
|
 Page loaded successfully. Logo, top nav, category menu, hero banner and promotional sections all displayed correctly 
|
|
**
Status
**
|
 PASS 
|
|
**
Priority
**
|
 High 
|

---

### TC-002 — Hero banner images render without broken links

|
 Field 
|
 Detail 
|
|
-------
|
--------
|
|
**
Scenario
**
|
 Homepage Load 
|
|
**
Preconditions
**
|
 Homepage is loaded 
|
|
**
Steps
**
|
1.
 Load homepage. 2. Observe hero banner images 
|
|
**
Expected Result
**
|
 All hero banner images render correctly; no broken image icons 
|
|
**
Actual Result
**
|
 Hero banners displayed correctly; no broken images observed 
|
|
**
Status
**
|
 PASS 
|
|
**
Priority
**
|
 Medium 
|

---

### TC-003 — Category navigation menu displays all main categories

|
 Field 
|
 Detail 
|
|
-------
|
--------
|
|
**
Scenario
**
|
 Homepage Load 
|
|
**
Preconditions
**
|
 Homepage is loaded 
|
|
**
Steps
**
|
1.
 Load homepage. 2. Observe the horizontal category nav bar 
|
|
**
Expected Result
**
|
 All expected categories visible: Official Stores, Phones & Tablets, TVs & Audio, Appliances, Health & Beauty, Home & Office, Fashion, Computing, Gaming, Supermarket, Baby Products 
|
|
**
Actual Result
**
|
 All 10+ main categories visible in nav bar 
|
|
**
Status
**
|
 PASS 
|
|
**
Priority
**
|
 High 
|

---

### TC-004 — Flash Sale countdown timer is displayed and counts down

|
 Field 
|
 Detail 
|
|
-------
|
--------
|
|
**
Scenario
**
|
 Homepage Load 
|
|
**
Preconditions
**
|
 Homepage is loaded; a Flash Sale is currently running 
|
|
**
Steps
**
|
1.
 Load homepage. 2. Locate the Flash Sales section. 3. Note the countdown timer value. 4. Wait 10 seconds and observe 
|
|
**
Expected Result
**
|
 A countdown timer is visible and decrements every second 
|
|
**
Actual Result
**
|
 Flash Sale section visible with live countdown timer (hh:mm:ss); timer decrements in real time 
|
|
**
Status
**
|
 PASS 
|
|
**
Priority
**
|
 Medium 
|

---

### TC-005 — Search returns relevant results for a valid keyword

|
 Field 
|
 Detail 
|
|
-------
|
--------
|
|
**
Scenario
**
|
 Search Functionality 
|
|
**
Preconditions
**
|
 User is on the homepage 
|
|
**
Steps
**
|
1.
 Click the search bar. 2. Type 'Samsung Galaxy A16'. 3. Press Enter or click the search icon 
|
|
**
Expected Result
**
|
 Search results page loads showing products matching or related to 'Samsung Galaxy A16' 
|
|
**
Actual Result
**
|
 Results page loaded; Samsung Galaxy A16 listings displayed with product names, prices and images 
|
|
**
Status
**
|
 PASS 
|
|
**
Priority
**
|
 High 
|

---

### TC-006 — Search with an empty query does not break the page

|
 Field 
|
 Detail 
|
|
-------
|
--------
|
|
**
Scenario
**
|
 Search Functionality 
|
|
**
Preconditions
**
|
 User is on the homepage 
|
|
**
Steps
**
|
1.
 Click the search bar. 2. Leave it empty. 3. Press Enter or click the search icon 
|
|
**
Expected Result
**
|
 Either the page stays on homepage or a helpful message is shown; no error page 
|
|
**
Actual Result
**
|
 Clicking search with empty field reloads the homepage without showing an error page 
|
|
**
Status
**
|
 PASS 
|
|
**
Priority
**
|
 Medium 
|

---

### TC-007 — Search with a non-existent product shows a no results message

|
 Field 
|
 Detail 
|
|
-------
|
--------
|
|
**
Scenario
**
|
 Search Functionality 
|
|
**
Preconditions
**
|
 User is on the homepage 
|
|
**
Steps
**
|
1.
 Click the search bar. 2. Type 'xyznonexistentproduct123'. 3. Press Enter 
|
|
**
Expected Result
**
|
 A 'no results found' message or similar empty-state UI is displayed 
|
|
**
Actual Result
**
|
 Page shows 'No results found' message with suggestions to try different keywords 
|
|
**
Status
**
|
 PASS 
|
|
**
Priority
**
|
 Medium 
|

---

### TC-008 — Search autocomplete suggestions appear while typing

|
 Field 
|
 Detail 
|
|
-------
|
--------
|
|
**
Scenario
**
|
 Search Functionality 
|
|
**
Preconditions
**
|
 User is on the homepage 
|
|
**
Steps
**
|
1.
 Click the search bar. 2. Start typing 'iphone' 
|
|
**
Expected Result
**
|
 A dropdown of autocomplete suggestions appears as the user types 
|
|
**
Actual Result
**
|
 Autocomplete dropdown appeared showing relevant suggestions 
|
|
**
Status
**
|
 PASS 
|
|
**
Priority
**
|
 Low 
|

---

### TC-009 — Search results can be filtered by category

|
 Field 
|
 Detail 
|
|
-------
|
--------
|
|
**
Scenario
**
|
 Search Functionality 
|
|
**
Preconditions
**
|
 User has performed a search for 'laptop' 
|
|
**
Steps
**
|
1.
 Search for 'laptop'. 2. On the results page, click a category filter (e.g. 'Computing') 
|
|
**
Expected Result
**
|
 Results are filtered to show only items in the selected category 
|
|
**
Actual Result
**
|
 Category filter applied; results narrowed to Computing laptops only 
|
|
**
Status
**
|
 PASS 
|
|
**
Priority
**
|
 High 
|

---

### TC-010 — Search results can be sorted by price low to high

|
 Field 
|
 Detail 
|
|
-------
|
--------
|
|
**
Scenario
**
|
 Search Functionality 
|
|
**
Preconditions
**
|
 User has performed a search for 'headphones' 
|
|
**
Steps
**
|
1.
 Search for 'headphones'. 2. Locate the sort dropdown. 3. Select 'Price: Low to High' 
|
|
**
Expected Result
**
|
 Products are reordered so the lowest-priced item appears first 
|
|
**
Actual Result
**
|
 Products reordered with lowest price first; verified first and last items 
|
|
**
Status
**
|
 PASS 
|
|
**
Priority
**
|
 Medium 
|

---

> **Note:** TC-011 through TC-050 follow the same format. Full details are available in the Excel file:  
> [`Test Cases/Jumia_Exploratory_Test_Cases.xlsx`](./Jumia_Exploratory_Test_Cases.xlsx)
Save the file in VS Code with Ctrl+S.

Step 4 — Commit and push everything

bash
git add .
git status
git commit -m "Add folder structure and test cases (Excel + Markdown)"
git push origin main
Once that's pushed, come back and we'll write the README. Let me know when Step 4 is done.

That's pushed, let's write the README now


Prepared to craft comprehensive README documentation
Prepared to craft comprehensive README documentation
Open the existing README.md in VS Code:

bash
code README.md
Replace everything in it with this content:

markdown
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

Tested with Google Lighthouse (Chrome DevTools) on a simulated Fast 4G connection.

| Metric | Score | Rating |
|--------|-------|--------|
| Performance | 54/100 | 🟡 Needs Improvement |
| Accessibility | 78/100 | 🟡 Needs Improvement |
| Best Practices | 92/100 | 🟢 Good |
| SEO | 88/100 | 🟢 Good |

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

**Immaculata Chepkirui**  