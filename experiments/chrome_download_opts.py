from selenium import webdriver


def get_driver():
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': r'C:\dummy'}
    options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(chrome_options=options)
    return browser


def download_file():
    driver = get_driver()
    driver.get('http://www.sample-videos.com/download-sample-xls.php')
    driver.find_elements_by_xpath('//a[text()="Click"]')[0].click()


def close_stuff(driver):
    driver.close()
    driver.quit()


def run():
    driver = get_driver()
    download_file()
    close_stuff(driver)

if __name__ == '__main__':
    run()