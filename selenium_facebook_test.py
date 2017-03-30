from selenium import webdriver
import os
import urllib2
import urllib
import subprocess
import pandas as pd
import requests
import csv
import xmllib
import cookielib 
import mechanize

url = "https://www.facebook.com/"
chromedriver = "/Users/fafaschiavo/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get(url)
print browser.page_source
browser.get('https://www.facebook.com/search/pages/?q=Aine')
print browser.page_source
# treePath_tag = browser.find_element_by_name("treePath")



# selenium.find_element_by_name("add_form").submit()



# username = selenium.find_element_by_id("username")
# password = selenium.find_element_by_id("password")

# username.send_keys("YourUsername")
# password.send_keys("Pa55worD")

# selenium.find_element_by_name("submit").click()