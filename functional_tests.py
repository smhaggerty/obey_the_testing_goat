from selenium import webdriver

browser = webdriver.Firefox(executable_path = "/mnt/c/Users/Shane/Downloads/geckodriver-v0.18.0-win64/geckodriver.exe")
browser.get('http://localhost:8000')

assert 'Django' in browser.title
