import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# xpath
driver.find_element(By.XPATH,"//input[contains(@placeholder,'User')]").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Password')]").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[contains(@type,'submit')]").click()
driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']").click()
driver.find_element(By.XPATH,"//button[@data-test='checkout']").click()


time.sleep(10)