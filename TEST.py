#Project goal: “BuyMe” website sanity test.
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\DevOps\\ChromeDriver.exe")
### Enter the Site
driver.get("https://buyme.co.il/")
driver.implicitly_wait(10)

### Open Login and registration window for user
driver.find_element_by_xpath("//div[2]/ul/li[5]/a").click()

### Not yet sighned
driver.find_element_by_xpath("//div/span").click()



### ENTER NAME, EMAIL, PASS,
driver.find_element_by_id("ember901").send_keys("GIL")
driver.find_element_by_id("ember902").send_keys("gil112@gmail.com")
driver.find_element_by_id("valPass").send_keys("123Abcde")
driver.find_element_by_id("ember904").send_keys("123Abcde")

time.sleep(3)

#driver.find_element_by_xpath("//*[@id='ember900']/div[5]/div/label").click()
driver.find_element_by_id("ember900").click()

driver.find_element_by_xpath("//*[@id='ember900']/button").click()
time.sleep(5)
###1
###2
###3
#driver.find_element_by_id("ember709").click()


######
#x = d##river.find_element_by_xpath("//*[@id='ember650_chosen']")
#x[2].## click()

#elements = driver.find_elements_by_name("btnK")
#print(elements)
