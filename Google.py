import selenium.webdriver as webdriver
from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox')
url = "https://www.google.com"
browser = webdriver.Firefox(firefox_binary=binary)
browser.get(url)

def get_results(search_terms, max_links):
    MAX_LINKS = max_links   # Set the maximum number of links to gather
    results = []

    # Search the first key
    for search_term in search_terms:

        search_bx = browser.find_element_by_class_name('gsfi')
        search_bx.clear()
        search_bx.send_keys(search_term)
        search_bx.submit()
        sleep(1)

        try:
            # links = browser.find_elements_by_class_name('_Rm')
            links = browser.find_elements_by_xpath('//div//h3//a')
        except:
            print("error")

       # retrieves links
        print("For: " + search_term)
        for link in links[0:MAX_LINKS]:
            # href = link.get_property('text')
            # href = link.get_attribute('data-href')
            href = link.get_attribute('href')
            results.append(href)
            print(href)
    browser.close()

    # print(results)
    return results

# get_results("MARKUS EDINGER GERMANY")
