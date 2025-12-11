def test_search_user(page):
    from pages.login_page import LoginPage
    from pages.admin_page import AdminPage
    from utils.test_data import USERNAME

    login = LoginPage(page)
    admin = AdminPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")
    admin.go_to_admin()
    admin.search_user(USERNAME)
