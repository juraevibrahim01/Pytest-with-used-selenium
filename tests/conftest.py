import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture
def driver():
    # Для простоты без явного пути к драйверу
    service = Service(executable_path="drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
