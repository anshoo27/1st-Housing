from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
s=Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")   #excutable service patch
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get("https://app.mondofi.co/")

driver.find_element("xpath", '//*[@id="root"]/div/div/form/div[1]/div/input').send_keys("stage_mondofi")
#print(type(userEle))
driver.find_element("xpath", '//*[@id="root"]/div/div/form/div[2]/div/input').send_keys("Z3Pytzsh56eQSZmH")

driver.find_element("xpath", '//*[@id="root"]/div/div/form/div[3]/button').click()
time.sleep(2)
driver.find_element("xpath", '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div/div[2]/ul/li[1]/a').click()
driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[2]/div[3]/form/div[1]/div/input').send_keys("anshoo@yopmail.com")
driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[2]/div[3]/form/div[2]/div/input').send_keys("Test@123")
driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[2]/div[3]/form/div[3]/div/label/span').click()
driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[2]/div[3]/form/div[4]/button').click()
driver.quit()
