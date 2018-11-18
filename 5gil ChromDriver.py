from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\DevOps\\ChromeDriver.exe")
driver.implicitly_wait(10) ##SECONDS

##THE PAGE
driver.get("https://translate.google.co.il/?hl=iw/")
print(driver.current_url)
print(driver.title)

#print(driver.page_source)

driver.refresh();
#driver.find_element_by_name("gt-submit")
#elements = driver.find_elements_by_name("btnK")
#print(elements)

#driver.find_elements(By.Xpath;("btnK")
#driver.find_element_by_id("firstBotton").click()

#button_element = driver.find_element_by_id("source")


#driver.find_element_by_id("source").send_keys("GGGGGG")

a = driver.find_element_by_xpath("//textarea[@id='source']").send_keys("GGGGGG")
if a.is_displayed()
    print ("TRUE")
#
time.sleep(5)
##driver.implicitly_wait(10)

x = driver.find_elements_by_id("gt-submit")
x[2].click()


driver.find_element(By.ID,value="123").send_keys(Keys.ENTER)

#driver.close();
# driver.quit();
