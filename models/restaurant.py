from models.rate import Rate

class RestaurantConfig:
    restaurants = []
    
    def __init__(self, name, category):
        self._name = name.title()
        self.category = category.title()
        self._status = False
        self._rate = []
        RestaurantConfig.restaurants.append(self)

    def __str__(self):
        return f'{self._name} | {self.category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'{'Restaurant name'.ljust(15)} | {'Category'.ljust(15)} | {'Rate'.ljust(15)} | {'Status'}')
        for restaurant in cls.restaurants:
            # print(f'{restaurant._name.ljust(15)} | {restaurant.category.ljust(15)} | {restaurant.avg_rate.ljust(15)} | {restaurant.status}')
            print(f'{restaurant._name.ljust(15)} | {restaurant.category.ljust(15)} | {str(restaurant.avg_rate).ljust(15)} | {restaurant.status}')

    @property
    def status(self):
        return 'Active' if self._status else 'Inactive'
    
    def alternate_status(self):
        self._status = not self._status
        
    def get_rate(self, client, rate):
        if 0 < rate <= 5:
            rate = Rate(client, rate)
            self._rate.append(rate) 
    
    @property
    def avg_rate(self):
        if not self._rate:
            return '-'
        rate_sum = sum(rate._rate for rate in self._rate)
        rate_qtd = len(self._rate)
        avg = round(rate_sum/rate_qtd, 1)
        return avg