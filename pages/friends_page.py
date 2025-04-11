import re

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
        self.page.wait_for_selector(".friend", timeout=10000)

    def edit_friend(self, old_name: str, new_name: str, new_email: str):
        friend_row = self.page.locator(".friend").filter(has_text=old_name)
        if not friend_row.is_visible():
            raise ValueError(f"Friend '{old_name}' not found in the list")
        friend_row.get_by_text("Ändra").click()
        self.page.wait_for_selector("section.form", timeout=10000)
        self.fill_name(new_name)
        self.fill_email(new_email)
        self.click_save()

    def remove_friend(self, name: str, email: str = None, all_matches: bool = False):
        locator = self.page.locator(".friend").filter(has_text=f"{name} {email}" if email else name)
        if all_matches:
            while locator.count() > 0:
                locator.nth(0).get_by_text("Ta bort").click()
                self.page.wait_for_timeout(500)
        else:
            if not locator.is_visible():
                raise ValueError(f"Friend '{name}' not found")
            locator.get_by_text("Ta bort").click()

    def search_friend(self, search_term: str):
        self.page.locator("input[placeholder='Sök namn']").fill(search_term)
        self.page.wait_for_timeout(500)

    def is_friend_visible(self, name: str, email: str = None):
        if email:
            return self.page.get_by_text(f"{name} {email}").is_visible()
        return self.page.get_by_text(name).is_visible()

