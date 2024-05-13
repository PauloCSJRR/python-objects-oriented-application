from models.restaurant import RestaurantConfig
from models.menu.drink import Drink
from models.menu.dish import Dish

italian_restaurant = RestaurantConfig('supreme Pizza', 'Italian')
mexican_restaurant = RestaurantConfig('Mexican Food', 'Mexican')
japanese_restaurant = RestaurantConfig('Sushi Now', 'Japanese')

drink_juice = Drink('Melon Juice', 5.0, 'Big')
drink_juice.apply_discount()
dish_steak = Dish('Steak', 25.0, 'Ribeye Cap Steak')
dish_steak.apply_discount()

italian_restaurant.add_to_menu(drink_juice)
italian_restaurant.add_to_menu(dish_steak)

# RestaurantConfig.list_restaurants()

def main():
    italian_restaurant.show_menu

if __name__ == '__main__':
    main()
