from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(r'C:\Users\im_bradley\Downloads\chromedriver_win32\chromedriver.exe'))
driver.get("https://instagram.com")
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys("tarmicas_code")
password.send_keys("")
driver.find_element(By.TAG_NAME, 'form').submit()
time.sleep(60)
