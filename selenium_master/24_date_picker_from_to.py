import assertpy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_date_picker_range():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://jqueryui.com/datepicker/#date-range')
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'demo-frame'))

    driver.find_element(By.XPATH, '//input[@id="from"]').click()
    Select(driver.find_element(By.XPATH, '//div/select[@class="ui-datepicker-month"]')).select_by_visible_text('May')
    driver.find_element(By.XPATH, '//table/tbody/tr/td/a[text()="1"]').click()

    driver.find_element(By.XPATH, '//input[@id="to"]').click()
    Select(driver.find_element(By.XPATH, '//div/select[@class="ui-datepicker-month"]')).select_by_visible_text('Jun')
    driver.find_element(By.XPATH, '//table/tbody/tr/td/a[text()="1"]').click()

    assertpy.assert_that(driver.find_element(By.XPATH, '//input[@id="from"]').get_attribute('value')).\
        is_equal_to('05/01/2017')
    assertpy.assert_that(driver.find_element(By.XPATH, '//input[@id="to"]').get_attribute('value')). \
        is_equal_to('06/01/2017')

    driver.close()
    driver.quit()
