from playwright.sync_api import sync_playwright
from behave import fixture, use_fixture

from pages.friends_page import FriendsPage


@fixture
def browser_context(context):
    print("before_all run")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context.browser = browser
    context.page = browser.new_page()
    context.base_urls = {
        "main": "https://forverkliga.se/JavaScript/my-contacts/#/",
        "add": "https://forverkliga.se/JavaScript/my-contacts/#/add",
        "list": "https://forverkliga.se/JavaScript/my-contacts/#/friends"
    }
    context.page.goto(context.base_urls["main"])

    yield context

    print("after_all run")
    browser.close()
    playwright.stop()

def before_all(context):
    use_fixture(browser_context, context)

def before_scenario(context, scenario):
    print(f"before_scenario run\nbase_url set: {context.base_urls['main']}")
    context.page.goto("https://forverkliga.se/JavaScript/my-contacts/#/friends")
    context.friends_page = FriendsPage(context.page)
    for name, email in [
        ("Test Friend", "test@example.com"),
        ("Ana", "ana@example.com"),
        ("Bob", "bob@example.com"),
        ("Updated Friend", "test@example.com"),
        ("Test Friend", "updated@example.com")
    ]:
        context.friends_page.remove_any_existing(name, email)

def after_scenario(context, scenario):
    print("after_scenario run")
