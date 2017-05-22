import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_get_elements_in_list():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://blevmpve01.sthlm.projectplace.com/planview/')
    time.sleep(5)

    _dsn = driver.find_element(By.NAME, 'DSN')
    _user_name = driver.find_element(By.ID, 'Username')
    _password = driver.find_element(By.ID, 'UserPass')
    _sign_in = driver.find_element(By.ID, 'btnLogin')

    Select(_dsn).select_by_visible_text('ppint_gaurav')
    _user_name.send_keys('pvmaster')
    _password.send_keys('ip')
    _sign_in.click()
    Alert(driver).accept()

    driver.find_element(By.LINK_TEXT, 'Work').click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'projectWorkTabToggleLinkContainer'))).click()

    # banner = driver.find_element(By.ID, 'bannerMenuEntities')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'bannerMenuEntities')))
    # driver.implicitly_wait(5)
    # time.sleep(5)

    _works = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@id="bannerMenuEntities"]/ul/li/a[@class="main-item-description"]')))
    # _works = driver.find_elements(By.XPATH, '//div[@id="bannerMenuEntities"]/ul/li/a[@class="main-item-description"]')
    for work in _works:
        print(work.text)

    input('Should i close?')
    driver.close()
    driver.quit()
