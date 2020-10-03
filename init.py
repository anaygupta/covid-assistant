from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import pandas as pd
import time
from datetime import datetime
import pyttsx3


#  configured selenium for Brave instead of Chrome
options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver = webdriver.Chrome(
    options=options, executable_path='/Users/~/Downloads/chromedriver')
# driver = webdriver.Chrome(executable_path='/Users/anaygupta/Downloads/chromedriver')

driver.get('https://asuportal.pointnclick.com/login_dualauthentication.aspx')

driver.find_elements_by_id("cmdStudentDualAuthentication")[0].click()


driver.find_element_by_id("username").send_keys("")
driver.find_element_by_id ("password").send_keys("!")
driver.find_element_by_name("submit").click()

# WebDriverWait(driver, .01).until(expected_conditions.presence_of_all_elements_located((By.XPATH, ('//*[@id="ctl03"]/b'))))

time.sleep(10)

driver.find_elements_by_id("dtDOBMN")[0].send_keys('')
driver.find_elements_by_id("dtDOBDY")[0].send_keys('')
driver.find_elements_by_id("dtDOBYR")[0].send_keys('')

driver.find_elements_by_id("cmdStandardProceed")[0].click()

# WebDriverWait(driver, .01).until(expected_conditions.presence_of_all_elements_located((By.XPATH, ('//*[@id="ctl03"]/b'))))

# button = driver.find_elements_by_xpath('//*[@id="'+x+'"]/div/div/a')

# WebDriverWait(driver, .01).until(expected_conditions.presence_of_all_elements_located((By.XPATH, ("//*[@id='ctl03']/h1"))))

# print(home[0].text)


medical_btn = driver.find_elements_by_xpath('//*[@id="sidebar"]/ul/li[16]/a')
driver.execute_script("arguments[0].click();", medical_btn[0])

labs_btn = driver.find_elements_by_xpath('//*[@id="ctl03"]/ul/li[4]/a')
driver.execute_script("arguments[0].click();", labs_btn[0])


# reports = driver.find_elements_by_xpath("//*[contains(@id,'ct')]")
latest_report = driver.find_element_by_xpath('//*[@id="ctl03"]/table/tbody/tr[2]/td[3]/a')
latest_report.click()
# //*[@id="ctl03"]/table/tbody/tr[2]/td[3]/a
# //*[@id="ctl03"]/table/tbody/tr[4]/td[3]/a
# //*[@id="ctl03"]/table/tbody/tr[6]/td[3]/a


driver.switch_to.window(driver.window_handles[1])

date = driver.find_element_by_xpath('/html/body/article/section[1]/header/dl[1]/dd[1]').text
result = driver.find_element_by_xpath('/html/body/article/section[1]/table/tbody/tr[2]/td[2]').text

driver.close()

date, result

driver.switch_to.window(driver.window_handles[0])

driver.close()

# print('As of ' + )
date_time_obj = datetime.strptime(date, '%m/%d/%Y %I:%M %p')
date_time_obj

date = date_time_obj.strftime("%B %d, %Y")

output = 'As of ' + date + ', your coronavirus test result is ' + result.lower() + '.'

engine = pyttsx3.init()
engine.say(output)

print(output)
engine.runAndWait()
# return(output)
