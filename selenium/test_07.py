from selenium.webdriver.common.by import By


def test_check_new_tab(browser):
    browser.get("http://demo.guru99.com/test/guru99home/")
    browser.switch_to.frame(browser.find_element(By.XPATH, '//iframe[@id="a077aa5e"]'))
    link = browser.find_element(By.XPATH, '//a')
    link.click()
    main_window = browser.current_window_handle
    new_window = [window for window in browser.window_handles if window != main_window][0]
    browser.switch_to.window(new_window)
    assert 'Selenium Live Project: FREE Real Time Project for Practice' == browser.find_element(By.XPATH, "//*[@id ='g-mainbar']//h1").text
