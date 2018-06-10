from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_feature(context, feature):
    chrome_options = Options()
    if 'headless' in context.tags:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1024,768")
    context.browser = webdriver.Chrome(
        chrome_options=chrome_options,
        executable_path="/home/sinan/Downloads/selenium/chromedriver")
        # C:\Users\sinan\Downloads\chromedriver_win32_2.0\chromedriver.exe
    context.browser.implicitly_wait(3)


    """ Kullanacağımız değişkenleri setleyelim. """
    context.STOREFRONT = {
        "homepage": "https://www.hepsiburada.com",
        "cart":     "/ayagina-gelsin/sepetim",
        "login":    "/ayagina-gelsin/giris"
    }

    context.CATEGORIES = {
        "uzaktan_kumanda": "/uzaktan-kumandali-arabalar-c-14001244"
    }

    context.LOGIN_INFO = {
        "mail":     "test@guerrillamail.com",
        "password": "test112233"
    }

def after_feature(context, scenario):
    context.browser.quit()
