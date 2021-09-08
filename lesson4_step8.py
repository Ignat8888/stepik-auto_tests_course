from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time

URL = "http://suninjuly.github.io/explicit_wait2.html"

price_selector = "price"
submit_selector = "book"
price_value = "100"
x_selector = "input_value"
answer_selector = "answer"
solve_selector = "solve"

browser = webdriver.Chrome()
browser.get(URL)

def func(x):
	y = math.log(abs(12*math.sin(x)))
	return y


price_element = WebDriverWait(browser, 12).until(
					EC.text_to_be_present_in_element(
						(By.ID, price_selector), price_value
					)
				)

submit_element = WebDriverWait(browser, 3).until(
				 	EC.element_to_be_clickable(
				 		(By.ID, submit_selector)
				 	)
				 )				 
				 
submit_element.click()

x_element = browser.find_element(By.ID, x_selector)
x_value = int(x_element.text)

answer_element = browser.find_element(By.ID, answer_selector)
answer_element.send_keys(str(func(x_value)))

solve_element = browser.find_element(By.ID, solve_selector)
solve_element.click()



time.sleep(30)
browser.quit()
