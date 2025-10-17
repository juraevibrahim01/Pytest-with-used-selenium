from selenium.webdriver.support.ui import WebDriverWait

def wait(driver, sec):
    return WebDriverWait(driver, sec)