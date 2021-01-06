import requests as req
from bs4 import BeautifulSoup
from ScrapingBot import Spider

bot = Spider()
bot.request_destination()
bot.request_item_quantity()
bot.request_html_data()
bot.parse_html_result()

for item in bot.item_list:
    print(item.print())
    # print()