from os import system
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from botparameters import username, password, search_item


system.setProperty('webdriver.chrome.driver', r'C:\Users\im_bradley\Downloads\chromedriver_win32\chromedriver.exe')
ChromeOptions = webdriver.ChromeOptions()
Options.add_argument('--headless')
Options.add_argument('--no-sandbox')
Options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(ChromeOptions)



def login(username, password):
    driver.get('https://instagram.com')
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.TAG_NAME, 'form').submit()
    time.sleep(30)   
    return driver

def search(search_term):
    
    driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()
    #clearing notifiation thingy
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
    driver.find_element(By.NAME, 'search').send_keys(search_term)
    driver.find_element(By.NAME, 'search').send_keys(Keys.RETURN)
    time.sleep(10)
    return driver
    
    

if __name__ == '__main__':
    login(username, password)
    search(search_item)