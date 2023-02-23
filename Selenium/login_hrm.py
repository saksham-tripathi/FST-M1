from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--window-size-=1920,1080")
driver = webdriver.Chrome(options=options)

username = 'orange'
password = 'orangepassword123'

driver.get("http://alchemy.hguy.co/orangehrm")


driver.find_element("xpath", "//*[@id='txtUsername']").send_keys(username)

driver.find_element("xpath", "//*[@id='txtPassword']").send_keys(password)

driver.find_element("xpath", "//*[@id='btnLogin']").click()

if driver.find_element("xpath", "//*[@id='menu_dashboard_index']"):
    print('logged in')

driver.quit()
