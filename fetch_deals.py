from selenium import webdriver
from selenium.webdriver.firefox.options import Options

deals = []
urls = [
    "https://forums.redflagdeals.com/hot-deals-f9/2/?c=9",
    "https://forums.redflagdeals.com/hot-deals-f9/?c=9"
]

# comment
driver = webdriver.PhantomJS(executable_path=r'./phantomjs.exe', service_args=['--ignore-ssl-errors=true', '--ssl-protocol=tslv1.0'])
driver.set_window_size(1920, 1080)

def get_deals(url):
    driver.get("https://forums.redflagdeals.com/hot-deals-f9/?c=9")
    elems = driver.find_elements_by_class_name("topic_title_link")
    for elem in elems:
        deals.append(elem.get_attribute("text"))

for i in urls:
    get_deals(i)

for i in deals:
    print(i)
driver.quit()


