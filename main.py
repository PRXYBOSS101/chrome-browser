from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://smart.shre.su/v1/99182c8df1171d5cb8bac92eb5512d66?deeplink=deeplink")
input("Press enter to exit ;)")
