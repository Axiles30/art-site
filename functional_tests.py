from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class BasicInstallTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	def test_home_page_title(self):
		self.browser.get('http://127.0.0.1:0000')



if __name__ == '__main__':
	unittest.main()