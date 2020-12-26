import unittest
from selenium import webdriver
import ddt

from page.login_page import LoginPage
from page.home_page import HomePage
from page.bid_page import BidPage
from page.user_page import UserPage
from TestDatas import Global_Datas as GD

class TestInvest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()
        LoginPage(self.driver).login(*GD.user_invest)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_invest_success(self):
        # 1 首页 - 选第一个标
        HomePage(self.driver).click_first_bid()
        bp = BidPage(self.driver)

