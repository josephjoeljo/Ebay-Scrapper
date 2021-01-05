
class Item(object):

    item_name = ''
    item_price = ''
    item_condition = ''
    item_shipping_price = ''
    item_purchase_option = ''

    def __init__(self, name, price, condition, shipping, option):
        self.item_name = name
        self.item_price = price
        self.item_condition = condition
        self.item_shipping_price = shipping
        self.item_purchase_option = option

    def print(self):
        print(self.item_name)
        print(self.item_price)
        print(self.item_condition)
        print(self.item_shipping_price)
        print(self.item_purchase_option)
        print()
