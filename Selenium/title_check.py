from selenium import webdriver

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size-=1920,1080")
driver = webdriver.Chrome(options=options)


driver.get("http://alchemy.hguy.co/orangehrm")


get_title = driver.title

expected_title = "OrangeHRM"

if get_title == expected_title:
    print('title matched')
elif get_title != expected_title:
    print('title not matched')

driver.quit()
