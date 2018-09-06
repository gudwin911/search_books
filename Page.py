from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self, num):
        self.driver.execute_script("window.scrollTo(0, %s);" % num)

    def search(self, field, book, shop):
        txt = self.driver.find_element(By.NAME, "%s" % field)
        txt.send_keys(book)
        txt.submit()
        return SearchResultPage(self.driver, shop)


class SearchResultPage(BasePage):
    def __init__(self, driver, shop):
        super().__init__(driver)
        self.driver.get("%s" % shop)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1")))

    def to_book(self, book):
        self.driver.find_element(By.LINK_TEXT(book)).click()
        return ProductPage(self.driver)


class ProductPage(SearchResultPage):
    def __init__(self, driver):
        super().__init__(self, driver)
        pass
