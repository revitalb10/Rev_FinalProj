from selenium import webdriver

SITE = "http://192.168.99.100:5000/"


# Use chrome as browser
driver = webdriver.Chrome("C:\\Users\Revital\Downloads\chromedriver_win32\chromedriver.exe")

driver.get(SITE)
driver.implicitly_wait(20)

content = driver.find_element_by_xpath("/html/body").text
print(content)



