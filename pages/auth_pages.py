from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import wait
import pyotp

class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(driver, 10)

        # Элементы (локаторы)
        self.inputAuth = (By.CSS_SELECTOR, 'input[name="first"]')

    def twofa(self):
        try:
             # Генерация отп
            secret = "U75FSFTNSI7SVJ3R"

            # создаём объект TOTP
            totp = pyotp.TOTP(secret)

            # получить текущий 6-значный код
            return totp.now()
        except:
            print("Ошибка 2fa")

    def input(self, input):
        try:
            # Вводим 2fa
            inputField = self.wait.until(EC.presence_of_element_located(self.inputAuth))
            print("Поле input-2fa найденно")
            inputField.send_keys(input)
        except:
            print("Поле input-2fa не найденно")