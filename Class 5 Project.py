from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\DevOps\\ChromeDriver.exe")
driver.implicitly_wait(10) ##SECONDS

##THE PAGE
driver.get("https://translate.google.co.il/?hl=iw/")
print(driver.current_url)
print(driver.title)
