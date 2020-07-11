from selenium import webdriver
import webbrowser
import pyautogui as pg
import time
import regex as re

#If you are uisng chrome comment out the 11 and 12 lines
chrome_driver = "Drivers/chromedriver"
driver = webdriver.Firefox(executable_path = chrome_driver)

#If you are using firefox comment out the 8 and 9 lines
firefox_driver = "Drivers/geckodriver"
driver = webdriver.Firefox(executable_path = firefox_driver)

# Enter the link 
link = 'link'

driver.get(link)

#Enter your College name and email here for future purpose
name = 'name' 
email = 'email'
reg = 'reg'

#Below is code for if the link is for live session it will enter name and mail of the user and gets in else it will automatically registers
if 'live' in link:
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[1]/input').send_keys(name)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/input').send_keys(email)
    driver.find_element_by_xpath('//*[@id="register_btn"]').click()
else:
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="js-reg-btn"]').click()
    time.sleep(5)
    frame = driver.find_element_by_xpath('//*[@id="wj_registration_frame"]')
    driver.switch_to_frame(frame)
    driver.find_element_by_xpath('/html/body/div/div/form/div/div[3]/div[2]/div/div[1]/div[1]/div/div[1]/div/input').send_keys(name)
    driver.find_element_by_xpath('/html/body/div/div/form/div/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/div/input').send_keys(email)
    driver.find_element_by_id("register_btn").click()
    time.sleep(2)
    pg.moveTo(750,650)
    pg.click()
    time.sleep(5)
    driver.switch_to_default_content()
pg.click(700,700)
link,otp = '',''
#This is for extracting all the hyperlinks in the currently running vedio once it find the hyperlink it will be redirected to webbrowser for autofilling
while len(link)==0:
    time.sleep(30)
#This is used for extracting hyperlink
    for a in driver.find_elements_by_tag_name('a'):
        if 'docs' in a.get_attribute('href'):
            link = a.get_attribute('href')
#This is used for extracting otp
text = driver.find_element_by_tag_name('div').text
#Extracting the 4 digit number from the text
r = re.findall(r'[0-9]{4,5}',text)
if r:
    otp = r[0]
    print(r)
print(link,otp)
webbrowser.open(link)

#This is used for Locating the parts of images on the screen and entering values in the google forms
time .sleep(5)
for pos in pg.locateAllOnScreen('Attendence Pictures/mail.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x+60,y+60)
        pg.write(email")
        break

for pos in pg.locateAllOnScreen('Attendence Pictures/name.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x+60,y+60)
        pg.write(name)
        break

for pos in pg.locateAllOnScreen('Attendence images/register.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x+60,y+60)
        pg.write(reg)
        break

pg.scroll(-600)

for pos in pg.locateAllOnScreen('Attendence images/trainer.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x+60,y+58)
        pg.write("Saranya")
        break

for pos in pg.locateAllOnScreen('Attendence images/checkbox.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x-60,y)
        break

for pos in pg.locateAllOnScreen('Attendence images/otp.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x+60,y+60)
        pg.write(otp)
        break

for pos in pg.locateAllOnScreen('Attendence images/submit.png',confidence=.8):
    if pos:
        x,y = pg.center(pos)
        pg.click(x,y)
        break






