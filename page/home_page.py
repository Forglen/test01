from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    # 退出
    exit_loc = (By.XPATH, '//a[text()="退出"]')
    # 关于我们
    about_us = (By.XPATH, '//a[text()="关于我们"]')
    # 用户昵称
    user_link = (By.XPATH, '//a[@href="/Member/index.html"]')
    # 抢投标按钮
    bid_button = (By.XPATH, '//a[text()="抢投标"]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_element_exists(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.exit_loc))
        except:
            return False
        else:
            return True

    def click_first_bid(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(self.bid_button))
        self.driver.find_element(*self.bid_button).click()

