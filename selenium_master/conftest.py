import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()
