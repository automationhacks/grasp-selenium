import assertpy
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestTooltip:
    def test_jquery_tool_tip(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://jqueryui.com/tooltip/')
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, 'iframe'))

        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.ID, 'age'))
        actions.perform()

        assertpy.assert_that(self.driver.find_element(By.CLASS_NAME, 'ui-tooltip-content').text).\
            is_equal_to('We ask for your age only for statistical purposes.')

        time.sleep(5)
        self.driver.close()
        self.driver.quit()
