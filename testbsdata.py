import requests
from bs4 import BeautifulSoup

url = 'https://www.bigccharterservice.com/contact-uc'
# Need header to mimic a real browser and avoid being detected as a scraper
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# outputs initial tag with given id value
result_by_id = soup.find(id="1245374334")

# outputs initial tag with input and id value
result_by_input_id = soup.find('input', {'id': '1245374334'})

print(result_by_input_id)