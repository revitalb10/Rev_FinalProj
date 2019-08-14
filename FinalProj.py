from selenium import webdriver
import re

SITE = "http://192.168.99.100:5000/"

# Use chrome as browser
driver = webdriver.Chrome("C:\\Users\Revital\Downloads\chromedriver_win32\chromedriver.exe")
# Open Site
driver.get(SITE)
driver.implicitly_wait(20)
#find string
content = driver.find_element_by_xpath("/html/body").text

#remove World from print
string = re.sub('World', '', content)
print(string)



