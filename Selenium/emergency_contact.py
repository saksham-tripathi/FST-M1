from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--window-size-=1920,1080")
driver = webdriver.Chrome(options=options)

username = 'orange'
password = 'orangepassword123'

driver.get("http://alchemy.hguy.co/orangehrm")


driver.find_element("xpath", "//*[@id='txtUsername']").send_keys(username)

driver.find_element("xpath", "//*[@id='txtPassword']").send_keys(password)

driver.find_element("xpath", "//*[@id='btnLogin']").click()

driver.find_element("xpath", "//*[@id='menu_pim_viewMyDetails']").click()


driver.find_element("xpath", "//*[@id='sidenav']/li[9]/a").click()

driver.find_element("xpath", "//*[@id='sidenav']/li[3]/a").click()

print(driver.find_element("xpath", "//*[@id='emgcontact_list']/tbody").text)

print('details printed')

driver.quit()
