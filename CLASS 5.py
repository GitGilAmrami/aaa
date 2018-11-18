###CLASS 5

#1.
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\DevOps\\ChromeDriver.exe")
driver.get("https://www.walla.co.il/")
#driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\DevOps\\geckodriver.exe")
driver.get("http://www.ynet.co.il")

driver.implicitly_wait(10)
#print(driver.current_url)

#2.
#a.
print(driver.title)
web_name = driver.title

#b.
driver.refresh()
#c.
if web_name==driver.title:
    print("The Same:",web_name)

#3.
# locators are the same in all browsers

#4.
driver.get("https://translate.google.com/")
driver.find_element_by_id("sugg-item-iw").click()
driver.find_element_by_id("sugg-item-iw").click()
driver.find_element_by_id("source").send_keys("דפדפן")
driver.find_element_by_id("gt-submit").click()

#5.
driver.get("https://www.youtube.com/")
driver.find_element_by_id("search").send_keys("The wall")
driver.find_element_by_id("search-icon-legacy").click()

#6.
driver.get("https://translate.google.com/")
a = driver.find_element_by_id("gt-submit")
print("a",a)
b = driver.find_element_by_class_name("jfk-button")
print("b",b)
# WHY DOES IT BRING ...SyntaxError: invalid syntax ?
c = driver.find_element_by_xpath("//*[@id='gt-submit']")
print("c",c)

#7.
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("gilamrami@gmail.com")
driver.find_element_by_id("pass").send_keys("12345")
driver.find_element_by_id("loginbutton").click()