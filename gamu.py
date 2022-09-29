from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import argparse
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

intro ='This is an Instagram bot built by Engineer Chiwara (@the.ip.boy.friend on Instagram). It goes to a targets recent post, goes through the people who liked it and follows them in hopes of them following back.'

#defining arguments 
parser =argparse.ArgumentParser(description=intro, usage='python gamu.py [target] [username] [password]', add_help=True)
#adding arguments
parser.add_argument('target', help='target account')
parser.add_argument('username', help='username of your account')
parser.add_argument('password', help='password of your account')
#read arguments from command line
args = parser.parse_args()
#setting arguments into variables. RIP to RAM 
target = args.target
username = args.username
password = args.password

#just to show that arguments were taken
logo = r'''

'''
#print(logo)
options = Options()
#options.headless = True
driver = webdriver.Chrome(options=options, service=Service(r'C:\Users\im_bradley\Downloads\chromedriver_win32\chromedriver.exe'), port=51508)



def login(username, password):
    driver.get('https://instagram.com')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'username'))).send_keys(username)
    
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.TAG_NAME, 'form').submit()
    time.sleep(30)   
    return driver

def search(target):
    
    driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()
    #clearing notifiation thingy and searching
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Not Now"]'))).click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(target)
    time.sleep(10)
    WebDriverWait(driver, 15).until(driver.find_element(By.CSS_SELECTOR, '#mount_0_0_Ia > div > div > div > div.bdao358l.om3e55n1.g4tp4svg > div > div > div > div.alzwoclg.cqf1kptm.p1t2w4gn.fawcizw8.om3e55n1.g4tp4svg > div:nth-child(1) > section > nav > div._acc1._acc3 > div > div > div._aawf._aawg._aexm > div._abn- > div > div._aa61 > div > div._abn_ > a')).click()
    time.sleep(10)
    return driver
    
    

if __name__ == '__main__':
    login(username, password)
    search(target)