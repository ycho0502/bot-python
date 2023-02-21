import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from pytz import timezone
import pytz
import random
import time

searchterms = [
    'Shared co working space near me',
    'coworking space Los Angeles',
    'meeting space Los Angeles',
    'business meeting rooms in LA',
    'i want to book a co working space'
]

def get_pst_time():
    date_format = '%m_%d_%Y_%H_%M_%S_%Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    pstDateTime = date.strftime(date_format)
    hour2 = [*pstDateTime][11]  # hour [0, 1, 2] are only options
    time.sleep(1800) #30 min
    if hour2 == 2:
        time.sleep(14400) #4 hours

def adclicker():
    x = random.randrange(0, len(searchterms))
    print(searchterms[x])

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.google.com/')
    time.sleep(1)
    search_input = driver.find_elements_by_css_selector('input.gLFyf.gsfi')[0] #goes to google search box
    search_input.send_keys(searchterms[x] + Keys.RETURN) #types in search term on google search box
    time.sleep(1)
    finalclick = driver.find_element_by_id('result-stats')
    time.sleep(1)

    action = ActionChains(driver)
    action.click(on_element=finalclick)
    action.send_keys(Keys.TAB) #selects link of first ad
    action.send_keys(Keys.RETURN) #clicks link of first ad
    action.perform()

    print(driver.title) #there should be a lot of scraping here with beautiful soup #################################

count = 0
while (count < 999999999999):
    adclicker();
    get_pst_time();

# https://www.geeksforgeeks.org/web-scraping-without-getting-blocked/
# https://www.geeksforgeeks.org/the-complete-guide-to-proxies-for-web-scraping/
# https://www.geeksforgeeks.org/get-contents-of-entire-page-using-selenium/?ref=rp
# https://www.geeksforgeeks.org/scrape-google-search-results-using-python-beautifulsoup/?ref=rp
# https://www.geeksforgeeks.org/scrape-and-save-table-data-in-csv-file-using-selenium-in-python/?ref=rp
# https://www.geeksforgeeks.org/how-to-take-screenshot-using-selenium-in-python/?ref=rp
