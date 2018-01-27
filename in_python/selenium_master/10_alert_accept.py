import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class AlertTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_alert_accept(self):
        self.driver.get('http://127.0.0.1:5000/')
        radio_option = self.driver.find_element(By.XPATH, '//input[@value="TC2"]')
        remove_btn = self.driver.find_element(By.NAME, 'remove_btn')

        radio_option.click()
        remove_btn.click()

        alert_text = Alert(self.driver).text
        print(alert_text)

        Alert(self.driver).accept()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()