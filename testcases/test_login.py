from selenium import webdriver

from page.login_page import LoginPage
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://120.78.128.25:8765/Index/login.html")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_success(self):
        LoginPage(self.driver).login("18684720553", "python")
        pass
