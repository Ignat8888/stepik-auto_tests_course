from selenium import webdriver
import time, math

URL = "http://suninjuly.github.io/redirect_accept.html"

flyButton_selector = "form button"
x_selector = "#input_value"
answer_selector = "#answer"
submit_selector = "form button"

browser = webdriver.Chrome()
browser.get(URL)

def find(selector):
	element = browser.find_element_by_css_selector(selector)
	return element
	
def func(x):
	y = math.log(abs(12*math.sin(int(x))))
	return y
	
flyButton_element = find(flyButton_selector)
flyButton_element.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = find(x_selector)
x_value = x_element.text

answer_element = find(answer_selector)
answer_value = str(func(x_value))
answer_element.send_keys(answer_value)

submit_element = find(submit_selector)
submit_element.click()

answerWindow = browser.switch_to.alert
answer2 = answerWindow.text
answerWindow.accept()

answer2 = answer2.split(":")
answer2 = answer2[1].strip()

print(answer2)

time.sleep(3)
browser.quit()
