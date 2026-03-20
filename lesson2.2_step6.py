import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

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
    
    # Проскроллить страницу вниз.
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    
    # Выбрать radiobutton "Robots rule!
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    
    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()