import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SwitchWindows(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_switch_windows(self):
        self.driver.get('http://robotframework.org/')
        libraries_link = self.driver.find_element(By.XPATH, '//a[@href="#libraries"]')
        libraries_link.click()

        built_in_link = self.driver.find_element(By.LINK_TEXT, 'Builtin')
        built_in_link.click()

        windows = self.driver.window_handles
        print(len(windows))
        self.driver.switch_to.window(windows[len(windows) - 1])
        time.sleep(5)

        built_in = self.driver.find_element(By.XPATH, '//table/tbody//  td[contains(text(), BuiltIn)]')
        self.assertTrue(built_in.is_displayed())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()