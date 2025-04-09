from playwright.sync_api import sync_playwright
from behave import fixture, use_fixture


@fixture
def browser_context(context):
    # Setup: Launch Playwright and browser
    print("before_all rulat")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)  # Headless for quick tests
    context.browser = browser
    context.page = browser.new_page()
    context.base_url = "https://forverkliga.se/JavaScript/my-contacts/#/"  # URL

    yield context  # The tests run here

    # Teardown: Close the browser
    print("after_all rulat")
    browser.close()
    playwright.stop()


def before_all(context):
    use_fixture(browser_context, context)

def before_scenario(context, scenario):
    print(f"before_scenario rulat\nbase_url setat: {context.base_url}")
    context.page.goto(context.base_url)

def after_scenario(context, scenario):
    print("after_scenario rulat")

