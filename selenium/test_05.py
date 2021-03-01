from selenium.webdriver.common.by import By

# @pytest.fixture(scope='module')
def test_accept(browser):
    browser.get("https://www.testandquiz.com/selenium/testing.html")
    get_allert_button = browser.find_element(By.XPATH, '//button[text()="Generate Confirm Box"]').click()
    alert = browser.switch_to.alert
    print(f'allert text: {alert.text}')
    alert.accept()
    assert 'You pressed OK!' == browser.find_element(By.XPATH, '//*[@id="demo"]').text

# def test_cancell(browser):
#     browser.get("https://www.testandquiz.com/selenium/testing.html")
#     get_allert_button = browser.find_element(By.XPATH, '//button[text()="Generate Confirm Box"]').click()
#     alert = browser.switch_to.alert
#     alert.dismiss()
#     assert 'You pressed Cancel!' == browser.find_element(By.XPATH, '//*[@id="demo"]').text


