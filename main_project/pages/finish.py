
from main_project.base.base_class import Base


class FinishPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    # Getters

    # Actions


    # Methods
    def end(self):
        self.get_current_url()
        self.asser_url('https://www.sima-land.ru/cabinet/cart/?per-page=20&sort=-created')
        self.get_screenshot()




