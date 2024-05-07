class RestaurantConfig:
    restaurants = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.status = False
        RestaurantConfig.restaurants.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    
    def list_restaurants():
        for restaurant in RestaurantConfig.restaurants:
            print(f'{restaurant.name} | {restaurant.category} | {restaurant.status}')
    
    
restaurant_pizza = RestaurantConfig('Supreme Pizza', 'Italian')
restaurant_sushi = RestaurantConfig('Sushi Now', 'Japanese')

RestaurantConfig.list_restaurants()