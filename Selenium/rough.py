print("----------mouse action button_------")

# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# Element=driver.find_element(By.XPATH,"//button[text()='Point Me']");
#
# act=ActionChains(driver)
# act.move_to_element(Element).perform()
# Element=driver.find_element(By.XPATH,"//a[text()='Laptops']");
# # act.move_to_element(Element).double_click().perform()

# time.sleep(10)


print("----------select radio button_------")
# //label[text()='Male']

# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# Element=driver.find_element(By.XPATH,"//label[text()='Male']")
# or
# driver.find_element(By.XPATH,"//label[text()='Male']").click
#
# act=ActionChains(driver)
#
# act.click(Element).perform()
#
# time.sleep(10)
#
# print("----------select radio button_------")
#
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# Element=driver.find_element(By.XPATH,"//label[text()='Monday']")
# # or
# # driver.find_element(By.XPATH,"//label[text()='Male']").click()
#
# act=ActionChains(driver)
#
# act.click(Element).perform()
#
# time.sleep(10)



# print("----------dropdown------")
#
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# driver.find_element(By.XPATH,"//Select[@id='country']/option[@value='canada']").click()
#
# time.sleep(5)


# print("---------- Scroll dropdown------")
#
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# driver.find_element(By.XPATH,"//Select[@id='colors']/option[@value='yellow']").click()
#
# time.sleep(10)



# print("---------- Scroll dropdown animal------")
#
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# driver.find_element(By.XPATH,"//Select[@id='animals']/option[@value='cat']").click()
#
# time.sleep(5)



print("---------Calender 1------")

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()


driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
if True:
    driver.find_element(By.XPATH,"//span[text()='June']").click()
    driver.find_element(By.XPATH,"//span[text()='2025']").click()
    driver.find_element(By.XPATH,"//a[text()='18']").click()


time.sleep(10)