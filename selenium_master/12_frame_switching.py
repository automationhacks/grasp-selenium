import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By


class SwitchingToFrame(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_switch_to_frame(self):
        self.driver.get('http://jqueryui.com/dialog/')
        frame = self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(frame)

        iframe_title = self.driver.find_element_by_xpath('//span[text()="Basic dialog"]')
        print(iframe_title.text)

        assert iframe_title.is_displayed()
        self.driver.switch_to.default_content()

        try:
            iframe_title = self.driver.find_element_by_xpath('//span[text()="Basic dialog"]')
            print(iframe_title)
        except:
            print('Element not found from outside IFrame')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
