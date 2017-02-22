# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest


class FacebookTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "https://www.facebook.com/"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_facebook(self):
		driver = self.driver
		driver.find_element_by_id("u_0_1").send_keys("dfdsf")
		driver.find_element_by_id("u_0_6").send_keys("dsfsdf")
		driver.find_element_by_id("u_0_3").send_keys("sdfsdf")
		driver.find_element_by_id("u_0_9").send_keys("sdfsdf")
		driver.find_element_by_id("u_0_d").send_keys("sdfsdf")
		Select(driver.find_element_by_id("month")).select_by_visible_text("Jan")
		Select(driver.find_element_by_id("day")).select_by_visible_text("1")
		Select(driver.find_element_by_id("year")).select_by_visible_text("2017")
		driver.find_element_by_xpath("//div[@id='reg_form_box']/div[9]/button").click()

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e:
			return False
		return True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
	unittest.main()
