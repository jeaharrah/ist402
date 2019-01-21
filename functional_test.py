from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary, executable_path='virtualenv\\Scripts\\geckodriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
