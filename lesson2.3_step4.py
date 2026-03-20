import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
     
    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    
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
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()