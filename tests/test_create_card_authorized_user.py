from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import DoskaLocators
from data import EMAIL_EXIST_USER, PASSWORD


class TestCreateCard:
    def test_create_card_aut_user(self, driver):
        # Авторизация
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
                DoskaLocators.POPAP_TO_LOGIN
            )
        )
        driver.find_element(*DoskaLocators.EMAIL).send_keys(EMAIL_EXIST_USER)
        driver.find_element(*DoskaLocators.PASSWORD).send_keys(PASSWORD)
        driver.find_element(*DoskaLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                DoskaLocators.CIRCLE_PROFIL
            )
        )

        driver.find_element(*DoskaLocators.BUTTON_CREATE_CARD).click()

        # основное
        driver.find_element(*DoskaLocators.FILD_NAME).send_keys("Велосипед")
        driver.find_element(*DoskaLocators.FILD_DESCRIPTION).send_keys(
            "Б/у велосипед. Имеет 2 колеса и руль."
        )
        driver.find_element(*DoskaLocators.FILD_PRICE).send_keys(8000)

        # нажимаем на дропдауны
        driver.find_element(*DoskaLocators.DROPDAWN_CATEGORY).click()
        driver.find_element(*DoskaLocators.HOBBY_BUTTON).click()

        # город
        driver.find_element(*DoskaLocators.DROPDAWN_CITY).click()
        driver.find_element(*DoskaLocators.SPB_CITY).click()

        # радио баттн
        driver.find_element(*DoskaLocators.RADIOBUTTON_OLD).click()

        # опубликовать
        driver.find_element(*DoskaLocators.PUBLISH_BUTTON).click()
        # в профиль
        driver.find_element(*DoskaLocators.CIRCLE_PROFIL).click()
        # проверить
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(DoskaLocators.CARD)
        )
        assert driver.find_element(*DoskaLocators.CARD).is_displayed() is True
