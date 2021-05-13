import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements_by_css_selector('button.btn-add-to-basket')
    assert len(button) == 1, 'No such button on a page'
