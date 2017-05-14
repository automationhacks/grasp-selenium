import time
import assertpy

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_jquery_resizable():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://jqueryui.com/selectable/')
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))

    item1 = driver.find_element(By.XPATH, '//ol[@id="selectable"]/li[text()="Item 1"]')
    item2 = driver.find_element(By.XPATH, '//ol[@id="selectable"]/li[text()="Item 2"]')

    actions = ActionChains(driver)
    actions.click(item1)
    actions.send_keys(Keys.CONTROL)
    actions.click(item2)
    actions.perform()

    items = driver.find_elements(By.XPATH, '//ol[@id="selectable"]/li[contains(@class, "ui-selected")]')
    time.sleep(5)
    assertpy.assert_that(len(items)).is_greater_than(1)

    driver.close()
    driver.quit()
