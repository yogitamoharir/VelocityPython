# Iframe
# The iframe is a web page inside another webpage
# To perform action on iframe we need to switch selenium focus from main page iframe using 3
# different ways
# Using WelElement
# Using String id/name
# Using index
# To navigate from Iframe to main page we have 2 method parentFrame() & defaultContent()
# parentFrame() :- use to switch selenium focus from child frame to immediate parent frame
# defaultContent() :- use to switch selenium focus fromany child frame to main page

# Ex1: Switch to Frame

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")
# time.sleep(2)
# #Switch to Frame
# # element=driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")
# # driver.switch_to.frame(element) #using WebElement
# #driver.switch_to.frame(0) #using int FrameIndex
# driver.switch_to.frame("iframeResult") #using String FrameId/FrameName
# #click on Date & Time Btn
# driver.find_element(By.XPATH,"//button[contains(text(),'Click me')]").click()
#
# time.sleep(10)


# Ex2: Switch to main page from Iframe

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")
time.sleep(2)

#Switch to Frame
driver.switch_to.frame("iframeResult")

#click on Date & Time Btn from Iframe
driver.find_element(By.XPATH,"//button[contains(text(),'Click me')]").click()
time.sleep(3)

#Switch to Main Page
driver.switch_to.parent_frame()
# driver.switch_to.default_content()

#click on Open menu btn from Main Page
driver.find_element(By.XPATH,"//a[@id='menuButton']").click()
time.sleep(10)