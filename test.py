from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging']) #Disables ubs logging
options.add_experimental_option("detach", True) #leaves browser on

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# webdriver_service = Service("chromedriver/chromedriver") ## path to where you saved chromedriver binary

fName = 'Taylor'
lName = 'Jones'
name = fName + ' ' + lName
email = 'taylorjones1119@gmail.com'
message = '1/22/2023 LAX to Anaheim Marriott, ' \
          '1/23 Anaheim Marriott to Millenium Biltmore, ' \
          '1/24 Millenium Biltmore to LAX'
pax = '56'
addy1 = 'LAX'
addy2 = 'Anaheim Marriott'
phone = '8189256637'
message2_1 =  'for 50 people '
message2_2 = '1/22/2023 5pm Vegas Airport to Luxor '
message2_3 = '1/23 10am-7pm, Luxor to Valley of Fire State Park then dinner in Vegas '
message2_4 = '1/24 10am Luxor to Vegas Airport'
luxor =  ['3900 S Las Vegas Blvd', 'Las Vegas', 'NV', 89119]
harryreid = ['5757 Wayne Newton Blvd', 'Las Vegas', 'NV', 89119]


url = 'https://charters.whitecastletours.com/Quotation'
driver.get(url)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#Pickup[type='text']"))).send_keys(addy1)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#Destination[type='text']"))).send_keys(addy2)


