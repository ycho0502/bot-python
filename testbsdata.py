import requests
from bs4 import BeautifulSoup

links = ['whitecastletours.com', 'gowindstar.com', 'arrowstagelines.com', 'sunshinetravellv.com', 'sweetours.com', 'lasvegasbus.com']
# url = 'https://www.bigccharterservice.com/contact-uc'

# Need header to mimic a real browser and avoid being detected as a scraper
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

for link in links:
    response = requests.get('http://' + link,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    result = soup.find('h1')
    
    if result is not None:
        h1_strings = [string for string in result.strings]  # Extract the string contents of the h1 tag and its child tags separately
        h1_string = ''.join(h1_strings)  # Combine the strings into a single string
        print(f"{link}: {h1_string}")
    else:
        print(f"{link}: h1 tag not found")

# response = requests.get(url,headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')

# outputs initial tag with given id value
result_by_id = soup.find(id="1245374334")

# outputs initial tag with input and id value
# result_by_input_id = soup.find('input', {'id': '1245374334'})

# print(result_by_input_id)