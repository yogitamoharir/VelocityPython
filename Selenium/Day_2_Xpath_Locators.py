"""
Locators

Locators are used to identify an element present in a webpage

Types of locators
1-Tagname
2-ID
3-Name
4-ClassName
5-LinkText
6-PartialLinkText
7-CSS
8-XPath

XPath locator type
To use XPath we need to find XPath expression
Different ways to create XPath expression

1: Xpath by Attribute  → //tagname[@AttributeName=’AttributeValue’]
2: Xpath by Text         —> //tagname[text()=’textValue’]
3: Xpath by Contains
			Attribute ->   //tag[contains(@attributeName,’partial attribute value’)]
			Text->         //tag[contains(text(),’partial text value’)]
4: Xpath by index
5: Absolute Xpath
	Use to navigate from parent to immediate child
	We can achieve absolute using /

6: Relative Xpath
	Use to navigate from parent to any child
	We can achieve absolute using //

Absolute xpath:
UN: /html/body/div[1]/input[1]
contact: /html/body/div[2]/input[3]
login: /html/body/div[3]/button

Relative Xpath:
UN: //div[1]//input[1] or //div[1]/input[1]
contact: //div[2]//input[3] or //div[2]/input[3]
login: //button

"""

# EX1: Xpath By Attribute

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# time.sleep(2)
# # driver.find_element(Locator)
# #driver.find_element(By.XPATH,"Xpath Expression")
# driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc@gmail.com")
# driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy _9npi']").send_keys("nsdfhf9rr32r")
# driver.find_element(By.XPATH,"//button[@name='login']").click()

# # EX2: Xpath by Text
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# time.sleep(4)
#
# # # click on forgotten pwd link
# # driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").click()
#
# # click on Create New Acc link
# driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
#
# time.sleep(4)

# # EX3: Xpath by contains Attribute
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[contains(@placeholder,'address or phone')]").send_keys("abc@gmail.com")
# driver.find_element(By.XPATH, "//input[contains(@class,'_6luy _9npi')]").send_keys("nsdfhf9rr32r")
# driver.find_element(By.XPATH, "//button[contains(@class,'4jy1 selected _51sy')]").click()
#
# time.sleep(4)

# # EX4: XPath by contains Text
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# time.sleep(2)
#
# # #click on forgotten pwd link
# # driver.find_element(By.XPATH,"//a[contains(text(),'password')]").click()
#
# # click on create new acc link
# driver.find_element(By.XPATH, "//a[contains(text(),'Create new')]").click()
#
# time.sleep(4)

# # EX5: Xpath by index
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# time.sleep(2)
#
# # click on create new acc link
# driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
#
# time.sleep(3)
# # Enter FN
# driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("abc")
#
# # Enter LN
# driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("xyz")
#
# # Enter mobile num
# driver.find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys("999999999")
#
# time.sleep(10)


# 1: Tagname Locator Type:
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/Velocity/Selenium/AllHtml.html")
time.sleep(2)

# Enter FN
driver.find_element(By.TAG_NAME, "input").send_keys("abc")
# Enter LN
driver.find_element(By.TAG_NAME, "input").send_keys("xyz")
time.sleep(15)

# 2: ID Locator Type:

driver = webdriver.Chrome()
driver.get("file:///D:/Velocity/Selenium/AllHtml.html")
time.sleep(2)

# Enter FN
driver.find_element(By.ID, "123").send_keys("abc")
# Enter LN
driver.find_element(By.ID, "345").send_keys("xyz")
time.sleep(15)


# 3: Name Locator Type
driver = webdriver.Chrome()
driver.get("file:///D:/Velocity/Selenium/AllHtml.html")
time.sleep(2)

# Enter FN
driver.find_element(By.NAME, "abc123").send_keys("abc")
# Enter LN
driver.find_element(By.NAME, "abc124").send_keys("xyz")
time.sleep(15)

# 4: ClassName Locator Type

driver = webdriver.Chrome()
driver.get("file:///D:/Velocity/Selenium/AllHtml.html")
time.sleep(2)

# Enter FN
driver.find_element(By.CLASS_NAME, "xyz456").send_keys("abc")
# Enter LN
driver.find_element(By.CLASS_NAME, "xyz123").send_keys("xyz")
time.sleep(15)


# 5: LinkText & PartialText

driver = webdriver.Chrome()
driver.get("file:///D:/Velocity/Selenium/AllHtml.html")
time.sleep(2)

# click on facebook link
# driver.find_element(By.LINK_TEXT,"facebook").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "book").click()

time.sleep(5)

# When Text value is duplicate
# When Text is not present for that element





