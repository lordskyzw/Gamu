from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time




driver = webdriver.Chrome(service=Service(r'C:\Users\im_bradley\Downloads\chromedriver_win32\chromedriver.exe'))
driver.get("https://instagram.com")

time.sleep(60)
