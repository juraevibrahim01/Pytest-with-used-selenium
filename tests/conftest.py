import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_pages import LoginPage
from pages.auth_pages import AuthPage
from utils.helpers import wait

@pytest.fixture
def driver():
    # Для простоты без явного пути к драйверу
    service = Service(executable_path="drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def login_and_check_banner(driver):
    # Pages Login
    page = LoginPage(driver)
    page.open()
    page.enter_username("501012048")
    page.enter_password("1")
    page.click_login()

    # Pages Auth
    wait(driver, 10).until(lambda d: "authentication_choice" in d.current_url.lower())

    auth = AuthPage(driver)
    authCode = auth.twofa()
    auth.input(authCode)

    try:
        wait(driver, 10).until(lambda d: "accounts" in d.current_url.lower())
        print("Успешно вошли в ИБ, успешного тестирования")
    except Exception as e:
        pytest.fail(f"Ошибка: Ошибка: не получилось войти в ИБ : {e}")