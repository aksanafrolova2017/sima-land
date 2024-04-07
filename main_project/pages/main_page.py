from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.base.base_class import Base




class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_section_product_xpath = "//a[@href='/posuda/?banner_main=44932&chpnk=1']"
    dishes = "//a[@href='/stolovaya-posuda/']"
    plates = "//*[@id='category-page__root']/div/div[2]/div[1]/ul/li[1]/a"
    price = "//*[@id='category-page__root']/div/div[2]/div[3]/div[1]/div/div[2]/div/div/label[2]/div"
    plate = "//*[@id='category-page__root']/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/button"
    cart = "//a[@href='/cabinet/cart/']"



    # Getters
    def get_select_section_product_xpath(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_section_product_xpath)))

    def get_dishes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dishes)))

    def get_plates(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plates)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_plate(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plate)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))





    # Actions
    def click_select_section_product_xpath(self):
        self.get_select_section_product_xpath().click()
        print("Click select section product 1")

    def click_dishes(self):
        self.get_dishes().click()
        print("Click select dishes")

    def click_plates(self):
        self.get_plates().click()
        print("Click select plates")

    def click_price(self):
        self.get_price().click()
        print("Click select price")


    def click_plate(self):
        self.get_plate().click()
        print("Click select plate")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")



# Methods
    def select_section_product_1(self):
        self.get_current_url()
        self.click_select_section_product_xpath()
        self.click_dishes()
        self.click_plates()
        self.click_price()
        self.click_plate()
        self.click_cart()
        self.asser_url('https://www.sima-land.ru/cabinet/cart/?per-page=20&sort=-created')












