import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SelHubTest(unittest.TestCase):
    chrome = None
    firefox = None

    @classmethod
    def setUpClass(cls):
        cls.chrome = webdriver.Remote(command_executor='http://localhost:4446/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        cls.firefox = webdriver.Remote(command_executor='http://localhost:4446/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)

    def test_chrome(self):
        self.chrome.maximize_window()
        self.chrome.get('http://www.google.co.in')
        text_search = self.chrome.find_element_by_id('lst-ib')
        text_search.send_keys('Selenium')
        text_search.send_keys(Keys.ENTER)

        time.sleep(10)
        self.assertIn('selenium', self.chrome.page_source)

    def test_firefox(self):
        self.firefox.maximize_window()
        self.firefox.get('http://www.google.co.in')
        text_search = self.firefox.find_element_by_id('lst-ib')
        text_search.send_keys('Docker containers')
        text_search.send_keys(Keys.ENTER)

        time.sleep(20)
        self.assertIn('Docker containers', self.firefox.page_source)

    @classmethod
    def tearDownClass(cls):
        cls.chrome.close()
        cls.chrome.quit()

        cls.firefox.close()
        cls.firefox.quit()

if __name__ == '__main__':
    unittest.main()
