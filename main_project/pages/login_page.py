import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        solver = TwoCaptcha('7b26684bcd1e1103d9278299a77959f6')
        button_personal_cab = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-header']//div//div[2]//div//div[2]//nav//div[2]//a")))
        button_personal_cab.click()
        print("Click Personal Cab")
        time.sleep(3)

        login_aksana_user = self.driver.find_element(By.XPATH, "//input[@class='WmHUki ubCCEG']")
        login_aksana_user.click()
        login_aksana_user.send_keys(login_name)
        print("Input Login")
        time.sleep(3)

        password_aksana_user = self.driver.find_element(By.XPATH, "//input[@type='password']")
        password_aksana_user.send_keys(login_password)
        print("Input Password")
        time.sleep(3)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#g-recaptcha-response")))
        time.sleep(5)

        result = solver.recaptcha(
            sitekey='6LddTjccAAAAAOgLouQduxanMMM2evmQjxPAJBy_',
            url=self.driver.current_url)['code']
        time.sleep(10)

        symbols = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        for symbol in symbols:
            try:
                resp = self.driver.execute_script(f"return ___grecaptcha_cfg.clients['0']['{symbol}']['{symbol}']")
                if 'callback' in resp:
                    self.driver.execute_script(
                        f"___grecaptcha_cfg.clients['0']['{symbol}']['{symbol}']['callback']('{result}')")
                    print(f"Сегодня буква {symbol}")
                    break
            except Exception:
                pass