"""
1. Hard coded using time.sleep(sec) which suspends thread execution for given secs
2. Explicit wait: Webdriver will wait for condition to be true to proceed

Conditions:
    title_is
    title_contains

    presence_of_element_located
    presence_of_all_elements_located

    visibility_of
    visibility_of_element_located
    invisibility_of_element_located

    text_to_be_present_in_element
    text_to_be_present_in_element_value

    frame_to_be_available_and_switch_to_it

    staleness_of
    alert_is_present

    element_to_be_clickable
    element_to_be_selected
    element_located_to_be_selected
    element_selection_state_to_be
    element_located_selection_state_to_be

3. Implicit wait - polls DOM for certain time while trying to locate element

"""

from time import sleep
import unittest
from unittest import TestLoader, TextTestRunner, TestSuite

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class WaitDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://demo.mahara.org')
        cls.driver.maximize_window()

    def setUp(self):
        print('test started')

    def test_hardcoded_sleep_login_logout(self):
        user_name = self.driver.find_element(By.ID, 'login_login_username')
        password = self.driver.find_element(By.NAME, 'login_password')
        login_btn = self.driver.find_element(By.XPATH, '//div/input[@id="login_submit"]')

        user_name.send_keys('student')
        sleep(5)

        password.send_keys('MaharaDemo')
        sleep(5)

        login_btn.click()
        sleep(5)

        self.assertTrue(self.driver.find_element(By.LINK_TEXT, 'Logout').is_displayed())

    def test_explicit_wait_login_loggout(self):
        user_name = self.driver.find_element(By.ID, 'login_login_username')
        password = self.driver.find_element(By.NAME, 'login_password')
        login_btn = self.driver.find_element(By.XPATH, '//div/input[@id="login_submit"]')

        user_name.send_keys('student')
        password.send_keys('MaharaDemo')
        login_btn.click()

        logout_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Logout')))
        self.assertTrue(logout_link.is_displayed())

    def test_implicit_wait_login_logout(self):
        user_name = self.driver.find_element(By.ID, 'login_login_username')
        password = self.driver.find_element(By.NAME, 'login_password')
        login_btn = self.driver.find_element(By.XPATH, '//div/input[@id="login_submit"]')

        user_name.send_keys('student')
        password.send_keys('MaharaDemo')
        login_btn.click()

        self.driver.implicitly_wait(10)
        logout_link = self.driver.find_element(By.LINK_TEXT, 'Logout')
        self.assertTrue(logout_link.is_displayed())

    def tearDown(self):
        logout_link = self.driver.find_element(By.LINK_TEXT, 'Logout')
        logout_link.click()
        print('test completed')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(WaitDemo('test_hardcoded_sleep_login_logout'))
    suite.addTest(WaitDemo('test_explicit_wait_login_loggout'))
    suite.addTest(WaitDemo('test_implicit_wait_login_logout'))

    runner = TextTestRunner()
    runner.run(suite)
