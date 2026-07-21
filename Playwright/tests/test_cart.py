import pytest
from playwright.sync_api import expect

BASE_URL = "https://www.jumia.co.ke"

# A stable product URL to use across cart tests
PRODUCT_URL = BASE_URL + "/samsung-galaxy-a16-6.7-hd-4gb-ram-128gb-dual-sim-50mp-5000mah-black-free-gifts-airpods-smart-watch-powerbank-297282814.html"


def dismiss_overlays(page):
    """Dismiss newsletter popup and any banners."""
    for selector in [
        "button[name='newsletter_popup_close-cta']",
        "button[class*='close']",
        "div[data-pop-id='newsletter'] button",
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
        page.evaluate(
            "document.querySelector('div[data-pop-id=\"newsletter\"]')?.remove()"
        )
    except Exception:
        pass
    try:
        banner = page.get_by_role("button", name="Close banner")
        if banner.is_visible(timeout=1000):
            banner.click()
    except Exception:
        pass


def test_add_to_cart_button_exists_on_product_page(page):
    """TC-016: Add to Cart button is present on a product detail page."""
    page.goto(PRODUCT_URL, wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    dismiss_overlays(page)

    add_to_cart = page.locator(
        "button[data-action*='cart'], "
        "button:has-text('Add to Cart'), "
        "button:has-text('Add To Cart'), "
        "button.-add-to-cart, "
        "button[class*='add-to-cart']"
    )
    assert add_to_cart.count() > 0, "No 'Add to Cart' button found on product page"


def test_product_page_shows_price(page):
    """TC-011: Product detail page shows a price in KSh."""
    page.goto(PRODUCT_URL, wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    dismiss_overlays(page)

    price = page.locator(
        "span[class*='price'], div[class*='price'], "
        "span:has-text('KSh'), div:has-text('KSh')"
    )
    assert price.count() > 0, "No price element found on product page"


def test_product_page_shows_title(page):
    """TC-011: Product detail page shows a product name/title."""
    page.goto(PRODUCT_URL, wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    dismiss_overlays(page)

    title = page.locator("h1, h1[class*='title'], div[class*='name'] h1")
    assert title.count() > 0, "No product title (h1) found on product page"
    title_text = title.first.inner_text().strip()
    assert len(title_text) > 5, f"Product title too short: '{title_text}'"


def test_cart_icon_is_visible_in_header(page):
    """Cart icon with link to /cart/ is visible in header."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    dismiss_overlays(page)

    cart_link = page.locator("a[href='/cart/'], a[href*='cart']").first
    expect(cart_link).to_be_visible()


def test_cart_page_loads(page):
    """TC-017: Cart page loads without error."""
    page.goto(BASE_URL + "/cart/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    dismiss_overlays(page)

    assert "jumia" in page.url.lower(), f"Left Jumia domain: {page.url}"
    assert "error" not in page.title().lower(), f"Error page: {page.title()}"

    # Either shows cart contents or empty cart message
    cart_content = page.locator(
        "div[class*='cart'], section[class*='cart'], "
        "div:has-text('Your cart is empty'), "
        "div:has-text('shopping cart')"
    )
    assert cart_content.count() > 0, "Cart page did not load expected content"


def test_checkout_redirects_to_login_when_not_authenticated(page):
    """TC-035: Checkout requires login for unauthenticated users."""
    page.goto(BASE_URL + "/cart/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    dismiss_overlays(page)

    checkout_btn = page.locator(
        "button:has-text('Checkout'), a:has-text('Checkout'), "
        "button[class*='checkout'], a[class*='checkout'], "
        "a[href*='checkout']"
    )

    if checkout_btn.count() == 0:
        pytest.skip("No checkout button found — cart may be empty")

    checkout_btn.first.click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)

    assert (
        "login" in page.url.lower() or
        "account" in page.url.lower() or
        "signin" in page.url.lower() or
        "sign-in" in page.url.lower()
    ), f"Expected login redirect but got: {page.url}"