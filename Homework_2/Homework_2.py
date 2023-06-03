import json
from pprint import pprint

with open ('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for recipes in file:
        cook_ingredient = int(file.readline())
        cook_list = []
        for i in range(cook_ingredient):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            cook_list.append({ 'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure })
        file.readline()

        cook_book[recipes.strip()] = cook_list

    # pprint(cook_book, width=100)   #Вывод через pprint

    # res = json.dumps(cook_book, ensure_ascii=False, indent=2)   #Вывод через json
    # print(res)

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish, ingredients_list in cook_book.items():
        for in_name in ingredients_list:
            if dish in dishes:
                ingredients.update({in_name['ingredient_name']: {'quantity': int(in_name['quantity'])*person_count, 'measure': measure}})
    return ingredients


pprint(get_shop_list_by_dishes(['Омлет','Фахитос'], 1))
