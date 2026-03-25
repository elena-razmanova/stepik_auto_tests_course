import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import LOGIN, PASSWORD

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_open_Chrome(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    button_enter = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    button_enter.click()
    
    email = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
    )
    email.send_keys(LOGIN)
    
    password = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    password.send_keys(PASSWORD)
    
    button_Enter_2 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_Enter_2.click()
    
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message"))
        )
    # Если элемент найден - тест падает
        assert False, "Сообщение об ошибке появилось, но не должно было"
    except TimeoutException:
    # Элемент не появился за 5 секунд - это успех
        pass