from selenium import webdriver

facebook = "https://facebook.com"
login_button = ".//*[@id='u_0_y']"

driver = webdriver.Firefox()
driver.delete_all_cookies()


driver.get(facebook)

driver.find_element_by_xpath(".//input[contains(@value, 'Log')]").click() #обычный x-path  не сработал, потому что у фейсбука кнопка меняет ид


# driver.close()
