from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


def test_create_card_aut_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    # Авторизация
    driver.find_element(By.XPATH, ".//button[text()='Вход и регистрация']").click()

    assert "/login" in driver.current_url
    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys("galahova_31@mail.ru")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "circleSmall")
        )
    )

    driver.find_element(
        By.XPATH,
        ".//button[@class='buttonPrimary inButtonText undefined inButtonText']",
    ).click()

    # основное
    driver.find_element(By.NAME, "name").send_keys("Велосипед")
    driver.find_element(
        By.XPATH, ".//textarea[@class='textarea_inputStandart__IoNxq spanGlobal']"
    ).send_keys("Б/у велосипед. Имеет 2 колеса и руль.")
    driver.find_element(By.NAME, "price").send_keys(8000)

    # нажимаем на дропдауны
    driver.find_element(
        By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[1]/button"
    ).click()
    time.sleep(1)
    driver.find_element(
        By.XPATH,
        "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[2]/button[4]/span",
    ).click()

    driver.find_element(
        By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[3]/div[1]/button"
    ).click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[3]/div[2]/button[2]"
    ).click()

    # радио баттн
    driver.find_element(
        By.XPATH, "//div[@class='radioUnput_inputRegular__FbVbr']"
    ).click()
    # опубликовать
    driver.find_element(
        By.XPATH, "//button[@class='buttonPrimary inButtonText undefined inButtonText']"
    ).click()
    # в профиль
    driver.find_element(By.XPATH, "//button[@class='circleSmall']").click()
    # проверить
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "card"))
    )
    