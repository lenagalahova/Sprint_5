import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service("/Users/elena/WebDriver/bin/chromedriver"))
    driver.maximize_window()
    
    # Передаем драйвер в тест
    yield driver

    time.sleep(3) 
    driver.quit()