from os import system, name
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
except:
    if name == 'nt':
        os.system("pip install selenium")
    else:
        os.system("sudo pip3 install selenium")
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

if name == 'nt':
    import getpass
else:
    print('Not windows huh ?')  

r = RandomWords()
windows_username = getpass.getuser()
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation'])
if name == 'nt':
	option.add_argument(f'--user-data-dir=C:\\Users\\{windows_username}\\AppData\\Local\\Google\\Chrome\\User Data')
else:
	option.add_argument(f'--user-data-dir=/home/user/.config/chrome-remote-desktop/chrome-config/google-chrome')
#options.add_argument(r'--profile-directory=YourProfileDir')
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
