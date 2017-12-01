import xlwt
import xlsxwriter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Page
import webbrowser
from selenium import webdriver
import re
from selenium.common.exceptions import NoSuchElementException
from openpyxl import Workbook

shop = "https://lavkababuin.com/"
# field = "keyword"
book_list = ["Хрома", "Nobrow. Культура маркетинга. Маркетинг культуры", "123", "ДНК особистості"]


def create_file(shop):
    wb = xlsxwriter.Workbook("price_analysis.xlsx")
    ws = wb.add_worksheet("prices")
    bold = wb.add_format({'bold': True})
    ws.write("A1", "Книга", bold)
    ws.write("B1", shop, bold)
    wb.close()


def get_book():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(shop)
    lst = []
    for item in book_list:
        search = driver.find_element(By.ID, "keyword")
        search.send_keys(item)
        search.submit()
        try:
            book = driver.find_element(By.LINK_TEXT, item)
            book.click()
            price = driver.find_element(By.ID, "yproduct_price").text
            lst.append(price)
        except NoSuchElementException:
            driver.find_element(By.ID, "keyword").clear()
            lst.append("0")
    driver.close()
    return lst


def make_price_without_literals():
    a = get_book()
    # to delete literals from price e.g "300 $" => "300"
    lst =[]
    for i in a:
        reg = re.compile("[^0-9]")
        i = reg.sub("", i)
        lst.append(i)
    return lst


def add_prices_to_list():
    # lst = make_price_without_literals()
    lst = ["375", "315", "0", "192"]
    wb = xlsxwriter.Workbook("price_analysis.xlsx")
    ws = wb.add_worksheet("prices")
    row = 1
    col = 0
    num = 1
    for book, price in zip(book_list, lst):
        ws.write(row, col, num)
        ws.write(row, col + 1, str(book))
        ws.write(row, col + 2, int(price))
        row += 1
        num += 1
    wb.close()

add_prices_to_list()
