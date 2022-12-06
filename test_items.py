import time

from selenium.webdriver.common.by import By


### pytest --language=es test_items.py


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_has_specific_text(browser):
    browser.get(link)
    # time.sleep(5)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text == "Añadir al carrito"
