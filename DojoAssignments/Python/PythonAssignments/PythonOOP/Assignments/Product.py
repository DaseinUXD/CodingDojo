class Product(object):
    def __init__(self, price, item_name, weight, brand, ):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.totalPrice = None


    def sell(self):
        self.add_tax(self.tax)
        self.status = "sold"

    def add_tax(self, tax):
        self.tax = tax
        self.totalPrice = (self.price * self.tax) + self.price
        return self

    def return_product(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
            self.totalPrice = None

        elif self.reason == "opened":
            self.status = "used"
            self.price = self.price - (self.price * 0.20)
            self.totalPrice = self.price + (self.price * self.tax)

        else:
            self.status = "new"
        self.display_info()
        return self

    def display_info(self):
        if self.totalPrice == None:
            print "Item Name: {} \n".format(self.item_name), \
                "Price: ${} \n".format(self.price), \
                "Weight: {} lbs \n".format(self.weight), \
                "Brand: {} \n".format(self.brand), \
                "Status: {} \n".format(self.status)
        else:
            print "Item Name: {} \n".format(self.item_name), \
                "Price: ${} \n".format(self.price), \
                "Price with tax: ${} \n".format(self.totalPrice), \
                "Weight: {} lbs \n".format(self.weight), \
                "Brand: {} \n".format(self.brand), \
            "Status: {} \n".format(self.status)


tv = Product(200, "television", 50, "Samsung")
dvd = Product(100, "dvd player", 15, "Sanyo")

tv.add_tax(0.0825)
tv.sell()
tv.display_info()
dvd.display_info()

tv.return_product("opened")
tv.return_product("defective")


