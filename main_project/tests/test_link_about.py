import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.pages.login_page import LoginPage


class Test1():
    @pytest.mark.test_select_product
    def test_select_product(self):
        driver = webdriver.Firefox()
        base_url = "https://www.sima-land.ru/"
        driver.get(base_url)
        driver.maximize_window()
        print("Start Test")

        login_aksana_user = "+79772562617"
        password_aksana_user = "Sevastopol2024"

        login = LoginPage(driver)
        login.authorization(login_aksana_user, password_aksana_user)

        button_close = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class ='lwldJ g5ORq qaY46']")))
        button_close.click()
        print('Close add')
        time.sleep(3)

        catalog = driver.find_element(By.XPATH, "//button[@class='aDsfj W3geQ']")
        catalog.click()
        print("Open Catalog")

        summer_goods = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-header']/div/div[2]/div[3]/div[1]/ul/li[3]/a")))
        summer_goods.click()
        print("Choose summer goods")

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//h1[@class='gO1Y2N Sgg26k']")))
        value_success_test = success_test.text
        assert value_success_test == "Летние товары"
        print("Test Success")

