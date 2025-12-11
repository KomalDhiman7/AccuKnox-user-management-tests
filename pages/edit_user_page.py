class EditUserPage:
    def __init__(self, page):
        self.page = page
        self.edit_icon = page.locator("i.oxd-icon.bi-pencil-fill").first
        self.status_dropdown = page.locator("(//div[@class='oxd-select-text-input'])[1]")
        self.save_btn = page.get_by_role("button", name="Save")

    def disable_user(self):
        self.edit_icon.click()
        self.status_dropdown.click()
        self.page.get_by_role("option", name="Disabled").click()
        self.save_btn.click()
