from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from excelParam import userName, password
import unittest, re, time


class Merchant_logout(unittest.TestCase):

	def setUp(self):
		self.longMessage = True
		self.driver = webdriver.Firefox()
		# self.driver = webdriver.Chrome()

		self.verificationErrors = []
		self.accept_next_alert = True

	def test_Case_logout(self):
		driver = self.driver
		driver.maximize_window()
		driver.get("https://stackoverflow.com/")
		# driver.find_element_by_xpath("//input[@id='user']").send_keys(
		# 	userName(3, 1, 'Sheet1', './test.xlsx'))  # Row num, Col Num, Sheet Name, Excel File Name
		# driver.find_element_by_xpath("//input[@id='pwd']").send_keys(
		# 	password(3, 2, 'Sheet1', './test.xlsx'))  # Row num, Col Num, Sheet Name, Excel File Name
		# driver.find_element_by_xpath("//button[@id='login']").click()
		# driver.find_element_by_xpath("//a[@href='/logout']").click()
		# login_Btn = driver.find_element_by_xpath("//b[text()='Your Merchant Login']")
		system_Date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
		driver.get_screenshot_as_file('ScreenShots/test_Valid_Login-%s.png' % system_Date)
		# self.assertEqual(login_Btn.text, 'Your Merchant Login', msg="Test Case Failed: Webelement is not matching")

	# def is_element_present(self, how, what):
	# 	try:
	# 		self.driver.find_element(by=how, value=what)
	# 	except NoSuchElementException as e:
	# 		return False
	# 	return True
	#
	# def is_alert_present(self):
	# 	try:
	# 		self.driver.switch_to_alert()
	# 	except NoAlertPresentException as e:
	# 		return False
	# 	return True
	#
	# def close_alert_and_get_its_text(self):
	# 	try:
	# 		alert = self.driver.switch_to_alert()
	# 		alert_text = alert.text
	# 		if self.accept_next_alert:
	# 			alert.accept()
	# 		else:
	# 			alert.dismiss()
	# 		return alert_text
	# 	finally:
	# 		self.accept_next_alert = True
	#
	# def tearDown(self):
	# 	self.driver.quit()
	# 	self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
	unittest.main()
