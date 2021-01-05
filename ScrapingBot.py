import requests as req
from Item import Item
from bs4 import BeautifulSoup


class Spider(object):

    data = " "
    name = 'Jinx'
    item_list = []
    html_result = " "
    item_prices = []
    destination = " "
    item_quantity = 0

    def __init__(self):
        print("Hello my name is Jinx\n")
        self.name = 'Jinx'

    def request_destination(self):
        try:
            self.destination = input("Where would you like me to search? \n")
        except ValueError:
            print("Invalid Entry: Value Error")

    def request_item_quantity(self):
        try:
            self.item_quantity = int(input("How many many results would you like? \n"))
        except ValueError:
            print("Invalid Entry: Value Error")

    def request_html_data(self):
        try:
            self.html_result = req.get(self.destination)
            self.data = self.html_result.text
        except():
            print("Failed to request HTML Data")

    def parse_html_result(self):
        constraint = self.item_quantity
        counter = 0
        soup = BeautifulSoup(self.data, features="html.parser")
        listings = soup.find_all('li', attrs={'class': 's-item'})

        for listing in listings:

            item_name = str(listing.find('h3', attrs={'class': 's-item__title'}))
            item_name = item_name[item_name.find(">")+1:-5]

            item_status = str(listing.find('span', attrs={'class': 'SECONDARY_INFO'}))
            item_status = item_status[item_status.find('>')+1:-7]

            item_shipping = str(listing.find('span', attrs={'class': 's-item__shipping'}))
            item_shipping = item_shipping[item_shipping.find('>')+1:-7]

            item_price = str(listing.find('span', attrs={'class': 's-item__price'}))
            item_price = item_price[item_price.find(">")+1:-7]

            item_buying = str(listing.find('span', attrs={'class': 's-item__purchase-options-with-icon'}))
            item_buying = item_buying[item_buying.find(">")+1:-7]

            if counter == 0:
                counter += 1
                continue

            counter += 1

            self.item_list.append(Item(item_name, item_price, item_status, item_shipping, item_buying))

            if counter == constraint+1:
                break
