# WebElement Methods:
# Use to perform action on elements present in browser
#
# 1:  send_keys() : use to enter value in text field
# 2:  clear() : use discard value from text field
# 3: click(): use to click on button/link & use to select radio button/checkboxes
# 4: text:  getText from webpage
# 5: get_attribute("value") : getText value from input field
# 6: is_enabled() : used to verify if an element is enabled or not. If element is enabled return true otherwise returns false
# 7: is_selected() : used to verify if a radio button or checkbox is selected or not. If it is selected return true otherwise returns false
# 8: is_displyed() : used to verify if an element is present or not. If element is present return true otherwise returns false


# 1: Sendkeys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#apr1
#driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc")

#apr2
un=driver.find_element(By.XPATH,"//input[@id='email']")
un.send_keys("abc")


time.sleep(5)


# 2: clear()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#apr1
# driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@id='email']").clear()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@id='email']").send_keys("xyz")

#apr2
un=driver.find_element(By.XPATH,"//input[@id='email']")
un.send_keys("abc")
time.sleep(2)
un.clear()
time.sleep(2)
un.send_keys("xyz")


time.sleep(5)


# 3: click()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#click on create new acc link
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
time.sleep(2)
#click on female radio button
driver.find_element(By.XPATH,"(//input[@class='_8esa'])[1]").click()

time.sleep(5)


# 4: getText from input field
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#get text from input field
un=driver.find_element(By.XPATH,"//input[@id='email']")

un.send_keys("abc")
time.sleep(2)

text=un.get_attribute("value")
print(text)

time.sleep(5)

# 5: getText from webpage
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#get text from webpage
info=driver.find_element(By.XPATH,"//button[@type='submit']").text
print(info)

time.sleep(5)

# 6: isEnabled()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

result=driver.find_element(By.XPATH,"//button[@type='submit']").is_enabled()
print(result)
print(type(result))

if result:
    print("Element is Enabled")
else:
    print("Element is disabled")

# 7: isSelected()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#click on create new acc link
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()

time.sleep(3)

driver.find_element(By.XPATH,"(//input[@class='_8esa'])[1]").click()

result=driver.find_element(By.XPATH,"(//input[@class='_8esa'])[1]").is_selected()
print(result)


time.sleep(10)

# 8: isDisplayed()
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

# result=driver.find_element(By.XPATH,"//a[text()='Create new account']").is_displayed()
# print(result)


try:
    result = driver.find_element(By.XPATH, "//a[text()='Create new account']").is_displayed()
    print("Element is present")
except NoSuchElementException:
    print("Element is not present")


time.sleep(10)










