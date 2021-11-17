import json

with open("menu.json", "r") as my_file:
    menu_json = my_file.read()
    menu = json.loads(menu_json)
    my_file.close()

first_item = menu[0]
max_price = first_item['price']
min_price = first_item['price']

# C1. Перебрать список пицц и найти цену на самую дешевую.
# for item in menu:
#     if item['price'] < min_price:
#         min_price = item['price']
#         name_min_price = item['name']
# print(f"Самая дешевая пицца: {name_min_price}, стоит {min_price} рублей")
# or
def get_min_price(item):
    return item['price']
min_price = min(menu, key=get_min_price)
print(min_price['name'], min_price['price'])
# C2. Перебрать список пицц и найти цену на самую дорогую.
# С3. Вывести название самой дорогой пиццы.
# for item in menu:
#     if item['price'] > max_price:
#         max_price = item['price']
#         name_max_price = item['name']
# print(f"Самая дорогая пицца: {name_max_price}, стоит {max_price} рублей")
# or
def get_max_price(item):
    return item['price']
max_price = max(menu, key=get_max_price)
print(max_price['name'], max_price['price'])
