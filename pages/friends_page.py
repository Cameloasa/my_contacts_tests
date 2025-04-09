
from playwright.sync_api import Page

def fill_name(page: Page, name: str):
    form = page.locator("section.form")
    form.locator("input").nth(0).fill(name)

def fill_email(page: Page, email: str):
    form = page.locator("section.form")
    form.locator("input").nth(1).fill(email)

def click_new_friend(page: Page):
    page.get_by_text("Ny Vän").click()
    page.wait_for_selector("section.form", timeout=10000)

def click_save(page: Page):
    page.get_by_text("Spara").click()

def go_to_friend_list(page: Page):
    page.get_by_text("Vänlista").click()
    page.wait_for_url("https://forverkliga.se/JavaScript/my-contacts/#/friends", timeout=10000)




