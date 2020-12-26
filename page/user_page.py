from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class UserPage:



    def __init__(self, driver: WebDriver):
        # 初始化driver
        self.driver = driver

    # 获取用户余额
    def get_user_money(self):
        pass
