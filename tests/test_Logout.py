from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import DoskaLocators
from data import EMAIL_EXIST_USER, PASSWORD


class Testlogout:
    def test_logout(self, driver):

        # Авторизация
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, ".//form[@class='popUp_shell__LuyqR']")
            )
        )
        driver.find_element(*DoskaLocators.EMAIL).send_keys(EMAIL_EXIST_USER)
        driver.find_element(*DoskaLocators.PASSWORD).send_keys(PASSWORD)
        driver.find_element(*DoskaLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, "circleSmall")
            )
        )
        # выход
        driver.find_element(By.XPATH, ".//button[text()='Выйти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, ".//button[text()='Вход и регистрация']")
            )
        )
        assert (
            driver.find_element(
                By.XPATH, ".//button[text()='Вход и регистрация']"
            ).is_displayed()
            is True
        )
