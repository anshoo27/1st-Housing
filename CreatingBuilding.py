import select

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support.select import Select  #import select matchod for Select

from selenium.webdriver.common.by import By #import By mathod
import keyboard
from keyboard import press

from selenium.webdriver.chrome.service import Service
#s=Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")   #excutable service patch
#driver = webdriver.Chrome(service=s)
driver=webdriver.Chrome() # changed the chrome location to the python installed folder
#driver.maximize_window()
driver.get("https://app.mondofi.co/")

driver.find_element("xpath", '//*[@id="root"]/div/div/form/div[1]/div/input').send_keys("stage_mondofi")

driver.find_element("xpath", '//*[@id="root"]/div/div/form/div[2]/div/input').send_keys("Z3Pytzsh56eQSZmH")

driver.find_element("xpath", '//*[@id="root"]/div/div/form/div[3]/button').click()
#time.sleep(2)
driver.find_element("xpath", '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div/div[2]/ul/li[3]/a').click()
driver.find_element("xpath", "//input[@placeholder='Enter your first name']").send_keys("Ash")
driver.find_element("xpath", "//input[@placeholder='Enter your last name']").send_keys("Ish")
driver.find_element("xpath", "//input[@placeholder='Enter email']").send_keys("ashi@yopmail.com")
driver.find_element("xpath", "//input[@placeholder='XXX-XXX-XXXX']").send_keys(9418035364)
driver.find_element("xpath", "//input[@placeholder='Enter building name']").send_keys("Lake View")
driver.find_element("xpath", "//input[@placeholder='Your building name']").send_keys("Lake")
driver.find_element("xpath", "//input[@placeholder='Enter building address']").send_keys("Surrey")
time.sleep(2)
driver.find_element("xpath", "//div[@class='autocomplete-dropdown-container']/div[2]").click()
#driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div/div[11]/div[2]/div/div/div[1]').click()
#time.sleep(2)

timezone = driver.find_element("xpath", "//div[@class='Select RemoveLine__input']/input");
timezone.send_keys("(GMT-08:00) Pacific Time (US & Canada");
press('enter')  #need to import keyboard and before that need to install keyboard through pip
#keyboard.press_and_release('enter')
driver.find_element("xpath", "//input[@placeholder='Enter password']").send_keys("Test@123")
driver.find_element("xpath", "//input[@placeholder='Confirm password']").send_keys("Test@123")
driver.find_element("xpath", "//button[@type='Submit']").click()
driver.close()


# driver.get("https://sadmin.mondofi.co/")
# time.sleep(2)
# print(driver.title)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
