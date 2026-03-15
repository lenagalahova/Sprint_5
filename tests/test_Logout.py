from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

def test_logout(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

# Авторизация
    driver.find_element(By.XPATH, ".//button[text()='Вход и регистрация']").click()
    time.sleep(1)
    assert "/login" in driver.current_url

    driver.find_element(By.NAME, "email").send_keys("galahova_31@mail.ru")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "circleSmall")))
# выход
    driver.find_element(By.XPATH, ".//button[text()='Выйти']").click()
