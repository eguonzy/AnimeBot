import time
import re
import requests
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
query = 'jujutsu'
print(f"Loading query {query}")
elemInput.send_keys(query)
print(f"Searching for {query}")
elemInput.send_keys(Keys.ENTER)
time.sleep(5)
links = driver.find_elements_by_class_name("poster-hover-layer")
print(f"{len(links)} results found")
for link in links:
    href = link.get_attribute('href')
    if query in href and href[-3:] != "dub":
        link.click()
        time.sleep(5)
        tags = driver.find_elements_by_class_name("epi-me")
        episodes = [{'url': x.find_element_by_tag_name("a").get_attribute("href"),
                     "title": x.find_element_by_tag_name("a").find_element_by_class_name("name").get_attribute("title")} for x in tags]
        print(episodes)
        for episode in episodes:
            print(f"Getttin link of {episode['title']}")
            driver.get(episode['url'])
            time.sleep(5)
            iframe = driver.find_elements_by_tag_name("iframe")
            url = iframe[1].get_attribute('src')
            downloadUrl = f"https://gogo-stream.com/download?id={url[url.index('id=') + 3:]}&refer=none"
            driver.get(downloadUrl)
            driver.maximize_window()
            input = driver.find_elements_by_tag_name("a")
            for a in input:
                if '360P' in a.text:
                    print( f"{episode['title']}::=> {a.get_attribute('href')}")
        # time.sleep(3)
        # input.click()

        # with open("frame.mp4",'wb') as file:
        #     for chunk in r.iter_content(chunk_size=chunkSize):
        #
        #       file.write(chunk)
        # for i,frame in enumerate (iframe):
        #     driver.switch_to.frame(i )
        #     time.sleep(3)
        #     print( frame.is_displayed(),True)
        # iframe.click()
        break


# assert "No results found." not in driver.page_source
# driver.close()
