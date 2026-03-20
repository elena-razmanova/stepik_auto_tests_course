import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.CSS_SELECTOR,'[name="firstname"]')
    first_name.send_keys("Elena")
    last_name = browser.find_element(By.CSS_SELECTOR,'[name="lastname"]')
    last_name.send_keys("Razmanova")
    Email = browser.find_element(By.CSS_SELECTOR,'[name="email"]')
    Email.send_keys("Razmanova.l@yandex.ru")
    
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "test.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    # отправляем файл
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    
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