Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> from selenium import webdriver
... from selenium.webdriver.common.by import By
... 
... driver = webdriver.Firefox()
... driver.maximize_window()
... 
... driver.get("https://magento.softwaretestingboard.com/")
... 
