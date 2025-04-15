from selenium import webdriver
import time

# WebDriver class Methods and Browser command
#
# Use to perform action on browser
#
# get: use to enter URL in browser or use to open an application
# get(url)
#
# close: use to close current tab of the browser
# driver.close()
#
# quit: use to close current tab of the browser
# driver.quit()
#
# title: use to get title of the application
# driver.title
#
# Current_url: use to get current url of the application
# driver.current_url
# driver.back()
# driver.forward()
# driver.fullscreen_window()
# driver.refresh()


#Open Browser
driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.google.com/")

#get Title
actTitle=driver.title
print(actTitle)
if actTitle=="Google":
    print("Pass")
else:
    print("Fail")

print(driver.title)


#get Current URL
actURL=driver.current_url
print(actURL)

#close Browser
# driver.close()
# driver.quit()


#Ex 2
driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.google.com/")
driver.get("https://www.Facebook.com/")
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.fullscreen_window()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)