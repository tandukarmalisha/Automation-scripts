from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

title = driver.title

time.sleep(1)

if "Google" in title:
    print("Test passed")
else:
    print("Test failed")


driver.quit()