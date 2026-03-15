from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import time

def test_user_registration(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

# Вход
    driver.find_element(By.XPATH, ".//button[text()='Вход и регистрация']").click()
    time.sleep(1)
    assert "/login" in driver.current_url
    driver.find_element(By.XPATH, ".//button[text()='Нет аккаунта']").click()
# регистрация
    new_email = f"Galahova_{random.randint(00, 99)}@mail.ru"

    driver.find_element(By.NAME, "email").send_keys(new_email)
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "submitPassword").send_keys("123456")
    driver.find_element(By.XPATH, ".//button[text()='Создать аккаунт']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "circleSmall")))

    assert driver.find_element(By.CLASS_NAME, "circleSmall").is_displayed()
# python3 -m pytest tests/registration.py -v -s