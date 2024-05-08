class RestaurantConfig:
    restaurants = []
    
    def __init__(self, name, category):
        self._name = name.title()
        self.category = category.title()
        self._status = False
        RestaurantConfig.restaurants.append(self)

    def __str__(self):
        return f'{self._name} | {self.category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'{'Restaurant name'.ljust(15)} | {'Category'.ljust(15)} | {'Status'}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(15)} | {restaurant.category.ljust(15)} | {restaurant.status}')
            
    @property
    def status(self):
        return 'Active' if self._status else 'Inactive'
    
    def alternate_status(self):
        self._status = not self._status
    