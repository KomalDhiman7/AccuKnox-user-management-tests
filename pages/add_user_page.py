class AddUserPage:
    def __init__(self, page):
        self.page = page
        self.role_dropdown = page.locator("(//div[@class='oxd-select-text-input'])[1]")
        self.employee_name = page.get_by_placeholder("Type for hints...")
        self.username = page.locator("(//input[@class='oxd-input oxd-input--active'])[2]")
        self.status_dropdown = page.locator("(//div[@class='oxd-select-text-input'])[2]")
        self.password = page.locator("(//input[@type='password'])[1]")
        self.confirm_password = page.locator("(//input[@type='password'])[2]")
        self.save_btn = page.get_by_role("button", name="Save")

    def add_user(self, emp, username, pwd):
        self.role_dropdown.click()
        self.page.get_by_role("option", name="ESS").click()

        self.employee_name.fill(emp)
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("option").first.click()

        self.username.fill(username)

        self.status_dropdown.click()
        self.page.get_by_role("option", name="Enabled").click()

        self.password.fill(pwd)
        self.confirm_password.fill(pwd)

        self.save_btn.click()
