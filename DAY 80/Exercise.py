import requests

category = input("What type of news are you interested in? (e.g., business, technology, sports): ").strip().lower()


url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey=YOUR_ACTUAL_API_KEY"

r = requests.get(url)


news = r.json() 

print(news, type(news))