from models.rate import Rate
from models.menu.menu_item import MenuItem

class RestaurantConfig:
    restaurants = []
    
    def __init__(self, name, category):
        self._name = name.title()
        self.category = category.title()
        self._status = False
        self._rate = []
        self._menu = []
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
    
    def add_to_menu(self, item):
        if isinstance(item,MenuItem):
            self._menu.append(item)

    @property
    def show_menu(self):
        print(f'Menu of restaurant {self._name}\n')
        for i,item in enumerate(self._menu, start=1):
                        
            if hasattr(item, 'description'):
                msg = f'{i}. Name: {item._name} | Price: ${item._price} | Description: {item.description}'
                print(msg)
                
            else:
                msg = f'{i}. Name: {item._name} | Price: ${item._price} | Size: {item.size}'
                print(msg)
                
            
        
    