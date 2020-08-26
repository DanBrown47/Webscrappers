# import multiprocessing
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

state = "KL"
dist = "11"
# letters = "A"
# i = "1"
options = Options()
# options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r"/home/rook/work/scrap/Vahan_Scrap/geckodriver")
base_url = "https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml"


letterlist = ["A","B"]
def main():
    driver.get(base_url)
    captcha = get_captcha()
    for letters in letterlist:
        for i in range(1, 10**4):
            plate = state + str(dist) + letters + str(i)
            driver.find_element_by_id("regn_no1_exact").clear()
            driver.find_element_by_id("regn_no1_exact").send_keys(plate)
            driver.find_element_by_id("txt_ALPHA_NUMERIC").send_keys(captcha)
            try:
                driver.find_element_by_xpath("/html/body/form/div[1]/div[3]/div/div[2]/div/div/div[2]/div[4]/div/button").click()
            except:
                print("Add time")
            time.sleep(2)
            extract_data()

def get_captcha():
    driver.find_element_by_id("regn_no1_exact").send_keys("KL11A01")
    for i in range(100):
            driver.find_element_by_id("txt_ALPHA_NUMERIC").clear()
            driver.find_element_by_id("txt_ALPHA_NUMERIC").send_keys(i)
            driver.find_element_by_xpath("/html/body/form/div[1]/div[3]/div/div[2]/div/div/div[2]/div[4]/div/button").click()
            time.sleep(2)
            page =  driver.page_source
            soup = BeautifulSoup(page, 'html.parser')
            details_3 = soup.findAll("div", {"class": "col-md-3"})
            try:
                registration_no = clean(details_3[1].get_text())
            except IndexError:
                print("Captcha is not"+ str(i)+ "Checking" + str(i+1))
            else:
                captcha = i
                print(captcha)
                return captcha

def extract_data():
    page =  driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    details_3 = soup.findAll("div", {"class": "col-md-3"})


    try:
        registration_no = clean(details_3[1].get_text())
        print(registration_no)
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
    with open('main.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([registration_no,reg_place,chasis_no,engine_no,vehicle_class,name,fuel,maker_model,fitness,MV_Tax,Insurance,PUCC,Emmision_norms,RC_Status])



def clean(data):
    u = str(data)
    v = u.strip()
    w = v.replace('\n', '')
    x = w.replace('"', '')
    y = x.replace("  ", "")
    z = x.replace('/', ' ')
    result = z.replace(',', '')
    return result


if __name__ == '__main__':
    main()
