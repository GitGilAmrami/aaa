#Project goal: “BuyMe” website sanity test.

from selenium import webdriver

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
driver.find_element_by_id("ember902").send_keys("gil120@gmail.com")
driver.find_element_by_id("valPass").send_keys("123Abcde")
driver.find_element_by_id("ember904").send_keys("123Abcde")

time.sleep(3)
### //*[@id="ember900"]/div[5]/div/label
driver.find_element_by_xpath("//*[@id='ember900']/div[5]/div/label").click()
###SUBMIT LOGIN
driver.find_element_by_xpath("//*[@id='ember900']/button").click()

###PRICE
x = drSiver.find_elements_by_id("ember610")
x[2].click()
###AREA
x = driver.find_elements_by_id("ember617")
x[2].click()
###  PRODUCT TYPE
x = diver.find_elements_by_id("ember632")
x[2].click()



#<button type="submit" class="db fluid btn btn-theme">הרשמה ל-BUYME</button>

#<li   class="active-result" data-option-array-index="1"    style="">עד 99 ש"ח</li>

#< li class ="active-result" data-option-array-index="2" style="" > 100-199 ש"ח</li>
