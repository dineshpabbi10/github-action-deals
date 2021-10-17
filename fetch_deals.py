from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd

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

deals_df = pd.DataFrame({'deals':deals})

readme = open("Readme.md","w")
deals_df.to_markdown(readme)
readme.close()

driver.quit()


