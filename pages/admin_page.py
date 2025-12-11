class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_tab = page.get_by_role("link", name="Admin")
        self.add_btn = page.get_by_role("button", name="Add")
        self.search_username = page.get_by_placeholder("Username")
        self.search_btn = page.get_by_role("button", name="Search")

    def go_to_admin(self):
        self.admin_tab.click()

    def search_user(self, username):
        self.search_username.fill(username)
        self.search_btn.click()
