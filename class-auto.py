class AutoCar:
    def __init__(self, Brand, Series, Buildyear):
        self.brand = Brand
        self.series = Series
        self.buildin = Buildyear
        
car_1 = AutoCar('BMW', '330', '2010')
car_2 = AutoCar('Mercedes', 'SL50', '2013')
car_3 = AutoCar('VW', 'Golf mark 7', '2018')

print(car_3.buildin)
