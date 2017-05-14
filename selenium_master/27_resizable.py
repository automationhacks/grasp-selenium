import time
import assertpy

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_jquery_resizable():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://jqueryui.com/resizable/')
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))

    resizable_header = driver.find_element(By.XPATH, '//div[@id="resizable"]/h3')
    resizable = driver.find_element(By.XPATH, '//div[@class="ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se"]')
    x_before = resizable_header.size.get('width')
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(resizable, x_before + 200, 0)
    actions.perform()
    x_after = resizable_header.size.get('width')
    time.sleep(5)
    assertpy.assert_that(x_after).is_greater_than(x_before)

    driver.close()
    driver.quit()
