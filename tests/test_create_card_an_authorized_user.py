from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_create_card_an_aut_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(By.XPATH, ".//button[@class='buttonPrimary inButtonText undefined inButtonText']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")))
