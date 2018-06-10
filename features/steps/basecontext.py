import datetime
import time
from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_category_url(context, category_name):
    return context.STOREFRONT["homepage"] + context.CATEGORIES[category_name]

def get_storefront_url(context, name):
    if name == "homepage":
        return context.STOREFRONT["homepage"]
    else:
        return context.STOREFRONT["homepage"] + context.STOREFRONT[name]

def get_login_info(context, info):
    return context.LOGIN_INFO[info]

def wait_for_text(context):
    text_present = EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'body'),"Hepsiburada.com, Bir Doğan Online Markasıdır.")
    WebDriverWait(context.browser, 5).until(text_present)

def wait_ajax_complete(context):
    WebDriverWait(context.browser, 10).until(lambda driver: driver.execute_script("return jQuery.active === 0"))

def visit(context, location=''):
    context.browser.get(location)
    wait_for_text(context)

@then('Ekran görüntüsü almalıyım.')
def save_screenshot(context, filename = str(datetime.datetime.now()).split('.')[0]):
    context.browser.save_screenshot("./features/" + filename + ".png")

@given('Anasayfaya gittiğimde')
def step_i_am_on_home_page(context):
    visit(context, get_storefront_url(context,"homepage"))

@when('Üye girişi yaptığımda')
def step_login(context):
    visit(context, get_storefront_url(context,"login"))
    emailField = context.browser.find_element_by_id("email")
    emailField.send_keys(get_login_info(context,"mail"))
    passwordField = context.browser.find_element_by_id("password")
    passwordField.send_keys(get_login_info(context,"password"))
    loginButton = context.browser.find_element_by_css_selector("#form-login > div.form-actions > button")
    loginButton.click()

@then('Başarıyla giriş yaptığımı görmeliyim.')
def step_success_login(context):
    wait_for_text(context)
    text_present = EC.text_to_be_present_in_element((By.ID, 'MyAccount'),"Hesabım")
    WebDriverWait(context.browser, 10).until(text_present)
    #assert "Hesabım" in context.browser.find_element_by_id("MyAccount").text, "Hesabım metni sağ üstteki myaccount classında yok."

@given('Sitede "{category_name}" kategorisine gidersem')
def step_i_am_on_category(context, category_name):
    visit(context, get_category_url(context, category_name))

@when('Sonuçlar içerisinden ilk ürüne tıkladığımda')
def step_click_first_product(context):
    context.browser.find_element_by_css_selector('.SearchListing > div > div > ul > li:nth-child(1)').click()

@when('Ürün detayındaki sepete ekle butonuna tıkladığımda')
def step_click_addtocart(context):
    context.browser.find_element_by_id('addToCart').click()

@then('Sepette "{quantity}" ürün olduğunu görmeliyim.')
def step_check_quantity_in_cart(context, quantity):
    visit(context, get_storefront_url(context,"cart"))
    assert context.browser.find_element_by_css_selector('#short-summary > div.box-content  > h2').text == "Sipariş Özeti", "Sipariş Özeti metni bulunamadı."
    quantity_text = context.browser.find_element_by_xpath('//*[@id="short-summary"]/div[1]/p/span').text
    assert quantity_text == quantity + " ürün", "Sepette '{} ürün' değil, '{}' var.".format(quantity,quantity_text)

@then('Sayfada "{contain_text}" metnini görmeliyim.')
def step_page_source_contain_text(context, contain_text):
    bodyText = context.browser.find_element_by_tag_name("body").text
    assert contain_text in str(bodyText), "Sayfa kaynağında '{}' metni yok.".format(contain_text)

@when('Sitede "{phrase}" araması yaptığımda')
def step_search(context, phrase):
    search_input = context.browser.find_element_by_name('q')
    search_input.send_keys(phrase + Keys.RETURN)

@then('En az "{mp_quantity}" adet satıcı görmeliyim.')
def step_check_marketplace(context, mp_quantity):
    mp_div = context.browser.find_element_by_css_selector('div.marketplace-list > table > tbody')
    assert len(mp_div.find_elements_by_xpath('//tr')) >= int(mp_quantity)

@given('Sayfada "{match}" sıradaki tedarikçiden ürünü sepete atarsam')
@when('Sayfada "{match}" sıradaki tedarikçiden ürünü sepete atarsam')
def step_match_merchant(context, match):
    match = match.replace(".","")
    mp_div = context.browser.find_element_by_css_selector('div.marketplace-list > table > tbody > tr:nth-child('+ match +') > td.form-area > div')
    mp_div.click()

@when('Alışverişe devam et butonuna tıkladığımda')
def step_click_continue_shopping(context):
    context.browser.find_element_by_css_selector("#cart-container > section > div.box.umbrella > div > a").click()

@when('Sepetimdeki tüm ürünleri sildiğimde')
def delete_products_on_cart(context):
    visit(context, get_storefront_url(context,"cart"))
    cart_items = context.browser.find_elements_by_css_selector("#form-item-list > ul > li")
    for i in range(len(cart_items),0,-1):
        context.browser.find_element_by_css_selector("#form-item-list > ul > li:nth-child("+ str(i) +") > div > div.product-detail > div.utils > a.btn-delete").click()
        wait_ajax_complete(context)