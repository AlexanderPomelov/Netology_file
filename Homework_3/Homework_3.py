

with open('1.txt', 'rt', encoding='utf-8') as file_1, open('2.txt', 'rt', encoding='utf-8') as file_2,\
        open('3.txt', 'rt', encoding='utf-8') as file_3:

    count_str_1, count_str_2, count_str_3 = file_1.readlines(), file_2.readlines(), file_3.readlines()


with open('result.txt', 'w' , encoding='utf-8') as result:
    result.write('2.txt' '\n')
    res_1, res_2, res_3 = len(count_str_2), len(count_str_1), len(count_str_3)
    result.write(f'{str(res_1)} \n')
    result.write(f'{"".join(count_str_2)} \n')
    result.write('1.txt' '\n')
    result.write(f'{str(res_2)} \n')
    result.write(f'{"".join(count_str_1)} \n')
    result.write('3.txt' '\n')
    result.write(f'{str(res_3)} \n')
    result.write(f'{"".join(count_str_3)} \n')

