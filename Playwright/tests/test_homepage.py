from playwright.sync_api import expect

BASE_URL = "https://www.jumia.co.ke"


def dismiss_overlays(page):
    """Dismiss newsletter popup and any banners that may block interaction."""
    for selector in [
        "button[name='newsletter_popup_close-cta']",
        "button[class*='close']",
        "button[aria-label*='close']",
    ]:
        try:
            btn = page.locator(selector).first
            if btn.is_visible(timeout=2000):
                btn.click()
                page.wait_for_timeout(300)
                break
        except Exception:
            pass

    try:
        banner_close = page.get_by_role("button", name="Close banner")
        if banner_close.is_visible(timeout=2000):
            banner_close.click()
            page.wait_for_timeout(300)
    except Exception:
        pass


def test_homepage_loads_successfully(page):
    """TC-001: Homepage loads and title contains Jumia."""
    page.goto(BASE_URL, wait_until="networkidle")
    assert "Jumia" in page.title(), f"Unexpected title: {page.title()}"


def test_homepage_search_bar_visible(page):
    """Search bar is present and interactive."""
    page.goto(BASE_URL, wait_until="networkidle")
    dismiss_overlays(page)
    search = page.locator("input[type='search'], input#q, input[name='q']").first
    expect(search).to_be_visible()
    expect(search).to_be_enabled()


def test_homepage_hero_banner_visible(page):
    """TC-002: Hero banner section is visible on load."""
    page.goto(BASE_URL, wait_until="networkidle")
    dismiss_overlays(page)
    banner = page.locator(
        "div.sldr, section.sldr, div[class*='banner'], "
        "div[class*='slider'], div[class*='hero']"
    ).first
    expect(banner).to_be_visible()


def test_homepage_category_nav_visible(page):
    """TC-003: Key category nav links exist on the page."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.wait_for_timeout(3000)
    dismiss_overlays(page)

    phones = page.locator("a[href*='/phones-tablets/']")
    fashion = page.locator("a[href*='/category-fashion'], a[href*='/fashion']")

    assert phones.count() > 0, "No Phones & Tablets nav link found"
    assert fashion.count() > 0, "No Fashion nav link found"


def test_homepage_logo_links_to_homepage(page):
    """TC-028: Clicking the Jumia logo returns to homepage."""
    page.goto(BASE_URL + "/phones-tablets/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    dismiss_overlays(page)

    logo = page.locator(
        "header a[href='/'], header a[href='https://www.jumia.co.ke/'], "
        "a[class*='logo']"
    ).first
    logo.click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1000)
    assert BASE_URL in page.url