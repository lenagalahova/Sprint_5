from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import DoskaLocators
from data import EMAIL_EXIST_USER, PASSWORD


class TestAlreadyRegistrated:
    def test_registrating_already_registrated_user(self, driver):

        # Авторизация
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, ".//form[@class='popUp_shell__LuyqR']")
            )
        )
        driver.find_element(*DoskaLocators.BUTTON_NO_ACCAUNT).click()
        # ввод существующего пользователя
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                DoskaLocators.REGISTRANION_FORM
            )
        )

        driver.find_element(*DoskaLocators.EMAIL).send_keys(EMAIL_EXIST_USER)
        driver.find_element(*DoskaLocators.PASSWORD).send_keys(PASSWORD)
        driver.find_element(*DoskaLocators.SUBMIT_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*DoskaLocators.BUTTON_CREATE_ACC).click()

        error = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, "input_span__yWPqB")
            )
        )
        assert "Ошибка" in error.text
