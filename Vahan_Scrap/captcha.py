
import os

import time
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r"/home/rook/work/scrap/Vahan_Scrap/geckodriver")
base_url = "https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml"
driver.get(base_url)
with open('filename.png', 'wb') as file:
    file.write(driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/div[2]/div/div/img').screenshot_as_png)
