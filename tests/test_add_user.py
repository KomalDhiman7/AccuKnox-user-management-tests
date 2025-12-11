import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage
from utils.test_data import USERNAME, PASSWORD, EMPLOYEE_NAME

def test_add_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)
    add_user = AddUserPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")
    admin.go_to_admin()
    add_user.add_user(EMPLOYEE_NAME, USERNAME, PASSWORD)
