import time
import assertpy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_text_operations_in_tiny_mce():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://www.tinymce.com/docs/demo/full-featured/')
    driver.switch_to.frame(driver.find_element(By.ID, 'cp_embed_NGegZK'))
    driver.switch_to.frame(driver.find_element(By.ID, 'result-iframe'))
    driver.switch_to.frame(driver.find_element(By.ID, 'mce_0_ifr'))

    mce = driver.find_element(By.XPATH, '//body[@id="tinymce"]')
    mce.clear()

    mce.send_keys('Entering text here')
    mce.send_keys(Keys.ENTER)
    mce.send_keys('Hahaha! Yo')
    time.sleep(5)

    text = mce.text
    assertpy.assert_that(text).contains('Haha')

    driver.close()
    driver.quit()
