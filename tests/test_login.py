from utils.helpers import wait
from pages.login_pages import LoginPage

def test_login(driver):
    page = LoginPage(driver)
    page.open()
    page.enter_username("501012048")
    page.enter_password("1")
    page.click_login()

    # Явное ожидание, пока URL не изменится и не появится "authentication_choice"
    wait(driver, 10).until(
        lambda d: "authentication_choice" in d.current_url.lower()
    )

    assert "authentication_choice" in driver.current_url.lower(), \
        f"Ошибка: после логина остались на {driver.current_url}"
