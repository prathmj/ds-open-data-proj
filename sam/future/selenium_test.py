#!/usr/bin/env python2.7

import os
from selenium import webdriver

os.environ["webdriver.chrome.driver"] = "./chromedriver"

driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.google.com")
driver.quit
