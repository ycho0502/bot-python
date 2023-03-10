from googlesearch import search
import random


searchterms = [
    'Coach Bus Los Angeles',
    'Los Angeles Coach Bus',
    'rent a bus los angeles',
    'Bus Rental Los Angeles',
    'la charter bus',
    'LA bus rental',
    'los angeles mini bus'
]
a = random.randrange(0, len(searchterms))

# googlesearch-python
search_results = search(searchterms[a], stop=5)
print(searchterms[a])

for result in search_results:
    print(result)

# Google Drive https://www.thepythoncode.com/article/using-google-drive--api-in-python
# Google Sheets https://www.geeksforgeeks.org/how-to-automate-google-sheets-with-python/?ref=rp
# Google Custom Search # https://www.thepythoncode.com/article/use-google-custom-search-engine-api-in-python
# Google Search https://www.geeksforgeeks.org/google-search-analysis-with-python/?ref=rp

# from googleapiclient.discovery import build
# apiKey="AIzaSyDgyEKsxkaOqyhfV805tGI12j2LFBuztts"
#
# def google_results_count(query):
#     service = build("customsearch", "v1",
#                     developerKey="306c676815fb87381a728adf09bfa37cf07f6f2f")
#
#     result = service.cse().list(
#             q=query,
#             cx=apiKey
#         ).execute()
#
#     return result["searchInformation"]["totalResults"]
#
# print google_results_count('Python is awesome')