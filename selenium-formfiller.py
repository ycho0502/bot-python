from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
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
def tripleJ():
    driver.get('https://www.lasvegasbus.com/request-quote')
    driver.find_element(By.ID, '1156231752').send_keys(name)
    driver.find_element(By.ID, '1266727981').send_keys(phone)
    driver.find_element(By.ID, '1578550632').send_keys(email)
    select = Select(driver.find_element(By.ID, '1949618457'))
    select.select_by_visible_text('Other')
    driver.find_element(By.ID, '1118823278').send_keys(message2_1 + Keys.RETURN + message2_2 + Keys.RETURN + message2_3 + Keys.RETURN + message2_4)
    driver.find_element(By.ID, '1494349731').click()

# # Sweetours-----------------------------------------------------------------
def sweetours():
    driver.switch_to.new_window('tab')
    driver.get('https://sweetours.com/contact-us/')
    driver.find_element(By.ID, 'input_1_5_3').send_keys(fName)
    driver.find_element(By.ID, 'input_1_5_6').send_keys(lName)
    driver.find_element(By.ID, 'input_1_2').send_keys(email)
    driver.find_element(By.ID, 'input_1_3').send_keys(phone)
    driver.find_element(By.ID, 'input_1_4').send_keys(message2_1 + Keys.RETURN + message2_2 + Keys.RETURN + message2_3 + Keys.RETURN + message2_4)
    time.sleep(10)

# Windstar-----------------------------------------------------------------
def windstar():
    driver.switch_to.new_window('tab')
    driver.get('https://quotes.gowindstar.com/Quotations/')
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, 'Pickup').send_keys(addy1)
    driver.find_element(By.ID, 'Destination').send_keys(addy2)
    select = Select(driver.find_element(By.ID, 'OBTime'))
    select.select_by_visible_text('10:00am')
    select = Select(driver.find_element(By.ID, 'IBTime'))
    select.select_by_visible_text('07:00pm')
    driver.find_element(By.ID, 'Passengers').send_keys(pax)
    driver.find_element(By.ID, 'MovementDescription').send_keys('Trip details')
    driver.find_element(By.ID, 'MovementFurtherRequirements').send_keys(message2_1 + Keys.RETURN + message2_2 + Keys.RETURN + message2_3 + Keys.RETURN + message2_4)
    select = Select(wait.until(EC.visibility_of_element_located((By.ID, "Quotation_Movements_0_VehicleVariations_0_Vehicles_2_Quantity"))))
    select.select_by_visible_text('1')
    driver.find_element(By.ID, 'Email').send_keys(email)
    driver.find_element(By.ID, 'Firstname').send_keys(fName)
    driver.find_element(By.ID, 'Surname').send_keys(lName)
    select = Select(driver.find_element(By.ID, 'AddressLine4'))
    select.select_by_visible_text('California')
    driver.find_element(By.ID, 'TelNo').send_keys(phone)
    time.sleep(2)
    driver.find_element(By.ID, 'SubmitForm').click()

# Arrow Stage Lines (HAS 40pax & 54pax)-----------------------------------------------------------------
def arrowStage():
    driver.switch_to.new_window('tab')
    driver.get('https://arrowstagelines.com/quick-quotes/')
    wait = WebDriverWait(driver,5)
    select = Select(wait.until(EC.visibility_of_element_located((By.ID, "input_1_39"))))
    select.select_by_visible_text('Arizona')
    wait.until(EC.presence_of_element_located((By.ID, 'gform_next_button_1_41'))).click()
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_1_3'))).send_keys(fName)
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_1_6'))).send_keys(lName)
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_2'))).send_keys(phone)
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_4'))).send_keys(email)
    wait.until(EC.presence_of_element_located((By.ID, 'gform_next_button_1_32'))).click()
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, 'choice_1_7_0'))).click()
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_8'))).send_keys(pax)
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_9_1'))).send_keys("Luxor")
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_9_2'))).send_keys('3900 S Las Vegas Blvd, Las Vegas, NV, 89119')
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_9_3'))).send_keys('Las Vegas')
    select = Select(wait.until(EC.visibility_of_element_located((By.ID, "input_1_9_4"))))
    select.select_by_visible_text('Nevada')
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_9_5'))).send_keys('89119')
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_11'))).send_keys('8/19/2023')
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_12_1'))).send_keys('10')
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_12_2'))).send_keys('00')
    select = Select(wait.until(EC.visibility_of_element_located((By.ID, "input_1_12_3"))))
    select.select_by_visible_text('AM')
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_10_1'))).send_keys("Harry Reid")
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_10_2'))).send_keys('5757 Wayne Newton Blvd, Las Vegas NV, 89119')
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_10_3'))).send_keys('Las Vegas')
    select = Select(wait.until(EC.visibility_of_element_located((By.ID, "input_1_10_4"))))
    select.select_by_visible_text('Nevada')
    wait.until(EC.presence_of_element_located((By.ID, 'input_1_10_5'))).send_keys('89119')
    wait.until(EC.presence_of_element_located((By.ID, 'gform_next_button_1_33'))).click()
    time.sleep(2)
    select = Select(wait.until(EC.visibility_of_element_located((By.ID, "input_1_16"))))
    select.select_by_visible_text('54 Passenger Motorcoach')
    wait.until(EC.presence_of_element_located((By.ID, 'choice_1_17_3'))).click()
    wait.until(EC.presence_of_element_located((By.ID, 'gform_next_button_1_34'))).click()
    time.sleep(2)
    driver.find_element(By.ID, 'input_1_20').send_keys(message2_1 + Keys.RETURN + message2_2 + Keys.RETURN + message2_3 + Keys.RETURN + message2_4)
    wait.until(EC.presence_of_element_located((By.ID, 'gform_submit_button_1'))).click()

# # White castle-----------------------------------------------------------
def whiteCastle():
    driver.switch_to.new_window('tab')
    driver.get('https://charters.whitecastletours.com/Quotation')
    driver.find_element(By.ID, 'Pickup').send_keys(addy1)
    select = Select(driver.find_element(By.ID, 'OBTime'))
    select.select_by_visible_text('10:00am')
    select = Select(driver.find_element(By.ID, 'IBTime'))
    select.select_by_visible_text('07:00pm')
    driver.find_element(By.ID, 'Destination').send_keys(addy2)
    driver.find_element(By.ID, 'Passengers').send_keys(pax)
    driver.find_element(By.ID, 'MovementDescription').send_keys("Trip Details")
    driver.find_element(By.ID, 'MovementFurtherRequirements').send_keys(message2_1 + Keys.RETURN + message2_2 + Keys.RETURN + message2_3 + Keys.RETURN + message2_4)
    driver.find_element(By.ID, 'Email').send_keys(email)
    driver.find_element(By.ID, 'Firstname').send_keys(fName)
    driver.find_element(By.ID, 'Surname').send_keys(lName)
    driver.find_element(By.ID, 'AddressLine3').send_keys('Los Angeles')
    driver.find_element(By.ID, 'TelNo').send_keys(phone)
    select = Select(driver.find_element(By.ID, 'Quotation_Movements_0_VehicleVariations_0_Vehicles_2_Quantity'))
    select.select_by_visible_text('1')
    select = Select(driver.find_element(By.ID, 'Quotation_ClientContactConsent_Consent'))
    select.select_by_visible_text('No')
    time.sleep(2)
    driver.find_element(By.ID, 'SubmitForm').click()

# cognitoforms---------------------------------------------------
def cognitoforms():
    driver.switch_to.new_window('tab')
    driver.get('https://www.cognitoforms.com/HolidayMotorCoach/OnlineQuote')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "cog-input-auto-0"))).send_keys(fName)
    wait.until(EC.presence_of_element_located((By.ID, "cog-input-auto-1"))).send_keys(lName)
    wait.until(EC.presence_of_element_located((By.ID, "cog-2"))).send_keys(phone)
    wait.until(EC.presence_of_element_located((By.ID, "cog-3"))).send_keys(phone)
    wait.until(EC.presence_of_element_located((By.ID, "cog-4-line1"))).send_keys("3900 S Las Vegas Blvd")
    wait.until(EC.presence_of_element_located((By.ID, "cog-4-city"))).send_keys("Las Vegas")
    wait.until(EC.presence_of_element_located((By.ID, "cog-4-state"))).send_keys("Nevada")
    wait.until(EC.presence_of_element_located((By.ID, "cog-4-zip-code"))).send_keys("89119")
    wait.until(EC.presence_of_element_located((By.ID, "cog-5"))).send_keys(email)
    wait.until(EC.presence_of_element_located((By.ID, "cog-7"))).send_keys("Other")
    wait.until(EC.presence_of_element_located((By.ID, "cog-8"))).send_keys("56 Passenger Motor Coach")
    wait.until(EC.presence_of_element_located((By.ID, "cog-9"))).send_keys("1")
    wait.until(EC.presence_of_element_located((By.ID, "cog-10-line1"))).send_keys("1 World Way")
    wait.until(EC.presence_of_element_located((By.ID, "cog-10-city"))).send_keys("Los Angeles")
    wait.until(EC.presence_of_element_located((By.ID, "cog-10-state"))).send_keys("California")
    wait.until(EC.presence_of_element_located((By.ID, "cog-10-zip-code"))).send_keys("90045")
    wait.until(EC.presence_of_element_located((By.ID, "cog-11"))).send_keys("1/22/2023")
    wait.until(EC.presence_of_element_located((By.ID, "cog-12"))).send_keys("5:00 PM")
    wait.until(EC.presence_of_element_located((By.ID, "cog-13-line1"))).send_keys("3900 S Las Vegas Blvd")
    wait.until(EC.presence_of_element_located((By.ID, "cog-13-city"))).send_keys("Las Vegas")
    wait.until(EC.presence_of_element_located((By.ID, "cog-13-state"))).send_keys("Nevada")
    wait.until(EC.presence_of_element_located((By.ID, "cog-14"))).send_keys("1/24/2023")
    wait.until(EC.presence_of_element_located((By.ID, "cog-15"))).send_keys("10:00 AM")
    wait.until(EC.presence_of_element_located((By.ID, "cog-13-zip-code"))).send_keys("89119")
    wait.until(EC.presence_of_element_located((By.ID, "cog-16"))).send_keys(message)
    time.sleep(10)

# LuxCoach----------------------------------------------------------------
def luxcoach():
    driver.switch_to.new_window('tab')
    driver.get('https://luxcoachamerica.com/quote')
    wait = WebDriverWait(driver, 10)
    wait1 = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input.text-input')))
    wait1[0].send_keys(name)
    wait1[1].send_keys(email)
    wait1[2].send_keys(phone)
    wait1[3].send_keys(message)
    wait1[4].send_keys(pax)
    wait2 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'text-area')))
    wait2.send_keys("3days")
    time.sleep(10)

# Sunshine Travel-------------------------------------------------------------
def sunshine():
    driver.switch_to.new_window('tab')
    driver.get('https://www.sunshinetravellv.com/')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "contact_request_name"))).send_keys(name)
    wait.until(EC.presence_of_element_located((By.ID, "contact_request_email"))).send_keys(email)
    wait.until(EC.presence_of_element_located((By.ID, "contact_request_phone"))).send_keys(phone)
    wait.until(EC.presence_of_element_located((By.ID, "contact_request_comments"))).send_keys(message2_1 + Keys.RETURN + message2_2 + Keys.RETURN + message2_3 + Keys.RETURN + message2_4)
    time.sleep(30)


# tripleJ()
# sweetours()
# windstar()
# arrowStage()
# whiteCastle()
# cognitoforms()
# luxcoach()
sunshine()
# driver.quit()