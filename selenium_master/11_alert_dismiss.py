import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class AlertDismiss(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_alert_dismiss(self):
        self.driver.get('http://127.0.0.1:5000/')
        radio_btn = self.driver.find_element(By.XPATH, '//input[@value="TC2"]')
        cancel_btn = self.driver.find_element(By.NAME, 'cancel_btn')

        radio_btn.click()
        cancel_btn.click()

        time.sleep(5)
        alert_text = Alert(self.driver).text
        print(alert_text)

        Alert(self.driver).dismiss()

        page_src = self.driver.page_source
        status = page_src.find('TC2')
        self.assertTrue(status > 0)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
