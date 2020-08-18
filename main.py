from threading import Thread
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import time
import csv

# Constants
driver = webdriver.Chrome("/home/rook/PycharmProjects/news/chromedriver")


def main():
    Asianet_url = "https://www.youtube.com/watch?v=iL53Y28Rp84"
    News24_url = "https://www.youtube.com/watch?v=zcrUCvBD16k"
    Manorma_url = "https://www.youtube.com/watch?v=jjH6v95z3Nw"
    MediaOne_url = "https://www.youtube.com/watch?v=d1iwUB9YFnA"
    while True:
        view_asianet = Asianet(Asianet_url)
        view_24 = News24(News24_url)
        view_manorama = Manorma(Manorma_url)
        view_media1 = MediaOne(MediaOne_url)


        with open('View_log.csv', 'a+', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.datetime.now(), view_asianet, view_24, view_manorama, view_media1])




def Asianet(Asianet_url):
    driver.get(Asianet_url)
    time.sleep(2)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

def News24(News24_url):
    driver.get(News24_url)
    time.sleep(2)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

def Manorma(Manorma_url):
    driver.get(Manorma_url)
    time.sleep(2)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

def MediaOne(MediaOne_url):
    driver.get(MediaOne_url)
    time.sleep(2)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

if __name__ == "__main__":
    main()