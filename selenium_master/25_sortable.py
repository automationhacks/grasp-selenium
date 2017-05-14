import assertpy
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_sortable_list():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://jqueryui.com/sortable/')
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'demo-frame'))

    item1 = driver.find_element(By.XPATH, '//ul[@id="sortable"]/li[text()="Item 1"]')
    item2 = driver.find_element(By.XPATH, '//ul[@id="sortable"]/li[text()="Item 2"]')

    item1_height = item1.size.get('height')
    item2_height = item2.size.get('height')

    action = ActionChains(driver)
    action.drag_and_drop_by_offset(item1, 0, item2_height + 5)
    action.perform()
    time.sleep(5)

    items = driver.find_elements(By.XPATH, '//ul[@id="sortable"]/li[text()="Item"]')
    for index, item in enumerate(items):
        if item.get_attribute('value') == 'Item 1':
            assertpy.assert_that(index).is_equal_to(1)
            break

    driver.close()
    driver.quit()
