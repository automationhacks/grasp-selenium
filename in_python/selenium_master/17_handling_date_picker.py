import assertpy

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_date_picker():
    driver = webdriver.Chrome(r'C:\selenium\drivers\chromedriver.exe')
    driver.maximize_window()

    driver.get('https://jqueryui.com/datepicker/')
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'demo-frame'))

    driver.find_element(By.ID, 'datepicker').click()
    driver.find_element(By.XPATH, '//table/tbody/tr/td/a[text()="18"]').click()
    driver.implicitly_wait(10)
    assertpy.assert_that(driver.find_element(By.ID, 'datepicker').get_attribute('value')).is_equal_to('05/18/2017')

    driver.close()
    driver.quit()
