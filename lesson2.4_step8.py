import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait    
from selenium.webdriver.support import expected_conditions as EC 
import time

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    price = WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    button_book = browser.find_element(By.CSS_SELECTOR, "[id='book']")
    button_book.click()
    
    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    # Считать значение для переменной x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Посчитать математическую функцию от x 
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)     
    
    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    
    # Нажать на кнопку Submit
    button2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()