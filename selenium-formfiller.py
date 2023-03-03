from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time

options = Options()
options.add_experimental_option("detach", True) #leaves browser on
options.add_experimental_option('excludeSwitches', ['enable-logging']) #Disables ubs logging

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


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


# Triple J Tours-----------------------------------------------------------------
driver.get('https://www.lasvegasbus.com/request-quote')
driver.find_element(By.ID, '1156231752').send_keys(name)
driver.find_element(By.ID, '1266727981').send_keys(phone)
driver.find_element(By.ID, '1578550632').send_keys(email)
select = Select(driver.find_element(By.ID, '1949618457'))
select.select_by_visible_text('Other')
driver.find_element(By.ID, '1118823278').send_keys(message2_1 + Keys.RETURN + message2_2 + Keys.RETURN + message2_3 + Keys.RETURN + message2_4)

# Sweetours-----------------------------------------------------------------
driver.get('https://sweetours.com/contact-us/')
driver.find_element(By.ID, 'input_1_5_3').send_keys(fName)
driver.find_element(By.ID, 'input_1_5_6').send_keys(lName)
driver.find_element(By.ID, 'input_1_3').send_keys(phone)
driver.find_element(By.ID, 'input_1_4').send_keys(message2_1 + Keys.RETURN + message2_2 + Keys.RETURN + message2_3 + Keys.RETURN + message2_4)

# Windstar-----------------------------------------------------------------
driver.get('https://quotes.gowindstar.com/Quotations/')
driver.find_element(By.ID, 'Pickup').send_keys(addy1)
driver.find_element(By.ID, 'Destination').send_keys(addy2)
driver.find_element(By.ID, 'Passengers').send_keys(pax)
driver.find_element(By.ID, 'MovementDescription').send_keys(message)
driver.find_element(By.ID, 'Email').send_keys(email)
driver.find_element(By.ID, 'Firstname').send_keys(fName)
driver.find_element(By.ID, 'Surname').send_keys(lName)
driver.find_element(By.ID, 'TelNo').send_keys(phone)

# Arrow Stage Lines (HAS 40pax & 54pax)-----------------------------------------------------------------
driver.get('https://arrowstagelines.com/quick-quotes/')
wait = WebDriverWait(driver,5)
select = Select(wait.until(EC.visibility_of_element_located((By.ID, "input_1_39"))))
select.select_by_visible_text('Arizona')
wait.until(EC.presence_of_element_located((By.ID, 'gform_next_button_1_41'))).click()
wait.until(EC.presence_of_element_located((By.ID, 'input_1_1_3'))).send_keys(fName)


# White castle-----------------------------------------------------------
driver.get('https://charters.whitecastletours.com/Quotation')
driver.find_element(By.ID, 'Pickup').send_keys(addy1)
driver.find_element(By.ID, 'Destination').send_keys(addy2)
driver.find_element(By.ID, 'Passengers').send_keys(pax)
driver.find_element(By.ID, 'MovementDescription').send_keys(message)
driver.find_element(By.ID, 'Email').send_keys(email)
driver.find_element(By.ID, 'Firstname').send_keys(fName)
driver.find_element(By.ID, 'Surname').send_keys(lName)
driver.find_element(By.ID, 'AddressLine3').send_keys('Los Angeles')
driver.find_element(By.ID, 'TelNo').send_keys(phone)
select = Select(driver.find_element(By.ID, 'Quotation_Movements_0_VehicleVariations_0_Vehicles_2_Quantity'))
select.select_by_visible_text('1')

# cognitoforms---------------------------------------------------
driver.get('https://www.cognitoforms.com/HolidayMotorCoach/OnlineQuote')


# Triple J Tours
browser.get('https://www.lasvegasbus.com/request-quote')
print(browser.title)

browser.find_element(By.ID, '1156231752').send_keys(name)
browser.find_element(By.ID, '1266727981').send_keys(phone)
browser.find_element(By.ID, '1578550632').send_keys(email)
browser.find_element(By.ID, '1118823278').send_keys(message2_1 + Keys.RETURN + message2_2 + Keys.RETURN + message2_3 + Keys.RETURN + message2_4)
# triplejselect = Select(browser.find_element_by_id('1949618457'))
# triplejselect.select_by_index(1)

# Sweetours
browser.get('https://sweetours.com/contact-us/')
print(browser.title)

# browser.find_element(By.ID, 'input_1_2').send_keys(email)
browser.find_element(By.ID, 'input_1_5_3').send_keys(fName)
browser.find_element(By.ID, 'input_1_5_6').send_keys(lName)
browser.find_element(By.ID, 'input_1_3').send_keys(phone)
browser.find_element(By.ID, 'input_1_4').send_keys(message2_1 + Keys.RETURN + message2_2 + Keys.RETURN + message2_3 + Keys.RETURN + message2_4)

# Windstar
browser.get('https://quotes.gowindstar.com/Quotations/')

browser.find_element(By.ID, 'Email').send_keys(email)
browser.find_element(By.ID, 'Firstname').send_keys(fName)
time.sleep(10)

# Arrow Stage Lines (HAS 40pax & 54pax)
browser.get('https://arrowstagelines.com/quick-quotes/')
print(browser.title)

# Step 1
select = Select(browser.find_element(By.ID, 'input_1_39'))
select.select_by_value('Nevada')
time.sleep(20)
# browser.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
# time.sleep(10)
# select = Select(browser.find_element_by_id('input_1_39'))
# select.select_by_value('Nevada')
# browser.find_elements_by_css_selector('input.gform_next_button')[0].send_keys(Keys.RETURN)
# time.sleep(5)
# # Step 2
# browser.find_element_by_id('input_1_1_3').send_keys(fName)
# browser.find_element_by_id('input_1_1_6').send_keys(lName)
# browser.find_element_by_id('input_1_2').send_keys(phone)
# browser.find_element_by_id('input_1_4').send_keys(email)
# time.sleep(10)
# browser.find_elements_by_css_selector('input.gform_next_button')[0].send_keys(Keys.RETURN)
# # Step 3 (doesnt need state)
# browser.find_element_by_id('input_1_8').send_keys(pax)
# # Step 4 (select 54pax)

# Step 5 (message)

# # White castle
# browser.get('https://charters.whitecastletours.com/Quotation')

# American Stage Lines
# Royal Coach Tours
# #### TTS CHARTER BUS
# driver.get('https://www.ttsshuttle.com/free-bus-quote')
# driver.find_element_by_id('input_comp-k8od8s4n').send_keys(fName + ' ' + lName)
# driver.find_element_by_id('input_comp-k8od8s4x').send_keys(email)
# driver.find_element_by_id('input_comp-k8od8s52').send_keys(phone)
# driver.find_element_by_id('input_comp-k8odc0dj').send_keys(Keys.SPACE) WHAT IS THIS?
# driver.find_element_by_id('input_comp-k8odc4dt').send_keys('e') WHAT IS THIS?
#
# #### GOLD COAST TOURS
# driver.get('https://www.goldcoasttours.com/free-quote')
# print(driver.title)
#
# driver.find_element_by_id('input_comp-krb098ry1').send_keys(fName + ' ' + lName)
# # driver.find_element_by_id('input_comp-krb098ry1').send_keys(fName)
# driver.find_element_by_id('input_comp-krb098s71').send_keys(phone)
# driver.find_element_by_id('input_comp-krb0eaaj').send_keys(email)
# driver.find_element_by_id('input_comp-kydb4i55').send_keys(pax)
#
#
# #### BIG C CHARTER SERVICE
# driver.get('https://www.bigccharterservice.com/contact-uc')
# print(driver.title)
#
# driver.find_element_by_id('1245374334').send_keys(fName)
# driver.find_element_by_id('1606564143').send_keys(lName)
# driver.find_element_by_id('1319114980').send_keys(email)
# driver.find_element_by_id('1162459086').send_keys(message)
# # driver.find_element_by_id('1287052193').click()
#
#
# #### TCS BUS
# driver.get('https://www.tcsbus.com/contact-us/')
# print(driver.title)
#
# driver.find_element_by_id('input_2_1_3').send_keys(fName)
# driver.find_element_by_id('input_2_1_6').send_keys(lName)
# driver.find_element_by_id('input_2_2').send_keys(email)
# driver.find_element_by_id('input_2_3').send_keys('3 days Los Angeles')
# driver.find_element_by_id('input_2_4').send_keys(message)
# # CAPTCHA HERE NEED TO FIGURE OUT
# # driver.find_element_by_id('gform_submit_button_2').click()


####

## QUICK QUOTE
# watch the AntiForgeryTokenContainer
# driver.get('https://charters.pacificcoachways.com/widgets/quickquote')
# print(driver.title)
#
# driver.find_element_by_id('Firstname').send_keys(fName)
# driver.find_element_by_id('Surname').send_keys(lName)
# driver.find_element_by_id('Email').send_keys(email)
# driver.find_element_by_id('TelNo').send_keys(phone)
# driver.find_element_by_class_name()
# driver.find_element_by_id('input_2_4').send_keys(message)
# driver.find_element_by_id('gform_submit_button_2').click()

# https://www.goldcoasttours.com/free-quote
# https://portal.luxbusamerica.com/Quotation
# https://charters.pacificcoachways.com/Quotation
# https://form.jotform.com/atstpe/client-trip-itinerary
# https://www.tcsbus.com/request-a-quote/
# https://ccctours.com/contact-us/
# https://www.bigccharterservice.com/private-charters
# https://www.ridemcoach.com/book-now
# https://tlcluxury.com/charter-bus-quote/
# https://www.ttsshuttle.com/free-bus-quote
# https://intermex.sengerio.site/forms/index#request-for-quotation

# Strackground
# California sight seers

# Step 1
# select = Select(driver.find_element(By.ID, 'input_1_39'))
# select.select_by_value('Nevada')
# time.sleep(20)
# driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
# time.sleep(10)
# select = Select(driver.find_element_by_id('input_1_39'))
# select.select_by_value('Nevada')
# driver.find_elements_by_css_selector('input.gform_next_button')[0].send_keys(Keys.RETURN)
# time.sleep(5)
# # Step 2
# driver.find_element_by_id('input_1_1_3').send_keys(fName)
# driver.find_element_by_id('input_1_1_6').send_keys(lName)
# driver.find_element_by_id('input_1_2').send_keys(phone)
# driver.find_element_by_id('input_1_4').send_keys(email)
# time.sleep(10)
# driver.find_elements_by_css_selector('input.gform_next_button')[0].send_keys(Keys.RETURN)
# # Step 3 (doesnt need state)
# driver.find_element_by_id('input_1_8').send_keys(pax)
# # Step 4 (select 54pax)

# Step 5 (message)


# driver.quit()