from selenium.webdriver.common.by import By
from utils.helpers import wait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(driver, 10)

        # Элементы (локаторы)
        self.username_field = (By.CSS_SELECTOR, 'input[type="string"]')
        self.password_field = (By.CSS_SELECTOR, 'input[type="password"]')
        self.login_button = (By.CSS_SELECTOR, 'button[type="submit"]')

    def open(self):
        """Открывает страницу логина"""
        self.driver.get("http://business-test.humo.tj:8081/login")

    def enter_username(self, username):
        """Вводит логин"""
        try:
            field = self.wait.until(EC.presence_of_element_located(self.username_field))
            print("Поле логина найдено")
            field.send_keys(username)
            print("Ввели логин")
        except:
            print("Ошибка: поле логина не найдено")

    def enter_password(self, password):
        """Вводит пароль"""
        try:
            field = self.wait.until(EC.presence_of_element_located(self.password_field))
            print("Поле пароля найдено")
            field.send_keys(password)
            print("Ввели пароль")
        except:
            print("Ошибка: поле пароля не найдено")

    def click_login(self):
        """Кликает на кнопку входа"""
        try:
            button = self.wait.until(EC.element_to_be_clickable(self.login_button))
            print("Кнопка входа найдена")
            button.click()
            print("Кликнули на кнопку")
        except:
            print("Ошибка: кнопка входа не найдена")
