from selenium import webdriver


def change_proxy_in_chrome():

    PROXY = "23.23.23.23:3128" # IP:PORT or HOST:PORT

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)

    chrome = webdriver.Chrome(options=chrome_options)
    chrome.get("http://whatismyipaddress.com")