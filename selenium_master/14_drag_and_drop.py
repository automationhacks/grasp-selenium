import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ActionChainsDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_action_chains_drag_drop(self):
        self.driver.get('http://jqueryui.com/droppable/')
        iframe = self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)

        draggable = self.driver.find_element(By.XPATH, '//div[@id="draggable"]')
        droppable = self.driver.find_element(By.XPATH, '//div[@id="droppable"]')

        # Action chains
        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable, droppable)
        actions.perform()
        time.sleep(5)

        drag_loc, drop_loc = draggable.location, droppable.location
        drag_x, drop_x = drag_loc.get('x'), drop_loc.get('x')

        print('Locations', drag_loc, drop_loc)
        print('X co-ordinates', drag_x, drop_x)
        self.assertTrue(drag_x > drop_x)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


