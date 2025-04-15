# Listbox

# Ex1: Select option – single selectable

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
time.sleep(2)

#Step1: identify listbox
month=driver.find_element(By.XPATH,"//select[@id='month']") #WebElement Object

#Step2: Create Object Select class
s=Select(month)
#3: call select class method
s.select_by_visible_text("Jun") #String Text
#s.select_by_value("8") #String value
# s.select_by_index(11)
time.sleep(5)



# Ex2: Select option – Multi selectable

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("file:///D:/6th%20July%202024/Selenium/html%20files/Sample4_Listbox.html")
time.sleep(2)
#Step1: identify listbox
selectCountry=driver.find_element(By.XPATH,"//select[@id='abc123']") #WebElement Object
#Step2: Create Object Select class
s=Select(selectCountry)
#3: call select class method
s.select_by_visible_text("Ind")
s.select_by_visible_text("Aus")
#s.select_by_value()
s.select_by_index(2)
time.sleep(5)


# Ex2: De Select option – single selectable

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("file:///D:/6th%20July%202024/Selenium/html%20files/Sample4_Listbox.html")
time.sleep(2)
selectCountry=driver.find_element(By.XPATH,"//select[@id='abc123']") #WebElement Object
s=Select(selectCountry)

s.select_by_index(0)
s.select_by_index(1)
s.select_by_index(2)
time.sleep(4)
s.deselect_by_visible_text("Ind")
#s.deselect_by_value()
s.deselect_by_index(1)
time.sleep(5)


# Ex4: DeSelect option – Multi selectable


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("file:///D:/6th%20July%202024/Selenium/html%20files/Sample4_Listbox.html")
time.sleep(2)
selectCountry=driver.find_element(By.XPATH,"//select[@id='abc123']") #WebElement Object
s=Select(selectCountry)
s.select_by_index(0)
s.select_by_index(1)
s.select_by_index(2)
time.sleep(4)
s.deselect_all()
time.sleep(5)


# Ex5: get Type listbox (single or multi)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
time.sleep(4)
month=driver.find_element(By.XPATH,"//select[@id='month']")
s=Select(month)
print(s.is_multiple)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("file:///D:/6th%20July%202024/Selenium/html%20files/Sample4_Listbox.html")
time.sleep(2)
selectCountry=driver.find_element(By.XPATH,"//select[@id='abc123']") #WebElement Object
s=Select(selectCountry)
print(s.is_multiple)
time.sleep(5)


# EX6.1: get Selected option from Single Selected listbox

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
time.sleep(2)
#Step1: identify listbox
month=driver.find_element(By.XPATH,"//select[@id='month']") #WebElement Object
s=Select(month)

#method 1
textValue=s.first_selected_option.text
print(textValue)

#method 2
# selectedOption=s.first_selected_option
# textValue2=selectedOption.text
# print(textValue2)

#method 3
# selectedOption=s.first_selected_option
# print(selectedOption.text)

time.sleep(10)


# EX6.2: get first Selected option from multi Selected listbox

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("file:///D:/6th%20July%202024/Selenium/html%20files/Sample4_Listbox.html")
time.sleep(2)
selectCountry=driver.find_element(By.XPATH,"//select[@id='abc123']") #WebElement Object
s=Select(selectCountry)
s.select_by_index(0)
s.select_by_index(1)
s.select_by_index(2)
textValue=s.first_selected_option.text
print(textValue)
time.sleep(10)


# EX7: get all seleted options from multi seleted listbox

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("file:///D:/6th%20July%202024/Selenium/html%20files/Sample4_Listbox.html")
time.sleep(2)
selectCountry=driver.find_element(By.XPATH,"//select[@id='abc123']") #WebElement Object
s=Select(selectCountry)
s.select_by_index(0)
s.select_by_index(1)
s.select_by_index(2)
allSelectedOptions=s.all_selected_options
print(len(allSelectedOptions))
for i in allSelectedOptions:
 print(i.text)
time.sleep(10)


# EX8: get all options from multi seleted listbox\

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("file:///D:/6th%20July%202024/Selenium/html%20files/Sample4_Listbox.html")
time.sleep(2)
selectCountry=driver.find_element(By.XPATH,"//select[@id='abc123']") #WebElement Object
s=Select(selectCountry)
allOptions=s.options
print(len(allOptions))
for i in allOptions:
 print(i.text)
time.sleep(10)