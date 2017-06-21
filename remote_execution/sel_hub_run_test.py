import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SelHubTest(unittest.TestCase):
    """
    Commenting firefox, since it requires marrionette to be turned off for FF Version 
    """
    chrome = None
    firefox = None
    ie = None

    @classmethod
    def setUpClass(cls):
        cls.chrome = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME.copy())
        # cls.firefox = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
        cls.ie = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy())

    def test_chrome(self):
        self.chrome.maximize_window()
        self.chrome.get('http://www.google.co.in')
        text_search = self.chrome.find_element_by_id('lst-ib')
        text_search.send_keys('Selenium')
        text_search.send_keys(Keys.ENTER)

        time.sleep(10)
        self.assertIn('selenium', self.chrome.page_source)

    # def test_firefox(self):
    #     self.firefox.maximize_window()
    #     self.firefox.get('http://www.google.co.in')
    #     text_search = self.firefox.find_element_by_id('lst-ib')
    #     text_search.send_keys('Docker containers')
    #     text_search.send_keys(Keys.ENTER)
    #
    #     time.sleep(20)
    #     self.assertIn('Docker containers', self.firefox.page_source)

    def test_ie(self):
        self.ie.maximize_window()
        self.ie.get('http://www.google.co.in')
        text_search = self.ie.find_element_by_id('lst-ib')
        text_search.send_keys('Docker containers')
        text_search.send_keys(Keys.ENTER)

        time.sleep(20)
        self.assertIn('Docker containers', self.ie.page_source)

    @classmethod
    def tearDownClass(cls):
        cls.chrome.close()
        cls.chrome.quit()

        # cls.firefox.close()
        # cls.firefox.quit()

        cls.ie.close()
        cls.ie.quit()

if __name__ == '__main__':
    unittest.main()
