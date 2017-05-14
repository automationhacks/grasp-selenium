import assertpy
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_jquery_slider():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://jqueryui.com/slider/#default')
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))

    slider = driver.find_element(By.XPATH, '//div[@id="slider"]/span')
    loc_x = slider.location.get('x')
    print('Before sliding ', loc_x)
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slider, loc_x + 20, 0)
    actions.perform()
    loc_x_after = slider.location.get('x')
    print('After sliding ', loc_x_after)
    assertpy.assert_that(loc_x_after).is_greater_than(loc_x)
    time.sleep(5)

    driver.close()
    driver.quit()
