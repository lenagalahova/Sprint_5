from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import DoskaLocators


class TestCreateCardAutUser:
    def test_create_card_an_aut_user(self, driver):

        driver.find_element(*DoskaLocators.BUTTON_CREATE_CARD).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                DoskaLocators.POPUP_FOR_AUTORIZATION
            )
        )
        assert (
            driver.find_element(*DoskaLocators.POPUP_FOR_AUTORIZATION).is_displayed()
            is True
        )
