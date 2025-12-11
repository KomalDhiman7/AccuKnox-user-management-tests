def test_edit_user(page):
    from pages.login_page import LoginPage
    from pages.admin_page import AdminPage
    from pages.edit_user_page import EditUserPage
    from utils.test_data import USERNAME

    login = LoginPage(page)
    admin = AdminPage(page)
    edit = EditUserPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")
    admin.go_to_admin()
    admin.search_user(USERNAME)
    edit.disable_user()
