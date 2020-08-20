from threading import Thread
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time
import csv

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r"/home/rook/PycharmProjects/news/geckodriver")


def main():
    count = 4
    Asianet_url = "https://www.youtube.com/watch?v=iL53Y28Rp84"
    News24_url = "https://www.youtube.com/watch?v=zcrUCvBD16k"
    Manorma_url = "https://www.youtube.com/watch?v=jjH6v95z3Nw"
    MediaOne_url = "https://www.youtube.com/watch?v=d1iwUB9YFnA"
    while True:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        view_asianet = Asianet(Asianet_url)
        view_24 = News24(News24_url)
        view_manorama = Manorma(Manorma_url)
        view_media1 = MediaOne(MediaOne_url)
        writecsv(current_time, view_asianet, view_24, view_manorama, view_media1)
        print(count)
        count = count + 4


def writecsv(current_time, view_asianet, view_24, view_manorama, view_media1):
    with open('View_log.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, view_asianet, view_24, view_manorama, view_media1])




def Asianet(Asianet_url):
    driver.get(Asianet_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

def News24(News24_url):
    driver.get(News24_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

def Manorma(Manorma_url):
    driver.get(Manorma_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

def MediaOne(MediaOne_url):
    driver.get(MediaOne_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

if __name__ == "__main__":
    main()
