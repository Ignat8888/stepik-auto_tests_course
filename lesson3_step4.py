from selenium import webdriver
import time, math

URL = "http://suninjuly.github.io/alert_accept.html"
go_selector = "button[type='submit']"
x_selector = "#input_value"
input_selector = "#answer"
submButton_selector = "form button"

browser = webdriver.Chrome()
browser.get(URL)

def find(selector):
	element = browser.find_element_by_css_selector(selector)
	return element
	
def func(x):
	y = math.log(abs(12*math.sin(x)))
	return str(y)
	
go_element = find(go_selector)
go_element.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = find(x_selector)
x_value = int(x_element.text)
answer = func(x_value)

input_element = find(input_selector)
input_element.send_keys(answer)

submButton_element = find(submButton_selector)
submButton_element.click()

answerWindow = browser.switch_to.alert
answer2 = answerWindow.text
answerWindow.accept()

answer2 = answer2.split(":")
answer2 = answer2[1].strip()

print(answer2)

browser.quit()



