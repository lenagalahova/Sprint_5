from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from locators import DoskaLocators
from data import PASSWORD


class TestAnValidEmail:
    def test_user_an_valid_email(self, driver):
        # Вход
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
                DoskaLocators.POPAP_TO_LOGIN
            )
        )
        driver.find_element(*DoskaLocators.BUTTON_NO_ACCAUNT).click()
        # регистрация невалидная почта
        new_email = f"Galahova_{random.randint(00, 99)}"

        driver.find_element(By.NAME, "email").send_keys(new_email)
        driver.find_element(*DoskaLocators.PASSWORD).send_keys(PASSWORD)
        driver.find_element(*DoskaLocators.SUBMIT_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*DoskaLocators.BUTTON_CREATE_ACC).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                DoskaLocators.ERROR_OF_REGISTRATION
            )
        )
        assert (
            driver.find_element(*DoskaLocators.ERROR_OF_REGISTRATION).is_displayed()
            is True
        )
