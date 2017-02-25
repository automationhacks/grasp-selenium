import unittest

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MultipleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://demo.mahara.org')
        cls.driver.maximize_window()

    def setUp(self):
        driver = self.driver
        user_name = driver.find_element(By.ID, 'login_login_username')
        password = driver.find_element(By.NAME, 'login_password')
        login_btn = driver.find_element(By.XPATH, '//input[@id="login_submit"]')

        user_name.send_keys('student')
        password.send_keys('MaharaDemo')
        login_btn.click()

    def test_change_max_tags_in_cloud(self):
        driver = self.driver
        settings = driver.find_element(By.LINK_TEXT, 'Settings')
        settings.click()

        driver.implicitly_wait(5)
        max_tags = driver.find_element(By.XPATH, '//div/input[@id="accountprefs_tagssideblockmaxtags"]')
        max_tags.clear()
        max_tags.send_keys('30')
        driver.implicitly_wait(5)

        submit_btn = driver.find_element(By.ID, 'accountprefs_submit')
        submit_btn.click()

        max_tags_after = driver.find_element(By.XPATH, '//div/input[@id="accountprefs_tagssideblockmaxtags"]').get_attribute('value')
        print('=> Current max_tags', max_tags_after)
        self.assertTrue(max_tags_after, '30')

    def test_update_default_licence(self):
        driver = self.driver
        settings = driver.find_element(By.LINK_TEXT, 'Settings')
        settings.click()
        wait = WebDriverWait(driver, 10)

        license_select = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div/span/select[@id="accountprefs_licensedefault"]')))
        select = Select(driver.find_element(By.XPATH, '//div/span/select[@id="accountprefs_licensedefault"]'))
        driver.implicitly_wait(5)

        select.select_by_visible_text('Creative Commons Attribution 4.0')
        driver.implicitly_wait(5)

        submit_btn = driver.find_element(By.ID, 'accountprefs_submit')
        submit_btn.click()

        self.assertTrue(driver.find_element(By.XPATH, '//div/span/select[@id="accountprefs_licensedefault"]/option[@selected="selected"]').text,
                        'Creative Commons Attribution 4.0')

    def tearDown(self):
        driver = self.driver
        logout = driver.find_element(By.LINK_TEXT, 'Logout')
        logout.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
