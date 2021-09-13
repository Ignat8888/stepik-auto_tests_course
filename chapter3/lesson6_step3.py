import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time


@pytest.fixture(scope="function")
def browser():
	browser = webdriver.Chrome()
	yield browser
	print(TestStepik.corr_answer)
#	time.sleep(4)
	browser.quit()
	

class TestStepik():

	URLS = ["https://stepik.org/lesson/236895/step/1",
			"https://stepik.org/lesson/236896/step/1",
			"https://stepik.org/lesson/236897/step/1",
			"https://stepik.org/lesson/236898/step/1",
			"https://stepik.org/lesson/236899/step/1",
			"https://stepik.org/lesson/236903/step/1",
			"https://stepik.org/lesson/236904/step/1",
			"https://stepik.org/lesson/236905/step/1"]
	
	answer_selector = "textarea"
	submitBtn_selector = "submit-submission"
	correct_selector = "div pre"

	def func(self):
		answer = math.log(int(time.time()))
		return answer

	@pytest.mark.parametrize('URL', URLS)
	def test_site(self, browser, URL):
		browser.get(URL)
		
		answer_element = WebDriverWait(browser, 10).until(
				EC.element_to_be_clickable((By.TAG_NAME, self.answer_selector))
												   )
		answer_element.send_keys(str(self.func()))
		
		submitBtn_element = WebDriverWait(browser, 10).until(
				EC.element_to_be_clickable((By.CLASS_NAME, self.submitBtn_selector))
												      )
		
		submitBtn_element.click()
		
		correct_element = WebDriverWait(browser, 10).until(
				EC.visibility_of_element_located((By.CSS_SELECTOR, self.correct_selector))
												     )
		assert correct_element.text == "Correct!"
		
		
		
		
		
		
		
		
		
		
