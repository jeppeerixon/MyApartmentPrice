import time
import sqlite3
from string import digits
from tqdm import tqdm
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#conn = sqlite3.connect('hempris.sqlite')
#cur = conn.cursor()

#cur.execute('''
#            CREATE TABLE IF NOT EXISTS Twitter
#            (name TEXT, retrieved INTEGER, friends INTEGER)''')

options = Options()
#options.add_argument("--headless")
#options.add_argument('log-level=3') options=options
webb=wd.Chrome('chromedriver.exe')
webb.get('https://www.hemnet.se/')

print('- - - - - - - - -')
sokort = input("Välj område i Stockholm: ")
print('- - - - - - - - -')
print('Data collection started')
print('- - - - - - - - -')

time.sleep(2)
kakor = webb.find_element_by_class('hcl-button hcl-button--primary')
kakor.click()

time.sleep(1)
slut = webb.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/ul/li[2]/label')
slut.click()

sok = webb.find_element_by_xpath('//*[@id="area-search-input-box"]')
sok.send_keys(sokort)
time.sleep(2)
sok.send_keys(Keys.ENTER)

time.sleep(1)
hitta = webb.find_element_by_xpath('//*[@id="search-form"]/div[3]/div[2]/div/button[2]')
hitta.click()
time.sleep(1)

res_list = webb.find_elements_by_class_name('sold-results__normal-hit')
salda_link = []

for el in res_list:
    res_link = el.find_elements_by_class_name('sold-property-listing')
    salda_link.append(res_link[0].get_property('href'))

slutpriser = []
kvm_alla = []
adresser = []
grundpris = []

for i in tqdm(salda_link[0:5]):
    time.sleep(1)
    webb.get(i)
    adress = webb.find_element_by_tag_name('h1')
    slut = webb.find_element_by_class_name('sold-property__price-value')
    kvm = webb.find_elements_by_class_name('sold-property__attribute-value')
    time.sleep(1)
    slutpriser.append(slut.text)
    grundpris.append(kvm[1].text)
    kvm_alla.append(kvm[4].text)
    adresser.append(adress.text)

print(slutpriser)
print(kvm_alla)
print(adresser)
print(grundpris)

print('- - - - - - - - -')
print('Data collection finished')

slut_ren = []
kvm_ren = []
adre_ren = []
grund_ren = []
okat_ren = []

for x in slutpriser:
    kr = x.split(" kr")
    krspace = kr[0].replace(" ", "")
    krint = float(krspace)
    slut_ren.append(krint)

for x in kvm_alla:
    kvm = x.split(" m²")
    kvm2 = kvm[0].replace(',', '.')
    kvmint = float(kvm2)
    kvm_ren.append(kvmint)

for x in adresser:
    adre = x.split("Slutpris\n")
    #kvm2 = kvm[0].replace(',', '.')
    #kvmint = float(kvm2)
    adre_ren.append(adre[1])

for x in grundpris:
    grund = x.split(" kr")
    grund2 = grund[0].replace(" ", "")
    grund3 = float(grund2)
    grund_ren.append(grund3)

for x in slut_ren:
    diff = x
    #fixa något najs här för att räkna ut prisökning
    #utan att använda hemnets grejs
    okat_ren.append(diff)


print(adre_ren)
print(grund_ren)
print(okat_ren)





#cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
            #VALUES (?, 0, 1)''', (friend, ))

#conn.commit()

#cur.close()




#https://matplotlib.org/stable/gallery/index.html#text-labels-and-annotations
#https://docs.streamlit.io/en/stable/api.html#display-charts
# https://www.youtube.com/watch?v=wCoTJdhRcQE&ab_channel=TechnologyforNoobs 22:11 loop för links
# tqdm = progressbar för kommandogrejen.
# = Forbidden = måste använda selenium = Går att bybass med Getrequest hack?
# Version 88.0.4324.150
# options = webdriver.ChromeOptions();
# options.add_argument('headless');
# options.add_argument('window-size=1200x600'); // optional
