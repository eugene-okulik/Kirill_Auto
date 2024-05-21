str_1 = 'результат операции: 42'
str_2 = 'результат операции: 514'
str_3 = 'результат операции: 9'


colon_index_1 = str_1.index(':')
colon_index_2 = str_2.index(':')
colon_index_3 = str_3.index(':')

number_1 = int(str_1[colon_index_1 + 2:]) + 10
number_2 = int(str_2[colon_index_2 + 2:]) + 10
number_3 = int(str_3[colon_index_3 + 2:]) + 10

#print(number_1)
#print(number_2)
#print(number_3)

print(f"Результат сложения: {number_1} {number_2} {number_3}")
