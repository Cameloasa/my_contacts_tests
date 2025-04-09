
from playwright.sync_api import Page

class FriendsPage:

    def __init__(self, page: Page):
        self.page = page


    def click_new_friend(self):
        self.page.get_by_text("Ny Vän").click()
        self.page.wait_for_selector("section.form", timeout=10000)

    def fill_name(self, name: str):
        form = self.page.locator("section.form")
        form.locator("input").nth(0).fill(name)

    def fill_email(self, email: str):
        form = self.page.locator("section.form")
        form.locator("input").nth(1).fill(email)


    def click_save(self):
        save_button = self.page.get_by_text("Spara")
        if save_button.is_disabled():
            error_message = self.page.locator("p.error").inner_text()
            raise ValueError(f"Cannot save – error: {error_message}")
        save_button.click()

    def go_to_friend_list(self):
        self.page.get_by_text("Vänlista").click()
        self.page.wait_for_url("https://forverkliga.se/JavaScript/my-contacts/#/friends", timeout=10000)

    def is_friend_visible(self, name: str):
        pass




