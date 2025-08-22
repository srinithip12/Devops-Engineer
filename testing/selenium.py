import sys
import pytest
import time
sys.path.append('/appInstall/UserPlugin/pylib')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
TIMEOUT = 60
ENV = "ITG"


def test_setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--proxy-server=http://proxy.example.com:8080")
    driver = webdriver.Remote('http://hub:4444/wd/hub', options=options)
    driver.maximize_window()


def test_login():
    print("Checking the login page")
    process_time = 0
    start_time = time.time()
    driver.get('url')
   try:
        elem = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, "input")))
        elem.send_keys('sample@gmail.com')
        elem = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button")))
        elem.click()
        time.sleep(10)
        elem = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, "input")))
        elem.send_keys('sample')
        elem = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button")))
        elem.click()
        time.sleep(20)
        elem = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, "Menu_DashBoard")))
        elem.click()
        process_time = time.time() - start_time - 30
        print("Application login page --- took %s seconds ---" % process_time)
        print("Login check done")
    except TimeoutException as e:
        print(f"Timeout while waiting for the button. Error: {str(e)}")
        pytest.fail(f"Test failed due to timeout: {str(e)}")
