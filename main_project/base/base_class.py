
import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)


    """Method assert word"""
    def asser_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + ' .png'
        self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\sima-land\\main_project\\screen\\' + name_screenshot)

    """Method assert url"""
    def asser_url(self, result):
        get_url = self.driver.execute_script("return window.location.href")
        assert get_url == result
        print("Good value url")