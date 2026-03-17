from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from locators import DoskaLocators
from data import PASSWORD


class TestRegistration:
    def test_user_registration(self, driver):

        # Вход
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, ".//form[@class='popUp_shell__LuyqR']")
            )
        )
        driver.find_element(*DoskaLocators.BUTTON_NO_ACCAUNT).click()
        # регистрация
        new_email = f"Galahova_{random.randint(000, 9999)}@mail.ru"
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                DoskaLocators.REGISTRANION_FORM
            )
        )

        driver.find_element(By.NAME, "email").send_keys(new_email)
        driver.find_element(*DoskaLocators.PASSWORD).send_keys(PASSWORD)
        driver.find_element(*DoskaLocators.SUBMIT_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*DoskaLocators.BUTTON_CREATE_ACC).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, "circleSmall")
            )
        )

        assert driver.find_element(By.CLASS_NAME, "circleSmall").is_displayed() is True
