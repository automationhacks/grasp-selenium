import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\selenium\drivers\chromedriver.exe')

    def test_login(self):
        self.driver.get('https://demo.mahara.org/')
        self.assertIn('Home - Mahara', self.driver.title)

        user_name = self.driver.find_element_by_id('login_login_username')
        user_name.send_keys('student')

        password = self.driver.find_element_by_id('login_login_password')
        password.send_keys('MaharaDemo')

        login_btn = self.driver.find_element_by_id('login_submit')
        login_btn.click()

        self.assertTrue(self.driver.find_element_by_link_text('Logout'), 'Logout Link')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
