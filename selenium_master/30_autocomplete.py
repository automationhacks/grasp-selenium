import time
import assertpy

from selenium.webdriver.common.by import By


def test_auto_complete_is_displayed(get_driver):
    driver = get_driver
    driver.get('https://jqueryui.com/autocomplete/')
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'tags').send_keys('Ja')
    ddl_items = driver.find_elements(By.XPATH, '//ul[@id="ui-id-1"]/li/div[contains(@id, "ui-id")]')

    for item in ddl_items:
        assertpy.assert_that(item).contains('Ja')
    time.sleep(5)


def test_auto_complete_is_selected(get_driver):
    driver = get_driver
    driver.get('https://jqueryui.com/autocomplete/')
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'tags').send_keys('Ja')
    driver.find_element(By.XPATH, '//ul[@id="ui-id-1"]/li/div[text()="Java"]').click()
    assertpy.assert_that(driver.find_element(By.ID, 'tags').get_attribute('value')).is_equal_to('Java')
    time.sleep(5)
