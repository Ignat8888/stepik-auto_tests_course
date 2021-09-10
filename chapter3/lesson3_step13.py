import unittest
from selenium import webdriver
import time


class TestTextInSite (unittest.TestCase):
	url_old = "http://suninjuly.github.io/registration1.html"
	url_new = "http://suninjuly.github.io/registration2.html"
	
	def test_old(self):
		browser = webdriver.Chrome()
		browser.get(self.url_old)
		firstName_locator = ".first_block .first"
		firstName = browser.find_element_by_css_selector(firstName_locator)
		firstName.send_keys("test")
		
		lastName_locator = ".first_block .second"
		lastName = browser.find_element_by_css_selector(lastName_locator)
		lastName.send_keys("test")
		
		email_locator = ".first_block .third"
		email = browser.find_element_by_css_selector(email_locator)
		email.send_keys("test")
		
		button_locator = ".btn-default"
		button = browser.find_element_by_css_selector(button_locator)
		button.click()
		
		time.sleep(1)
		
		welcome_elem_locator = "h1 "
		welcome_elem = browser.find_element_by_css_selector(welcome_elem_locator)
		welcome_elem_text = welcome_elem.text
		
		self.assertEqual(welcome_elem_text, \
		"Congratulations! You have successfully registered!", \
		"Error!!! Text not found!")

		
	def test_new(self):
		browser = webdriver.Chrome()
		browser.get(self.url_new)
		firstName_locator = ".first_block .first"
		firstName = browser.find_element_by_css_selector(firstName_locator)
		firstName.send_keys("test")
		
		lastName_locator = ".first_block .second"
		lastName = browser.find_element_by_css_selector(lastName_locator)
		lastName.send_keys("test")
		
		email_locator = ".first_block .third"
		email = browser.find_element_by_css_selector(email_locator)
		email.send_keys("test")
		
		button_locator = ".btn-default"
		button = browser.find_element_by_css_selector(button_locator)
		button.click()
		
		time.sleep(1)
		
		welcome_elem_locator = "h1 "
		welcome_elem = browser.find_element_by_css_selector(welcome_elem_locator)
		welcome_elem_text = welcome_elem.text
		
		self.assertEqual(welcome_elem_text, \
		"Congratulations! You have successfully registered!", \
		"Error!!! Text not found!")
	

if __name__ == "__main__":
	unittest.main()
