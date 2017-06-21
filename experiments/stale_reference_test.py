import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def test_get_elements_in_list():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://blevmpve02.eu.planview.world/planview/')
    time.sleep(5)

    _dsn = driver.find_element(By.NAME, 'DSN')
    _user_name = driver.find_element(By.ID, 'Username')
    _password = driver.find_element(By.ID, 'UserPass')
    _sign_in = driver.find_element(By.ID, 'btnLogin')

    Select(_dsn).select_by_visible_text('')
    _user_name.send_keys('')
    _password.send_keys('')
    _sign_in.click()
    # Alert(driver).accept()

    # driver.get('https://blevmpve02.eu.planview.world/planview/Workflows/wf_ProjDetail.asp?mode=new&wizard=Y&popup=1&back=close')
    # Select(driver.find_element(By.ID, 'Wbs22Code')).select_by_visible_text('Other Planned Work')
    # Select(driver.find_element(By.ID, 'Wbs22Code')).

    driver.find_element(By.LINK_TEXT, 'Work').click()
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'projectWorkTabToggleLinkContainer'))).click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//div[@id="bannerMenuEntities"]//ul//li//a[text()="Auto_UI_created_2017-05-26_15:08:01_909335"]').click()
    time.sleep(10)
    #
    # # banner = driver.find_element(By.ID, 'bannerMenuEntities')
    # WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'bannerMenuEntities')))
    # # driver.implicitly_wait(5)
    # # time.sleep(5)
    #
    # _works = WebDriverWait(driver, 10).until(
    #     ec.presence_of_all_elements_located(
    #         (By.XPATH, '//div[@id="bannerMenuEntities"]/ul/li/a[@class="main-item-description"]')))
    # # _works = driver.find_elements(By.XPATH, '//div[@id="bannerMenuEntities"]/ul/li/a[@class="main-item-description"]')
    # for work in _works:
    #     print(work.text)
    #
    # input('Should i close?')


    driver.close()
    driver.quit()
