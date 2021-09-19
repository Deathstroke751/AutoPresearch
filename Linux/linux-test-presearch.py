import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml
import requests
import time
import getpass
from random_word import RandomWords

r = RandomWords()
user = getpass.getuser() 

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument(f'--user-data-dir=/home/{user}/.config/chrome-remote-desktop/chrome-config/google-chrome')
option.add_argument('headless')
driver = webdriver.Chrome(options=option)

token = '1809322932:AAGqJ87VJos42k7edD_vb-sXf7KitT8oP2w'
rec = '484506892'

#Get Token/Search and Max Searches/Day
driver.get('https://presearch.org/account/tokens/rewards')
tps = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[1]/div/div')
mspd = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[2]/div/div')
tps = tps.text
mspd = mspd.text
max = float(tps)*float(mspd)

#Get Balance
driver.get('https://presearch.org/')
span_element = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[5]/a/span/span')
bal = float(span_element.text)

#Get Email
driver.get('https://presearch.org/account')
eml = driver.find_element_by_xpath('//*[@id="main"]/div[1]/p/a')
email = str(eml.text)

fbal = max+bal

x = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={rec}&text={email} - Tokens - {bal} PRE. Max - {fbal}')

i = 1
while bal < fbal and i <= 110:
    driver.get('https://presearch.org/')
    span_element = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[5]/a/span/span')
    bal = float(span_element.text)
    driver.get('https://testnet-engine.presearch.org/')
    searchbox = driver.find_element_by_xpath('//*[@id="Home"]/div[3]/div/div[1]/form/div/input')
    m = str(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10))
    searchbox.send_keys(m)
    searchbox.send_keys(Keys.RETURN)
    time.sleep(3)
    print(f"Attempt : {i} with {m}")
    i += 1

driver.get('https://presearch.org/')
span_element = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[5]/a/span/span')
bal = float(span_element.text)
print('\007')
x = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={rec}&text={email} - Max Search Achieved. Tokens - {bal} PRE')
driver.quit()
