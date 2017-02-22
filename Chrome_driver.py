from selenium import webdriver

#initialize
chrome_driver_path = "C:\Python35\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

facebook = 'https://facebook.com'
driver.get(facebook)
print(driver.title)

#close driver
driver.close()
#driver.quit()

