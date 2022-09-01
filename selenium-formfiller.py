import selenium

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())

fName = 'Taylor'
lName = 'Jones'
email = 'taylorjones1119@gmail.com'
message = '8/2/2022 LAX to Anaheim Marriott, ' \
          '8/3 Anaheim Marriott to Millenium Biltmore, ' \
          '8/4 Millenium Biltmore to LAX'
phone = '8189256637'


browser.get('https://www.bigccharterservice.com/contact-uc')
print(browser.title)

browser.find_element_by_id('1245374334').send_keys(fName)
browser.find_element_by_id('1606564143').send_keys(lName)
browser.find_element_by_id('1319114980').send_keys(email)
browser.find_element_by_id('1162459086').send_keys(message)
# browser.find_element_by_id('1287052193').click()

browser.get('https://www.tcsbus.com/contact-us/')
print(browser.title)

browser.find_element_by_id('input_2_1_3').send_keys(fName)
browser.find_element_by_id('input_2_1_6').send_keys(lName)
browser.find_element_by_id('input_2_2').send_keys(email)
browser.find_element_by_id('input_2_3').send_keys('3 days Los Angeles')
browser.find_element_by_id('input_2_4').send_keys(message)
# CAPTCHA HERE NEED TO FIGURE OUT
# browser.find_element_by_id('gform_submit_button_2').click()


## QUICK QUOTE
# watch the AntiForgeryTokenContainer
browser.get('https://charters.pacificcoachways.com/widgets/quickquote')
# print(browser.title)
#
# browser.find_element_by_id('Firstname').send_keys(fName)
# browser.find_element_by_id('Surname').send_keys(lName)
# browser.find_element_by_id('Email').send_keys(email)
# browser.find_element_by_id('TelNo').send_keys(phone)
# browser.find_element_by_class_name()
# browser.find_element_by_id('input_2_4').send_keys(message)
# browser.find_element_by_id('gform_submit_button_2').click()



browser.quit()