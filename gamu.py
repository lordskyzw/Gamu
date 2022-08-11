from ast import main
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import botparameters
from botparameters import username, password, search_item


driver = webdriver.Chrome(service=Service(r'C:\Users\im_bradley\Downloads\chromedriver_win32\chromedriver.exe'))



def login(username, password):
    driver.get('https://instagram.com')
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.TAG_NAME, 'form').submit()
    time.sleep(30)   
    return driver

def search(search_term):
    driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()
    driver.find_element(By.NAME, 'search').send_keys(search_term)
    driver.find_element(By.NAME, 'search').send_keys(Keys.RETURN)
    time.sleep(10)
    return driver
    
    


if __name__ == '__main__':
    login(username, password)
    search(search_item)