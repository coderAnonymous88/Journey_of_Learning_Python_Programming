import requests
from bs4 import BeautifulSoup

# response = requests.get("https://google.com")

# print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 1,
#   }
# headers = {
#     'Content-type': 'application/json; charset=UTF-8',
#   }

# response = requests.post(url , headers=headers , json=data)

# print("Status Code:" , response.status_code)
# print(response.json())


url = "https://github.blog/"
r = requests.get(url)
# print(r.text)



soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading)