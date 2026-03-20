import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = " https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел
    num1 = browser.find_element(By.ID, "num1")
    x = num1.text
    num2 = browser.find_element(By.ID, "num2")
    y = num2.text
    summ = str(int(x) + int(y))
    
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(summ)
    
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