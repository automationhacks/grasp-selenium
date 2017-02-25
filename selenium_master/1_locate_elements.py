import time

from selenium import webdriver

"""
Available locators:
    find_element_by_id
    find_element_by_name
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector
"""

driver = webdriver.Chrome()
driver.get('https://demo.mahara.org')
driver.maximize_window()


def by_id():
    user_name = driver.find_element_by_id('login_login_username')
    user_name.send_keys('By Id')
    return user_name


def by_name():
    user_name = driver.find_element_by_name('login_username')
    user_name.send_keys('By Name')
    return user_name


def by_xpath():
    user_name = driver.find_element_by_xpath('//input[@id="login_login_username"]')
    user_name.send_keys('Found by Xpath')
    return user_name


def by_link_text():
    wiki = driver.find_element_by_link_text('Mahara wiki')
    wiki.click()
    sleep(5)
    driver.back()


def by_partial_link_text():
    mahara_user = driver.find_element_by_partial_link_text('Mahara user')
    print(mahara_user.get_attribute('href'))


def by_tag_name():
    footer = driver.find_element_by_tag_name('footer')
    print(footer.text)


def by_class_name():
    login_related_links = driver.find_element_by_class_name('login-related-links')
    print(login_related_links.text)


def by_css_selector():
    logo = driver.find_element_by_css_selector('a.logo')
    print(logo.get_attribute('href'))


def clear_text(ctrl):
    ctrl.clear()


def sleep(sec):
    time.sleep(sec)


def close_driver():
    driver.close()
    driver.quit()


if __name__ == '__main__':
    # user_name = by_id()
    # user_name = by_name()
    # user_name = by_xpath()
    # by_link_text()
    # by_partial_link_text()
    # by_tag_name()
    # by_class_name()
    # by_css_selector()
    sleep(5)
    close_driver()
