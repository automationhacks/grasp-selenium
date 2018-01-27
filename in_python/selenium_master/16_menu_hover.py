import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MenuHover(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_menu_hover(self):
        self.driver.get('http://jqueryui.com/menu/')
        iframe = self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)
        menu = self.driver.find_element(By.ID, 'ui-id-9')
        submenu = self.driver.find_element(By.XPATH, '//ul/li[text()="Pop"]')

        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.perform()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
