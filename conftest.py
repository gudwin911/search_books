from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()