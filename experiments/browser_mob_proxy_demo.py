import time
from browsermobproxy import Server, RemoteServer

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

PATH_TO_BROWSER_MOB_PROXY = 'C:\\technical\\selenium\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy'


def start_local_proxy():
    server = Server(PATH_TO_BROWSER_MOB_PROXY)
    server.start()
    proxy = server.create_proxy()
    return proxy, server


def shutdown_local_server(server):
    server.stop()


def start_remote_proxy():
    server = RemoteServer('localhost', 8989)
    proxy = server.create_proxy()
    proxy.add_to_capabilities(DesiredCapabilities.CHROME)
    return proxy


def shutdown_remote_proxy(proxy):
    proxy.close()


def setup_chrome_options(proxy):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver


def login_to_app(driver, proxy):
    proxy.new_har('')
    driver.get('')

    Select(driver.find_element(By.NAME, 'DSN')).select_by_visible_text(' ')
    driver.find_element(By.ID, 'Username').send_keys('')
    driver.find_element(By.ID, 'UserPass').send_keys('')
    driver.find_element(By.ID, 'btnLogin').click()

    har = proxy.har
    return har


def teardown_driver(driver):
    driver.quit()


def wait_for_endpoint(endpoint, proxy, timeout=10):
    poll_frequency = 1
    # This impl is to verify if this works, we can use @wait decorator
    # easily for the same requirement

    def _wait_for_connection():
        for entry in proxy.har['log']['entries']:
            if endpoint in entry['request']['url']:
                status_code = entry['response']['status']
                print('Retrieved status code {}'.format(status_code))
                return status_code == 200

    end_time = time.time() + timeout
    while time.time() < end_time:
        if _wait_for_connection():
            return True
        else:
            poll_frequency *= 1.25
            time.sleep(poll_frequency)


if __name__ == '__main__':
    proxy = start_remote_proxy()
    driver = setup_chrome_options(proxy)
    har = login_to_app(driver, proxy)
    endpoint_url = ''
    print(wait_for_endpoint(endpoint_url, proxy))
    teardown_driver(driver)
    shutdown_remote_proxy(proxy)
