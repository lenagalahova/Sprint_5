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

        driver.find_element(*DoskaLocators.BUTTON_CREATE_CARD).click()

        # основное
        driver.find_element(By.NAME, "name").send_keys("Велосипед")
        driver.find_element(
            By.XPATH, ".//textarea[@class='textarea_inputStandart__IoNxq spanGlobal']"
        ).send_keys("Б/у велосипед. Имеет 2 колеса и руль.")
        driver.find_element(By.NAME, "price").send_keys(8000)

        # нажимаем на дропдауны
        driver.find_element(
            By.XPATH, "//input[@name='category']/parent::div/button"
        ).click()
        driver.find_element(By.XPATH, ".//button/span[text()='Хобби']").click()

        # город
        driver.find_element(
            By.XPATH, "//input[@name='city']/parent::div/button"
        ).click()
        driver.find_element(
            By.XPATH, ".//span[text()='Санкт-Петербург']/parent::button"
        ).click()

        # радио баттн
        driver.find_element(
            By.XPATH, "//div[@class='radioUnput_inputRegular__FbVbr']"
        ).click()

        # опубликовать
        driver.find_element(
            By.XPATH,
            "//button[@class='buttonPrimary inButtonText undefined inButtonText']",
        ).click()
        # в профиль
        driver.find_element(By.XPATH, "//button[@class='circleSmall']").click()
        # проверить
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "card"))
        )
        assert driver.find_element(By.CLASS_NAME, "card").is_displayed() is True
