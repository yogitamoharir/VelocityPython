# Ex1: Capture Screenshot of complete webpage
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.save_screenshot("C:\\Users\\Tushar\\PycharmProjects\\VelocityPython\\Selenium\\fb.png")
time.sleep(5)

# Ex2: Capture a Screenshot of specific element in a webpage
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//img[@class='fb_logo _8ilh img']").screenshot("C:\\Users\\Tushar\\PycharmProjects\\VelocityPython\\Selenium\\facebook.png")