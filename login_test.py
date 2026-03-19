from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

  
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)

message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in message:
    print("login test passed")
else: 
    print("login test failed")


driver.quit()