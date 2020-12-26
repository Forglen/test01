from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    # 用户名输入框
    user_input = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_input = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    login_button = (By.TAG_NAME, "button")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, username, password):
        # WebDriverWait()
        sleep(2)
        self.driver.find_element(*self.user_input).send_keys(username)
        print(self.user_input,">>>>>>>>>>",*self.user_input)

        self.driver.find_element(*self.passwd_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()