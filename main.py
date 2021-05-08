import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r"C:\Program Files\Chrome Driver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary)
driver.get("http://www.dubbedanime.vip")
assert "Anime" in driver.title
elem = driver.find_element_by_class_name("searcho")
elemInput = driver.find_element_by_class_name("nav-search")


print(elem.is_displayed())
elem.click()

elemInput.clear()
query='jujutsu'
elemInput.send_keys(query)
elemInput.send_keys(Keys.ENTER)
time.sleep(5)
links=driver.find_elements_by_class_name("poster-hover-layer")
print(links[1].get_attribute("href"))
for link in links :
    href=link.get_attribute('href')
    print(href[-3:])
    if query in href and href[-3:]!="dub":
        link.click()
        time.sleep(5)
        episodes=driver.find_elements_by_class_name("epi-me")
        #for episode in episodes:
        anchor=episodes[-1].find_element_by_css_selector("a")
        print(anchor.get_attribute("href"))
        anchor.click()
        time.sleep(5)
        iframe=driver.find_elements_by_tag_name("iframe")
        for i,frame in enumerate (iframe):
            driver.switch_to.frame(i)
            time.sleep(3)
            print(frame.is_displayed())
        # iframe.click()
        time.sleep(5)




#assert "No results found." not in driver.page_source
#driver.close()