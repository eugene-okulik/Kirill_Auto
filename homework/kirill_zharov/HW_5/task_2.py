str_1 = 'результат операции: 42'
str_2 = 'результат операции: 514'
str_3 = 'результат работы программы: 9'


list_1 = str_1.split(': ')
list_2 = str_2.split(': ')
list_3 = str_3.split(': ')

result_1 = int(list_1[1]) + 10
result_2 = int(list_2[1]) + 10
result_3 = int(list_3[1]) + 10

print(result_1)
print(result_2)
print(result_3)
