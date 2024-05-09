from models.restaurant import RestaurantConfig

italian_restaurant = RestaurantConfig('supreme Pizza', 'Italian')
italian_restaurant.get_rate('Paul', 5)
italian_restaurant.get_rate('Pedro', 2)
mexican_restaurant = RestaurantConfig('Mexican Food', 'Mexican')
mexican_restaurant.alternate_status()
japanese_restaurant = RestaurantConfig('Sushi Now', 'Japanese')

RestaurantConfig.list_restaurants()

def main():
    RestaurantConfig.list_restaurants()

if __name__ == 'main':
    main()