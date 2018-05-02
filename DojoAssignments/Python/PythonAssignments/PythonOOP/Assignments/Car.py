class Car(object):
    def display_all(self):

        print "Price: ${} \n".format(self.price), \
              "Speed: {} mph\n".format(self.speed), \
              "Fuel: {}\n".format(self.fuel), \
              "Mileage: {} mpg\n".format(self.mileage), \
              "Tax: {}%\n".format(self.tax)

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.tax = int(self.tax*100)
        self.display_all()


    # def display_all(self):
    #     print "hello"

    # display_all()


car1 = Car(2000,35,"Full",15)
car2 = Car(5000,25,"Empty",25)
car3 = Car(2005,55,"Quarter Full",12)
car4 = Car(10001,99,"On Fumes",2)
car5 = Car(5,5,"Full",90)
car6 = Car(20000,65,"Empty",25)



