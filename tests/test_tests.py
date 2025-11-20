from utils.helpers import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

# --------------------------- Кнопка оплатить при моздании платежа Swift --------------------------------------
def test_buttonPay(driver):
    try: #Раздел платежи найти и кликнуть
        payments = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/payments"]')))
        print("Раздел Платежи найденно")
        #Кликнули через js
        driver.execute_script("arguments[0].click();", payments)
        print("Кликнули на на раздел Платежи")

        # Ждём, пока появится хотя бы один нужный элемент
        wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'section._container_1jzfa_19')))
        print("Элементы найденны")
    
        # Получаем все подходящие элементы
        conversions = driver.find_elements(By.CSS_SELECTOR, 'section._container_1jzfa_19')
    
        #Скроливаем на раздел конвертация
        driver.execute_script("arguments[0].scrollIntoView(true);", conversions[1])
        time.sleep(1)
    
        #Кликаем через js
        driver.execute_script("arguments[0].click();", conversions[1])
        print("Кликнули на раздел Swift перевод")
 
        #Ждем появление элемента
        wait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_account_selector_input_back_1m8jn_380')))
        print("Элемент найден")

        # Присваеваем к переменной
        sum_spisan = driver.find_element(By.CLASS_NAME, '_account_selector_input_back_1m8jn_380')
        #Input данные
        time.sleep(1)
        sum_spisan.send_keys(300)
        print("Ввели значение больше чем на балансе")

    # Поле Вид деятельности
        bankSelects = driver.find_elements(By.NAME, 'bank-select')
        bankSelects[0].click()
        
        # Ждём и находим все выподающие элементы
        optionsBankSelect1 = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='_options_container_active']")))
        child_divsBankSelect1 = optionsBankSelect1.find_elements(By.CSS_SELECTOR, "div")
        
        # Нажимаем элемент из выподающего списка
        child_divsBankSelect1[0].click()

    # Swift-код банка
        bankSelects[1].click()

        # Ждём и находим все выподающие элементы
        optionsBankSelect2 = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='_options_container_active']")))
        child_divsBankSelect2 = optionsBankSelect2.find_elements(By.CSS_SELECTOR, "div")

        # Нажимаем на элемент из выпающего списка
        child_divsBankSelect2[0].click()
    
    # Поле Счет или IBAN
        acountOrIbans = driver.find_element(By.NAME, 'accountBankRecipient').send_keys(30000000)

    # Поле Счет получателя
        acountPoluchatel = driver.find_element(By.NAME, 'accountRecipient').send_keys(300)

    # Поле товар и услуги
        tovarAndUslug = driver.find_element(By.CSS_SELECTOR, 'input[type="default"]').click()
        tovarAndUslugList = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='_list_container']")))
        tovarAndUslugListDiv = tovarAndUslugList.find_element(By.CSS_SELECTOR, "div")
        tovarAndUslugListDivElement = tovarAndUslugListDiv.find_elements(By.CSS_SELECTOR, "div")
        tovarAndUslugListDivElement[0].click()

    #  Номер инвойса 8
        invoceNumber_countryPartner = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
        invoceNumber_countryPartner[9].send_keys(11111)
    
    #  Выберите документ
        chooseDocument = driver.find_elements(By.CSS_SELECTOR, 'input[type="default"]')[1].click()
        listchooseDocument = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='_list_container']")))
        listchooseDocumentDiv = listchooseDocument.find_element(By.CSS_SELECTOR, "div")
        listchooseDocumentDivElement = listchooseDocumentDiv.find_elements(By.CSS_SELECTOR, "div")
        listchooseDocumentDivElement[0].click()

    # Название платежа
        driver.find_element(By.CSS_SELECTOR, 'textarea[name="comment"]').send_keys("Тест")

    # Страна партнёра
        invoceNumber_countryPartner[11].click()

        #  Выбираем элемент из списка
        countryPartnerlist = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='_options_container_active']")))
        countryPartnerlistDiv = countryPartnerlist.find_element(By.CSS_SELECTOR, "div")
        countryPartnerlistDivElement = countryPartnerlistDiv.find_elements(By.CSS_SELECTOR, "div")
        countryPartnerlistDivElement[0].click()

    # Кнопка Создать платёж
        wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._btn_b512d_26'))).click()

    # Я согласен
        wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'svg[class*="_checkbox_"]'))).click()

    # Кнопка Создать платёж
        wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._btn_b512d_26'))).click()

    # Проверка высоты родительского контейнера и кнопки Подписать
        parrentDiv = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='_modal_content']")))
        viewport = driver.execute_script("return window.innerHeight") # Высота viewport 
        elem_px = parrentDiv.size['height'] # Высота элемента
        elem_vh = (elem_px / viewport) * 100 # Формула для подсчета vh от пикселя   
        
        assert int(elem_vh) > 85, f"Ожидалось: больше ы{85}vh, но получили {int(elem_vh)}vh"        

    except Exception as e:
        pytest.fail(f"Ошибка: {e}")    
