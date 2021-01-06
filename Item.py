
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
        return (self.item_name + "\n" + self.item_price + " \n" + self.item_condition + "\n"
                     + self.item_shipping_price + "\n" + self.item_purchase_option + "\n")
