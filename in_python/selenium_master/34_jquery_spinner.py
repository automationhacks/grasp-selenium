import assertpy
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSpinner:
    def test_jquery_spinner(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://jqueryui.com/spinner/')
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, 'iframe'))

        up_btn = self.driver.find_element(By.XPATH, '//span/a[contains(@class, "ui-spinner-up")]')
        up_btn.click()
        up_btn.click()
        up_btn.click()
        spinner_input = self.driver.find_element(By.XPATH, '//span/input[@id="spinner"]')
        assertpy.assert_that(spinner_input.get_attribute('aria-valuenow')).is_equal_to(str(3))
        time.sleep(5)

        spinner_input.clear()
        down_btn = self.driver.find_element(By.XPATH, '//span/a[contains(@class, "ui-spinner-down")]')
        down_btn.click()
        down_btn.click()
        down_btn.click()
        assertpy.assert_that(spinner_input.get_attribute('aria-valuenow')).is_equal_to(str(-3))
        time.sleep(5)

        self.driver.close()
        self.driver.quit()
