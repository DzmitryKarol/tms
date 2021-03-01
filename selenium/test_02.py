from selenium import webdriver
from time import sleep

def test_driver(browser):
    send_value = 78
    browser.get("http://the-internet.herokuapp.com/")
    element = browser.find_element_by_link_text('Inputs')
    sleep(3)
    element.click()
    page_head = browser.find_element_by_tag_name('h3').text
    assert "Inputs" == page_head
    input_field = browser.find_element_by_xpath("//input[@type='number']")
    input_field.send_keys(send_value)
    assert str(send_value) == input_field.get_attribute('value')

