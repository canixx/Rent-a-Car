import datetime
#parent class
class VehicleRent:

    def __init__(self,stock):
        self.stock = stock
        self.now = 0

    def displayStock(self):
        """
        display stock
        """
        print("{} vehicle available to rent".format(self.stock))
        return self.stock

    def rentHourly(self,n):
        """
        rent hourly

        """
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours.".format(n,self.now.hour))

            self.stock -= n

            return self.now


    def rentDaily(self,n):
        """
        rent daily

        """
        if n <= 0:
            print("Number should be positive")
            return None

        elif n > self.stock:
            print("Sorry, {} vehicle available to rent".format(self.stock))
            return None

        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for daily at {} hours.".format(n, self.now.hour))

            self.stock -= n

            return self.now

    def returnVehicle(self,request,brand):
        """
        return a bill
        """
        car_hourly_price = 10
        car_daily_price = car_hourly_price*8/10*24
        bike_hourly_price = 5
        bike_daily_price = bike_hourly_price*7/10*24

        rentalTime, rentalBasis, numberOfVehicle = request
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numberOfVehicle:
                self.stock += numberOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now -rentalTime

                if rentalBasis == 1: #hourly
                    bill = rentalPeriod.seconds/3600*car_hourly_price*numberOfVehicle

                elif rentalBasis == 2: #daily
                    bill = rentalPeriod.seconds/(3600*24)*car_daily_price*numberOfVehicle

                if ( 2<= numberOfVehicle):
                    print ("you have extra 20% discount")
                    bill = bill*0.8

                print("Thank you for returning your car")
                print("Price: $ {}".format(bill))

        elif brand == "bike":
            if rentalTime and rentalBasis and numberOfVehicle:
                self.stock += numberOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:  # hourly
                    bill = rentalPeriod.seconds / 3600 * bike_hourly_price * numberOfVehicle

                elif rentalBasis == 2:  # daily
                    bill = rentalPeriod.seconds / (3600 * 24) * bike_daily_price * numberOfVehicle

                if (4 <= numberOfVehicle):
                    print("you have extra 20% discount")
                    bill = bill * 0.8

                print("Thank you for returning your bike")
                print("Price: $ {}".format(bill))
        else:
            print("You do not rent a vehicle")
            return None

#child class 1
class CarRent(VehicleRent):

    global discount_rate
    discount_rate =15

    def __init__(self,stock):
        super().__init__(stock)

    def discount(self,b):

        bill = b - (b*discount_rate)/100
        return bill

#child class 2
class BikeRent(VehicleRent):

    def __init__(self,stock):
        super().__init__(stock)

#customer
class Customer:

    def __init__(self):
        self.bikes = 0
        self.rentalBasis_bike = 0
        self.rentalTime_bike = 0
        self.cars = 0
        self.rentalBasis_car = 0
        self.rentalTime_car = 0


    def requestVehicle(self,brand):
        """
        take a request bike or car from customer

        """
        if brand == "bike":
            bikes = input("How many bikes would you like to rent?")

            try:
                bikes = int(bikes)
            except ValueError:
                print("Form of a entered bike number should be number.")
                return -1

            if bikes < 1:
                print("Number of bikes sould be greater than zero")
                return -1
            else:
                self.bikes = bikes
            return self.bikes

        elif brand == "car":
            cars = input("How many cars would you like to rent?")

            try:
                cars = int(cars)
            except ValueError:
                print("Form of a entered bike number should be number.")
                return -1

            if cars < 1:
                print("Number of cars should be greater than zero")
                return -1
            else:
                self.cars = cars
            return self.cars


        else:
            print("request vehicle error")


    def returnVehicle(self,brand):
        """
        :return: bike or car

        """
        if brand == "bike":
            if self.rentalTime_bike and self.rentalBasis_bike and self.bikes:
                return self.rentalTime_bike,self.rentalBasis_bike, self.bikes
            else:
                return 0,0,0
        elif brand == "car":
            if self.rentalTime_car and self.rentalBasis_car and self.cars:
                return self.rentalTime_car,self.rentalBasis_car, self.cars
            else:
                return 0,0,0
        else:
            print("Return vehicle error")

