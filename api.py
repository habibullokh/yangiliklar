from bs4 import BeautifulSoup
import requests
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

for i in range(1, 10):
    url = f"https://daryo.uz/category/dunyo?page={i}&per-page=10"
    url_2 = "https://daryo.uz"
    

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    titles = soup.find_all("a", class_="mini__article-link")

    for title in titles:
        print(50 * "=")
        print(title.text)
        url = title["href"]
        main_url = url_2 + url

        text = requests.get(main_url)
        soup2 = BeautifulSoup(text.content, "html.parser")
        
        text2 = soup2.find_all("p")
        
        for text3 in text2:
          text4 = text3.text
          text_replaced = " ".join(text4.split())
          print(text_replaced)