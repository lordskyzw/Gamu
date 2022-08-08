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
password.send_keys("Tarmica12580")
driver.find_element(By.TAG_NAME, 'form').submit()

time.sleep(60)
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(60)
#clicking the not now button for notifications
driver.find_element(By.XPATH, '//*[@id="mount_0_0_MK"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
time.sleep(30)

driver.find_element(By.XPATH, '//*[@id="mount_0_0_Zp"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()