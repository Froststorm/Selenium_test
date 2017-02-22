from selenium import webdriver

driver = webdriver.Firefox()

url = 'http://facebook.com'
firstname ='Andrii'
lastname = 'Kulikovskiy'
email = 'Kulikovskiy@Kulikovskiy.com'
password = "password"
driver.get(url)

#faceboog registration
driver.find_element_by_name('firstname').send_keys(firstname)
driver.find_element_by_name('lastname').send_keys(lastname)
driver.find_element_by_name('reg_email__').send_keys(email)
driver.find_element_by_name('reg_email_confirmation__').send_keys(email)
driver.find_element_by_name('reg_passwd__').send_keys('password')
driver.find_element_by_link_text('Forgot account?').click()


# driver.close()
# driver.quit()
