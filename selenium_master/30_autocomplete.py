import time
import assertpy

from selenium.webdriver.common.by import By


def test_auto_complete_is_displayed(get_driver):
    driver = get_driver
    driver.get('https://jqueryui.com/autocomplete/')
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'tags').send_keys('Ja')
    ddl_item = driver.find_elements(By.XPATH, '//body/ul/li/div[text()="Java"]')
    assertpy.assert_that(ddl_item).is_not_empty()


def test_auto_complete_is_selected(get_driver):
    driver = get_driver
    driver.get('https://jqueryui.com/autocomplete/')
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'tags').send_keys('Ja')
    driver.find_element(By.XPATH, '//ul[@id="ui-id-1"]/li/div[text()="Java"]').click()
    assertpy.assert_that(driver.find_element(By.ID, 'tags').get_attribute('value')).is_equal_to('Java')
    time.sleep(5)
