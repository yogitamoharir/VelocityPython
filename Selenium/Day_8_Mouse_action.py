#Mouse Actions

# Ex1: Move To element

# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.flipkart.com/")
# time.sleep(2)
#
# loginElement=driver.find_element(By.XPATH,"//span[text()='Login']");
#
# act=ActionChains(driver)
# act.move_to_element(loginElement).perform()
#
# time.sleep(10)


# # Ex2: Handling of DropDown
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.flipkart.com/")
# time.sleep(2)
#
# loginElement=driver.find_element(By.XPATH,"//span[text()='Login']");
#
# act=ActionChains(driver)
# act.move_to_element(loginElement).perform()
# time.sleep(3)
#
# #click on Gift cards from dropdown
# driver.find_element(By.XPATH,"//li[text()='Gift Cards']").click();
#
# time.sleep(10)


# Ex3: Mouse Right click action

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)

cartElement=driver.find_element(By.XPATH,"//a[text()='Cart']");

act=ActionChains(driver)
# act.move_to_element(cartElement).perform()
# act.context_click().perform()

# act.move_to_element(cartElement).context_click().perform()

act.context_click(cartElement).perform()

time.sleep(10)

# Ex4: Mouse left click action

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)

cartElement=driver.find_element(By.XPATH,"//a[text()='Cart']")

act=ActionChains(driver)
# act.move_to_element(cartElement).perform()
# act.click().perform()

#act.move_to_element(cartElement).click().perform()

act.click(cartElement).perform()

time.sleep(10)


# Ex5: Mouse Double click

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(2)

Element=driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']");

act=ActionChains(driver)
#act.move_to_element(Element).perform()
# act.double_click().perform()

#act.move_to_element(Element).double_click().perform()

act.double_click(Element).perform()

time.sleep(10)


