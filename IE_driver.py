from selenium import webdriver

#initialize
ie_driver_path = "C:\Python35\Selenium_drivers\IEDriverServer.exe"
driver = webdriver.Ie(ie_driver_path)

facebook = 'https://facebook.com'
driver.get(facebook)
print(driver.title)

#close driver
# driver.close()
#driver.quit()