import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DragDropByOffsetDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_drag_and_drop_by_offset(self):
        self.driver.get('http://jqueryui.com/draggable/')
        iframe = self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)

        draggable = self.driver.find_element(By.ID, 'draggable')
        loc_before_drag = draggable.location
        loc_x_before_drag = loc_before_drag.get('x')

        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(draggable, '100', '0')
        actions.perform()
        time.sleep(5)

        loc_after_drag = draggable.location
        loc_x_after_drag = loc_after_drag.get('x')

        self.assertTrue(loc_x_after_drag > loc_x_before_drag)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
