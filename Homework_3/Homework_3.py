import os
import operator
from operator import itemgetter
from pprint import pprint

list_text = []
count_str = {}
text = {}
result = []
for x in os.listdir(r'C:\Users\Admen\Desktop\Netology Homework\Homework_Files\Homework_3'):
    if x.endswith('.txt'):
        with open(x, 'rt', encoding='utf-8') as file:
            list_text.append(x)
            count_str[x] = file.read().count('\n')+1
        with open(x, encoding='utf-8') as f:
            text[x] = f.read()
sort_count_str = {}
sort_key = sorted(count_str, key=count_str.get)

for i in sort_key:
    sort_count_str[i] = count_str[i]
for num_text in sort_count_str.keys():
    result.append(f'{num_text}\n{sort_count_str[num_text]}\n{text[num_text]}')
result = '\n'.join(result)

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(result)
