from selenium import webdriver
import time

driver = webdriver.Firefox()

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")

url = "http://github.com/turanozt0"
driver.get(url)

print(driver.title)

if "turanozt0" in driver.title:
    driver.save_screenshot("github-sadikturan.png")

time.sleep(2)

driver.back()
# driver.forward()

time.sleep(2)

#driver.close()

