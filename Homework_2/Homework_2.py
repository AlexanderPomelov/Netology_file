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

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                new_shop_list_item = dict(ingridient)
                new_shop_list_item['quantity'] = int(new_shop_list_item['quantity']) * person_count
                if new_shop_list_item['ingredient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

res = json.dumps(get_shop_list_by_dishes(['Омлет','Фахитос'], 3, cook_book), ensure_ascii=False, indent=2)
print(res)
