URL = "https://stepik.org/lesson/25969/step/8"

def test_con(browser):

	browser.get(URL)
	browser.find_element_by_css_selector("#ember213")
