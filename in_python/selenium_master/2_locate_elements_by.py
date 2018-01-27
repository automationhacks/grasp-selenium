import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demo.mahara.org')

def login_logout():
    user_name = driver.find_element(By.ID, 'login_login_username')
    password = driver.find_element(By.NAME, 'login_password')
    login_btn = driver.find_element(By.ID, 'login_submit')

    user_name.send_keys('student')
    password.send_keys('MaharaDemo')
    login_btn.click()

    logout = driver.find_element(By.LINK_TEXT, 'Logout')
    assert (logout.is_displayed())
    logout.click()

    login_btn = driver.find_element(By.ID, 'login_submit')
    assert (login_btn.is_displayed())

def all_tags():
    all_links = driver.find_elements(By.TAG_NAME, 'a')
    urls = [link.get_attribute('href') for link in all_links]
    print(urls)

def teardown():
    driver.close()
    driver.quit()


if __name__ == '__main__':
    # login_logout()
    all_tags()
    teardown()
