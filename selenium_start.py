print("hi selenium")
from selenium import webdriver

# initialize brovser

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get('https://google.com')
driver.maximize_window()
# check url and page title


print(driver.current_url, driver.title)
driver.get('https://gmail.com')
print(driver.current_url, driver.title, )
driver.back()
print(driver.current_url, driver.title)
driver.refresh()

# driver close
driver.close()
driver.quit()
