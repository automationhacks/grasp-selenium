import assertpy
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestJQueryTabs:
    def test_tab_is_switched(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://jqueryui.com/tabs/')
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, 'iframe'))

        tab1 = self.driver.find_element(By.XPATH, '//div[@id="tabs"]/ul/li[@aria-controls="tabs-1"]')
        assertpy.assert_that(tab1.get_attribute('aria-expanded')).is_true()

        tab2 = self.driver.find_element(By.XPATH, '//div[@id="tabs"]/ul/li[@aria-controls="tabs-2"]')
        tab2.click()
        assertpy.assert_that(tab2.get_attribute('aria-expanded')).is_true()
