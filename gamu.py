from selenium import webdriver
import argparse
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

intro = 'This is an Instagram bot built by Engineer Chiwara (@the.ip.boy.friend on Instagram). It goes to a targets recent post, goes through the people who liked it and follows them in hopes of them following back.'

# defining parser object which takes arguments from command line
parser = argparse.ArgumentParser(description=intro, usage='python gamu.py [target] [username] [password]', add_help=True)
# adding arguments using the parser object
parser.add_argument('target', help='target account')
parser.add_argument('username', help='username of your account')
parser.add_argument('password', help='password of your account')
# setting arguments from parser object into list variable
args = parser.parse_args()
# setting arguments into variables. RIP to RAM
target = args.target
username = args.username
password = args.password

# creating the mozilla driver object
serv = Service(r'C:\Users\Lords\dexterslab\lab\geckodriver.exe')
driver = webdriver.Firefox(service=serv)



def login(username, password):
    driver.get('https://instagram.com')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.NAME, 'username'))).send_keys(username)

    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.TAG_NAME, 'form').submit()
    time.sleep(30)
    return driver


def search(target):

    #driver.find_element(
        #By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()
    # clearing notifiation thingy and searching
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()="Not Now"]'))).click()
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(target)
    time.sleep(10)
    WebDriverWait(driver, 15).until(driver.find_element(By.CSS_SELECTOR, '#mount_0_0_Ia > div > div > div > div.bdao358l.om3e55n1.g4tp4svg > div > div > div > div.alzwoclg.cqf1kptm.p1t2w4gn.fawcizw8.om3e55n1.g4tp4svg > div:nth-child(1) > section > nav > div._acc1._acc3 > div > div > div._aawf._aawg._aexm > div._abn- > div > div._aa61 > div > div._abn_ > a')).click()
    time.sleep(10)
    return driver


if __name__ == '__main__':
    logo = r'''
    _____                       
    / ____|                      
    | |  __  __ _ _ __ ___  _   _ 
    | | |_ |/ _` | '_ ` _ \| | | |
    | |__| | (_| | | | | | | |_| |
    \_____|\__,_|_| |_| |_|\__,_|
                                
                                


    '''
    print(logo)
    login(username, password)
    search(target)
