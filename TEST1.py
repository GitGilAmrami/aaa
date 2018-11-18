from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\DevOps\\ChromeDriver.exe")
### Enter the Site
driver.get("https://buyme.co.il/")
driver.implicitly_wait(10)

#### Open Login and registration window for user
# driver.find_element_by_class_name("seperator-link").click()
#
# #HARSHAMA
# driver.find_element_by_xpath("//div/p/span").click()
# # PERSONAL DETAILS FOR HARSHAMA
# time.sleep(2)
# driver.find_element_by_id("ember973").send_keys("gil111")
# driver.find_element_by_id("ember975").send_keys("gil120@gmail.com")
# driver.find_element_by_id("valPass").send_keys("123Abcde")
# driver.find_element_by_id("ember979").send_keys("123Abcde")
#AGREE
time.sleep(5)
# driver.find_element_by_id("ember980").click()
###SUBMIT LOGIN
# driver.find_element_by_xpath("//*[@id='ember900']/button").click()
# time.sleep(2)
##CHOOSE AMOUNT
driver.find_element_by_class_name("chosen-single").click()
time.sleep(2)
#driver.find_element_by_css_selector("select#ember663 > option[value='2']").click()
##CHOOSE AREA
##CHOOSE CATEGORY
##FIND ME RESULTS
#<a class="chosen-single" tabindex="-1"><span>סכום</span><div><b></b></div></a>


