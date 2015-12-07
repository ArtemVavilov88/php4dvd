from selenium import webdriver
#import pytest for launching tests using this framework
import pytest
from model.application import Application

#create fixture for tests initialization
@pytest.fixture(scope="module")
def app(request, browser_type, base_url):
    if browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "ie":
        driver = webdriver.Ie()
    driver.implicitly_wait(10)
    #shutdown driver
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)
