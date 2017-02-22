from selenium import webdriver
from selenium.webdriver.support.ui import Select

# setup
driver = webdriver.Firefox()  # init firefox
wait = driver.implicitly_wait(1)


driver.get("https://gmail.com")
driver.delete_cookie("google")
# wait
driver.find_element_by_css_selector("#link-signup>a").click()  # go to create account
button_present = driver.find_element_by_css_selector("input[id='submitbutton").is_displayed()

# find form elements & find form elements

if button_present:
	driver.find_element_by_css_selector("input[id='FirstName']").send_keys("Andrey")
	driver.find_element_by_css_selector("input[id='LastName").send_keys("KKKKK")
	driver.find_element_by_css_selector("input[id='GmailAddress").send_keys("FalfJack")
	driver.find_element_by_css_selector("input[id='Passwd").send_keys("123456789")
	driver.find_element_by_css_selector("input[id='PasswdAgain").send_keys("123456789")
	driver.find_element_by_css_selector("input[id='BirthDay").send_keys("27")
	driver.find_element_by_xpath(".//*[@id='BirthMonth']/div[1]").click()
	# wait
	driver.find_element_by_css_selector("div[id=':1']").click()
	driver.find_element_by_css_selector("input[id='BirthYear").send_keys("1977")
	driver.find_element_by_css_selector("input[id='RecoveryPhoneNumber").send_keys("0672450398")
	driver.find_element_by_css_selector("input[id='RecoveryEmailAddress").send_keys("paladine@ukr.net")
	driver.find_element_by_xpath(".//*[@id='Gender']/div[1]").click()
	driver.execute_script()

	wait

	driver.find_element_by_xpath(".//*[@id='CountryCode']/div[1]").click() #country dropdown
	wait
	Select(driver.find_element_by_xpath(".//*[@id=':q']/div")) #select country option
	# driver.find_element_by_css_selector("input[id='submitbutton").click()

else:
	wait

#
driver.close()
# driver.quit()

