from selenium.webdriver.common.by import By
from time import sleep

def test_check_new_tab(browser):
    browser.get("http://the-internet.herokuapp.com/windows")
    link = browser.find_element(By.XPATH, "//a[text()='Click Here']")
    main_window = browser.current_window_handle
    link.click()
    sleep(5)
    new_window = [window for window in browser.window_handles if window != main_window][0]
    browser.switch_to.window(new_window)
    assert 'New Window' == browser.find_element(By.XPATH, "//h3").text

