from selenium.webdriver.remote.webdriver import WebDriver

from page.register import Register

class Login:
    def __init__(self,driver:WebDriver):
        self._driver = driver


    def scanf(self):
        pass

    def goto_register(self):

        return Register()