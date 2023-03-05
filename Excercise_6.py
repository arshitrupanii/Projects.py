import requests
import os
import pyshorteners

a = str(input("Good morning Sir, How are you 😊😊 : "))
n = str(input("What's your name : "))
os.system('clear')
print("Welcome to Taza Khabar news")

country = input('''Choose Your country :
us : US
in : India
ca : canada
gb : UK\n
Ans.
''')
os.system('clear')

topic = input('''Choose Topic:
1 : Sports
2 : Entertainment
3 : Technology
4 : Healthcare 
5 : Business
6 : Science
7 : politics\n
Ans. 
''')
os.system('clear')

if (int(topic) < 1 or int(topic) > 9):
  print("You went wrong")
  exit(1)

Topic = {
  "1": "sports",
  "2": "entertainment",
  "3": "technology",
  "4": "health",
  "5": "business",
  "6": "science",
  "7": "politics"
}
print(f"{n.capitalize()}, We Have found Some {Topic[topic]} news for You \n")


# News coding
api_key = "cb45d6e16ed24c01a8a48feb5b90b6e0" #Enter your key here
url = f"https://newsapi.org/v2/top-headlines?country={country}&category={Topic[topic]}&apiKey="+api_key
news = requests.get(url).json()

articles = news["articles"]

_articles = []
_articlesurl = []
_news = ""
_newsurl = ''
type_tiny = pyshorteners.Shortener()


for article in articles:
 _articles.append(article["title"])
 _articlesurl.append(article["url"])

# 0 to 5 news
for i in range(5):
  print(_news + str(i+1) + ". " + _articles[i])
  print(type_tiny.tinyurl.short(_newsurl + _articlesurl[i]) + '\n')

# function
def funr():
  print("- If you want to continue, Press : 'c'")
  exit_ = input("- If you want to Exit, Press : 'e' >> ")
  if exit_ == 'e':
    print("\nThanks for visit us...")
    exit()
  else:
    print("\nThanks for visit us...")

# 5 to 10 news
repeat = input("For more news, Press : 'z' >> ")
print("\n")

if repeat == 'z' or 'Z':
  for i in range(5,10):
    print(_news + str(i+1) + ". " + _articles[i])
    print(type_tiny.tinyurl.short(_newsurl + _articlesurl[i]) + '\n')
funr()

# 10 to 15 news
for i in range(i-4,i):
  print(_news + str(i+1) + ". " + _articles[i])
  print(type_tiny.tinyurl.short(_newsurl + _articlesurl[i]) + '\n')
funr()

# # 15 to 20 news
for i in range(10,15):
  print(_news + str(i+1) + ". " + _articles[i])
  print(type_tiny.tinyurl.short(_newsurl + _articlesurl[i]) + '\n')
funr()

# 20 to 25 news
for i in range(15,20):
  print(_news + str(i+1) + ". " + _articles[i])
  print(type_tiny.tinyurl.short(_newsurl + _articlesurl[i]) + '\n')
funr()
