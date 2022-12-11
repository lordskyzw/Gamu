from selenium import webdriver
from selenium.common import exceptions
import argparse
import time
import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Gamu():
    def __init__(self):
    # defining parser object which takes arguments from command line
        parser = argparse.ArgumentParser(usage='python gamu.py [target] [username] [password]', add_help=True)
        # adding arguments using the parser object
        parser.add_argument('target', help='target account')
        parser.add_argument('username', help='username of your account')
        parser.add_argument('password', help='password of your account')
        # setting arguments from parser object into list variable
        args = parser.parse_args()
        # setting arguments into variables. RIP to RAM
        self.target = args.target
        self.username = args.username
        self.password = args.password
        # creating the mozilla driver object
        self.serv = Service(r'C:\Users\Lords\dexterslab\lab\geckodriver.exe')
        self.driver = webdriver.Firefox(service=self.serv)
    

    
        def reload(self):
                driver = self.driver
                driver.back()
                driver.forward()

    def login(self):
        driver = self.driver
        driver.get('https://instagram.com')
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.NAME, 'username'))).send_keys(self.username)
            driver.find_element(By.NAME, 'password').send_keys(self.password)
            driver.find_element(By.TAG_NAME, 'form').submit()
            time.sleep(2)
        except TimeoutError:
            print('Timeout error occured')
            
        return driver

    def search(self):
        driver = self.driver
        target = self.target
        #driver.find_element(
            #By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()
        # clearing notifiation thingy and searching
        try:
            WebDriverWait(driver, 25).until(EC.element_to_be_clickable(
                (By.XPATH, '//button[text()="Not Now"]'))).click()
            time.sleep(2)
        except exceptions.NoSuchElementException:
            pass
        try:
            driver.find_element(By.XPATH, '//button[text()="Not Now"]').click()
            time.sleep(3)
        except exceptions.NoSuchElementException:
            pass
        try:
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[2]/div/div").click()
        except exceptions.NoSuchElementException:
            driver.find_element(By.CLASS_NAME, 'coreSpriteSearchIcon').click()
        time.sleep(3)
        keyboard.write(target)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[text()="{}"]'.format(target))))
        driver.find_element(By.XPATH, '//div[text()="{}"]'.format(target)).click()
        time.sleep(2)
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
    
    gamu = Gamu()
    gamu.login()
    gamu.search()
