#from bs4 import BeautifulSoup

#import requests

#req = urllib3.PoolManager()
#data = requests.get("https://www.google.com/search?q=junior+ntr")
#soup = BeautifulSoup(data.content,"html.parser")
#print(soup.prettify('utf-8'))
#details = {'wiki':'','insta':'','twit':''}
#for a in soup.find_all('a',href=True):
#    link = a['href']
#    if 'www.instagram.com' in link and details['insta']=='': details['insta']= link
#   elif 'www.twitter.com' in link and details['twit']=='': details['twit']=link
#    elif 'en.wikipedia.org' in link and details['wiki']=='': details['wiki']=link
#print(details) 58.0.3029.81

#import urllib3
"""import requests
#req = urllib3.PoolManager()
data = requests.get("https://www.google.com/search?q=ronaldo",headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
soup = BeautifulSoup(data.content,'html.parser')

#print(soup.prettify())

for a in soup.find_all('a',href=True):
    link = a['href']
    if ('instagram' in link or 'twitter' in link) and len(link)<40:
        print(link)

for text in soup.find_all('span'):
    if len(text.text) > 50:
        print(text.text.encode('utf-8'))"""

from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
import time
import pyautogui as pg
import webbrowser
import pyautogui as pg
import time
import regex as re

firefox_driver = "C:/Users/gurra/OneDrive/Documents/geckodriver"
driver = webdriver.Firefox(executable_path = firefox_driver)
link = 'https://event.webinarjam.com/go/live/377/6kow8f4zcgs2s6'
driver.get(link)
if 'live' in link:
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[1]/input').send_keys('mohan')
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/input').send_keys('mmohan9182@gmail.com')
    driver.find_element_by_xpath('//*[@id="register_btn"]').click()
else:
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="js-reg-btn"]').click()
    time.sleep(5)
    frame = driver.find_element_by_xpath('//*[@id="wj_registration_frame"]')
    driver.switch_to_frame(frame)
    driver.find_element_by_xpath('/html/body/div/div/form/div/div[3]/div[2]/div/div[1]/div[1]/div/div[1]/div/input').send_keys('mohan')
    driver.find_element_by_xpath('/html/body/div/div/form/div/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/div/input').send_keys('mmohan9182@gmail.com')
    driver.find_element_by_id("register_btn").click()
    time.sleep(2)
    pg.moveTo(750,650)
    pg.click()
    time.sleep(5)
    driver.switch_to_default_content()
pg.click(700,700)
link,otp = '',''
while len(link)==0:
    time.sleep(30)
    for a in driver.find_elements_by_tag_name('a'):
        if 'docs' in a.get_attribute('href'):
            link = a.get_attribute('href')
text = driver.find_element_by_tag_name('div').text
r = re.findall(r'[0-9]{4,5}',text)
if r:
    otp = r[0]
    print(r)
print(link,otp)
webbrowser.open(link)


"""firefox_driver = "C:/Users/gurra/OneDrive/Documents/geckodriver"
profile = webdriver.FirefoxProfile()
profile.set_preference("dom.disable_open_during_load", True)
driver = webdriver.Firefox(executable_path = firefox_driver,firefox_profile=profile)
driver.get('https://www.google.com/search?q=chiranjeevi')
for a in driver.find_elements_by_tag_name('a'):
    link = str(a.get_attribute('href'))
    if 'https://www.instagram.com/' == link[:26] or 'https://twitter.com/' == link[:20]:
        print(link)"""

"""import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.google.com/search?q=ram+charan",headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'})
soup = BeautifulSoup(data.content,"html.parser")
count=0
for a in soup.find_all('a',href=True):
	link = a['href']
	if 'instagram' in link or 'twitter' in link and len(link)<40:
		print(link)"""


time .sleep(2)
for pos in pg.locateAllOnScreen('C:/Users/gurra/OneDrive/Pictures/mail.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x+60,y+60)
        pg.write("mmohan9182@gmail.com")
        break

for pos in pg.locateAllOnScreen('C:/Users/gurra/OneDrive/Pictures/name.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x+60,y+60)
        pg.write("Manmohan Gurram")
        break

for pos in pg.locateAllOnScreen('C:/Users/gurra/OneDrive/Pictures/register.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x+60,y+60)
        pg.write("37110260")
        break

pg.scroll(-600)

for pos in pg.locateAllOnScreen('C:/Users/gurra/OneDrive/Pictures/trainer.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x+60,y+58)
        pg.write("Saranya")
        break

for pos in pg.locateAllOnScreen('C:/Users/gurra/OneDrive/Pictures/checkbox.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x-60,y)
        break

for pos in pg.locateAllOnScreen('C:/Users/gurra/OneDrive/Pictures/otp.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x+60,y+60)
        pg.write(otp)
        break

for pos in pg.locateAllOnScreen('C:/Users/gurra/OneDrive/Pictures/submit.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x,y)
        break

"""from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
import regex as re

firefox_driver = "C:/Users/gurra/OneDrive/Documents/geckodriver"
driver = webdriver.Firefox(executable_path = firefox_driver)
driver.get('https://miniwebtool.com/leap-years-list/?start_year=1900&end_year=2020')

text = driver.find_element_by_tag_name('div').text
r = re.findall(r'[0-9]{4,5}',text)
if r:
    print(r)
    print(text.encode('utf-8'))"""





