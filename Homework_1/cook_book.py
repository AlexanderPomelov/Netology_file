import json


with open (r'C:\Users\apomelov\Desktop\TEST\Homework_file\Homework_1\recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for recipes in file:
        dish_name = recipes.strip()
        cook_ingridient = int(file.readline())
        cook_list = []
        for i in range(cook_ingridient):
            ingridient_name, quantity, measure = file.readline().strip().split('|')
            cook_list.append({ 'ingridient_name': ingridient_name, 'quantity': quantity, 'measure': measure })
        file.readline()

        cook_book[dish_name] = cook_list


for key, value in cook_book.items():
    print(f'\n{key}\n')
    for key in value:
        print(f'{key}')
print()