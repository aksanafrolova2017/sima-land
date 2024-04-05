import time
import pytest
from selenium import webdriver
from main_project.pages.main_page import MainPage
from main_project.pages.finish import FinishPage

class Test2():
    @pytest.mark.test_buy_product_1
    def test_buy_product_1(self):
        driver = webdriver.Firefox()
        base_url = "https://www.sima-land.ru/"
        driver.get(base_url)
        driver.maximize_window()
        print("Start Test 2")

        mp = MainPage(driver)
        mp.select_section_product_1()

        fp = FinishPage(driver)
        fp.end()

        print("Finish Test 2")
        time.sleep(5)
        driver.quit()






