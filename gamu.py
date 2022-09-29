from selenium import webdriver
import argparse
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# defining parser object which takes arguments from command line
parser = argparse.ArgumentParser(usage='python gamu.py [target] [username] [password]', add_help=True)
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
def reload():
        driver.back()
        driver.forward()

def login(username, password):
    driver.get('https://instagram.com')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.NAME, 'username'))).send_keys(username)

    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.TAG_NAME, 'form').submit()
    time.sleep(2)
    return driver

def search(target):

    #driver.find_element(
        #By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()
    # clearing notifiation thingy and searching
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()="Not Now"]'))).click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[text()="Not Now"]').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Explore").click()
    searchField = driver.find_element(By.CSS_SELECTOR, "._aauy")
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
    intro = 'This is an Instagram bot built by Engineer Chiwara (@the.ip.boy.friend on Instagram). It goes to a targets recent post, goes through the people who liked it and follows them in hopes of them following back.'
    print(logo)
    print(intro)
    login(username, password)
    search(target)
