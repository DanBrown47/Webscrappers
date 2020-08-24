# import multiprocessing
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time
import csv

state = "KL"
dist = "11"
# letters = "A"
# i = "1"
options = Options()
# options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r"/home/rook/PycharmProjects/news/geckodriver")
base_url = "https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml"


letterlist = ["A","B"]
def main():
    driver.get(base_url)
    captcha = input("Your Captcha Here")
    for letters in letterlist:
        for i in range(1, 10**4):
            plate = state + str(dist) + letters + str(i)
            driver.find_element_by_id("regn_no1_exact").clear()
            driver.find_element_by_id("regn_no1_exact").send_keys(plate)
            driver.find_element_by_id("txt_ALPHA_NUMERIC").send_keys(captcha)
            driver.find_element_by_xpath("/html/body/form/div[1]/div[3]/div/div[2]/div/div/div[2]/div[4]/div/button").click()
            time.sleep(4)
            extract_data()


def extract_data():
    page =  driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    details_3 = soup.findAll("div", {"class": "col-md-3"})


    try:
        registration_no = clean(details_3[1].get_text())
    except IndexError:
        print("Vehicle not found")
    else:
        block_2(soup)



def block_2(soup):
    details_1 = soup.findAll("div", {"class": "top-space"})
    details_3 = soup.findAll("div", {"class": "col-md-3"})
    details_9 = soup.findAll("div", {"class": "col-md-9"})
    registration_no = clean(details_3[1].get_text())
    reg_place = clean(details_1[2].get_text())
    chasis_no = clean(details_3[5].get_text())
    engine_no = clean(details_3[7].get_text())
    vehicle_class = clean(details_3[10].get_text())
    name = clean(details_9[0].get_text())
    fuel = clean(details_3[12].get_text())
    maker_model = clean(details_9[1].get_text())
    fitness = clean(details_3[15].get_text())
    MV_Tax = clean(details_3[17].get_text())
    Insurance = clean(details_3[19].get_text())
    PUCC = clean(details_3[21].get_text())
    Emmision_norms = clean(details_3[23].get_text())
    RC_Status = clean(details_3[25].get_text())



    print(reg_place)
    print(registration_no)
    print(chasis_no)
    print(engine_no)
    print(vehicle_class)
    print(name)
    print(fuel)
    print(maker_model)
    print(fitness)
    print(MV_Tax)
    print(Insurance)
    print(PUCC)
    print(Emmision_norms)
    print(RC_Status)
    print("\n")
    print("\n")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx")
    print("\n")
    print("\n")




    
            






def clean(data):
    u = str(data)
    v = u.strip()
    w = v.replace('\n', '')
    x = w.replace('<td style="text-align: left;">', '')
    y = x.replace("  ", "")
    z = x.replace('<td>', '')
    result = z.replace('</td>', '')
    return result


if __name__ == '__main__':
    main()
