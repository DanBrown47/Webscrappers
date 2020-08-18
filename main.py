from selenium import webdriver

from bs4 import BeautifulSoup
import time




# Constants
driver = webdriver.Chrome("/home/rook/PycharmProjects/news/chromedriver")
url = "https://www.youtube.com/watch?v=iL53Y28Rp84"

driver.get(url)
time.sleep(3.5)
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
# print(soup)
span = soup.find("span", {"class":"view-count"})
watch = span.text
number = int(''.join(filter(str.isdigit, watch)))
print(number)