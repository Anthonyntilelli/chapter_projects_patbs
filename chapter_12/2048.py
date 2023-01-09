#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://play2048.co/")
print("Browser Loaded")
element = browser.find_element(By.TAG_NAME, "body")
for i in range(100):
    print("sending up")
    element.send_keys(Keys.UP)
    print("sending right")
    element.send_keys(Keys.RIGHT)
    print("sending down")
    element.send_keys(Keys.DOWN)
    print("sending left")
    element.send_keys(Keys.LEFT)

input("Press enter to close browser.")
browser.quit()