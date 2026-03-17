from selenium.webdriver.common.by import By

class DoskaLocators:
    EMAIL = By.NAME, "email"
    PASSWORD = By.NAME, "password"
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']"
    LOGIN_FORM = By.XPATH, ".//form[@class='popUp_shell__LuyqR']"
    SUBMIT_PASSWORD = By.NAME, "submitPassword"
    BUTTON_CREATE_ACC = By.XPATH, ".//button[text()='Создать аккаунт']"
    LOGIN_AND_REGISTRATION = By.XPATH, ".//button[text()='Вход и регистрация']"
    BUTTON_NO_ACCAUNT = By.XPATH, ".//button[text()='Нет аккаунта']"
    BUTTON_CREATE_CARD = By.XPATH, ".//button[@class='buttonPrimary inButtonText undefined inButtonText']"
    REGISTRANION_FORM = By.XPATH, ".//form[@class='popUp_shell__LuyqR']"
