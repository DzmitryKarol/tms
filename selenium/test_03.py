def test_driver(browser):
    full_name = 'dzmitry'
    email = 'dzmitry@gmail.com'
    current_address = 'Brest'
    permanent_adress = 'Minsk'
    browser.get("https://demoqa.com/text-box")
    full_name_field = browser.find_element_by_id('userName')
    email_field = browser.find_element_by_id('userEmail')
    current_address_field = browser.find_element_by_id('currentAddress')
    permanent_adress_field = browser.find_element_by_id('permanentAddress')
    submit_button = browser.find_element_by_id('submit')

    full_name_field.send_keys(full_name)
    email_field.send_keys(email)
    current_address_field.send_keys(current_address)
    permanent_adress_field.send_keys(permanent_adress)
    submit_button.click()

    result_name = browser.find_element_by_xpath('//p[@id="name"]').text.split(':')
    result_email = browser.find_element_by_xpath('//p[@id="email"]').text.split(':')
    result_current_address = browser.find_element_by_xpath('//p[@id="currentAddress"]').text.split(':')
    result_permanent_adress = browser.find_element_by_xpath('//p[@id="permanentAddress"]').text.split(':')


    assert full_name == result_name[1]
    assert email == result_email[1]
    assert current_address == result_current_address[1]
    assert permanent_adress == result_permanent_adress[1]

