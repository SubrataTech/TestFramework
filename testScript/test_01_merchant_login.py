import unittest, re, time
from selenium import webdriver
import sys
sys.path.append("..")

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from library.DataHandling import excel_handling, userName, password, cell_length
from library.ConstantsVariables import ConstantsVariables
import unittest, re, time




class Merchant_Login(unittest.TestCase):

	def setUp(self):
		self.longMessage = True
		# self.driver = webdriver.Firefox()
		# self.driver = webdriver.Chrome(ConstantsVariables())
		cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = False
		self.driver = webdriver.Firefox(capabilities=cap, executable_path=ConstantsVariables())

		#
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_2_Login_with_wrong_Password(self):
		driver = self.driver
		driver.maximize_window()
		driver.implicitly_wait(10)
		x = excel_handling(4, 1, 'Sheet1', '../data/test_data.xlsx')
		print("data : ", x)
		driver.get("https://merchants.mypoolin.com/")

		driver.find_element_by_xpath("//input[@id='user']").send_keys(
			excel_handling(4, 1, 'Sheet1', '../data/test_data.xlsx'))  # Row num, Col Num, Sheet Name, Excel File Name
		time.sleep(3)
		driver.find_element_by_xpath("//input[@id='pwd']").send_keys(
			excel_handling(4, 2, 'Sheet1', '../data/test_data.xlsx'))  # Row num, Col Num, Sheet Name, Excel File Name

		time.sleep(3)
		driver.find_element_by_xpath("//button[@id='login']").click()
		TextElement = driver.find_element_by_xpath("//body[text()='Username or password incorrect']")
		system_Date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
		driver.get_screenshot_as_file('../ScreenShots/test_Valid_Login-%s.png' % system_Date)
		self.assertEqual(TextElement.text, 'Username or password incorrect',
		                 msg="Test Case Failed: Webelement is not matching")
		time.sleep(3)

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e:
			return False
		return True

	def is_alert_present(self):
		try:
			self.driver.switch_to_alert()
		except NoAlertPresentException as e:
			return False
		return True

	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally:
			self.accept_next_alert = True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
	unittest.main()
