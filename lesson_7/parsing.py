from bs4 import BeautifulSoup
import requests

"""
request - запрос 

response - ответ
"""

# parsing = requests.get(url="https://www.nbkr.kg/index.jsp?lang=RUS")
# soup = BeautifulSoup(parsing.text)

# courses = soup.find_all("table", class_="table table-striped")

# for i in courses:
#     print(i.text)

# print(courses)


response = requests.get(url="https://www.sulpak.kg/")
soup = BeautifulSoup(response.text, "lxml")

title = soup.find_all("div", class_="product__item-name")
prices = soup.find_all("div", class_="product__item-price")

for name, price in zip(title, prices):
    print(f"\nНазвание товара - {name.text} - цена - {price.text}")
    
