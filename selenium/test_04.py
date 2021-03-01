from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_driver(browser):
    browser.get("https://ultimateqa.com/sample-application-lifecycle-sprint-3/")
    gender = browser.find_element(By.XPATH, '//input[@name="gender" and @value="male"]').click()
    first_name_field = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    first_name_field.send_keys("dzmitry")
    last_name_field = browser.find_element(By.XPATH, '//input[@name="lastname"]')
    last_name_field.send_keys("karol")
    submit_button = browser.find_element(By.XPATH, '//input[@type="submit"]')
    submit_button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH,'//div[@class="et_pb_text_inner"]//span')))

    assert_text = browser.find_element(By.XPATH, '//div[@class="et_pb_text_inner"]//span').text
    assert "Master test Automation, Faster.".upper() == assert_text


