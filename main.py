# temp = int(input('Введите температуру в F '))
# print(f'{temp} градусов по Фаренгейту равняется {(temp - 32)*5/9}')


# num = int(input('Введите число'))
# if num % 3 != 0 :
#     print(f'Число {num} не кратно 3')
# else:
#     print(f'Число {num} кратно 3')



#print(f'Количнство полных килограмм = { int(input("Введите количество грамм ")) //1000 }')


# print(f'Последняя цифра чилса= {int(input("Введите число ")) % 10}')


##########################################################


#Задача 1. Добавление элемента в список

# numbers = []
# print(f'{numbers.append(input("Введите новый элемент списка"))} {numbers}')


#Задача 2. Удаление элемента из списка

# lst = ['Moscow', 'London', 'Paris', 'St. Petersburg']
#
# lst2 = lst
# lst2.remove('London')
#
# print(f'Исходный список равен {lst} \nОбновленный список равен {lst2}')



#Задача 3. Доступ к элементу индекса

# lst = ['Moscow', 'London', 'Paris', 'St. Petersburg']
# print(f'Элемент с индексом 2 = {lst[2]}')


#Задача 4. Доступ к элементу среза

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f'Элементы среза [3:7] = {numbers[3:7]}')


#Задача 5. Изменение элемента списка

# colors = ['red', 'green', 'blue', 'black']
# colors_yellow = colors.copy()
#
# colors_yellow[2] = 'yellow'
# print(f'Исходный список {colors} \nИзмененный список {colors_yellow}')



#Задача 6. Узнаем длинну списка

# animals = ['cat', 'dog', 'rabbit', 'hamster']
# print(f'Длинна списка animals = {len(animals)}')

#Задача 7. Добавление элемента в словарь

# student = {
#     'name' : 'Ivan',
#     'age' : 20
# }
#
# student['grade'] = 'A'
#
# print(student)


#Задача 8. Изменение элемента словаря

# student = {
#     'name' : 'Ivan',
#     'age' : 20,
#     'grade' : 'B'
# }
#
# student['grade'] = 'A'
#
# print(student)

#Задача 9. Удаление элемента из словаря

# student = {
# #     'name' : 'Ivan',
# #     'age' : 20,
# #     'grade' : 'B'
# # }
# #
# # del student['age']
# #
# # print(student)


#Задача 10. Доступ к элементу словаря по ключу

# student = {
#     'name' : 'Ivan',
#     'age' : 20,
#     'grade' : 'B'
# }
#
# print(student['name'])



#Задача 11. Проверка наличия ключу в словаре

# student = {
#     'name' : 'Ivan',
#     'age' : 20,
#     'grade' : 'B'
# }
#
# if 'grade' in student:
#     print('Ключ найден')
# else:
#     print('Ключ не найден')



#Задача 12. Изменение элемента во вложенном словаре

# student = {
#     'name' : 'Ivan',
#     'adress' : {
#         'city' : 'Moscow',
#         'street' : 'Lenina'
#     }
# }
#
# student['adress']['city'] = 'St. Petersburg'
#
# print(student)



#Задача 13. Изменнеи элемента в списке, находящемся в словаре

# student = {
#     'name' : 'Marina',
#     'grades': [85, 90, 105]
# }
#
# student['grades'][0] = 20
#
# print(student)



#Задача 14. Изменение элемента в словаре, находящемся внутри списка

# student = [
#     {
#         'name' : 'Ivan',
#         'age' : 22
#     },
#     {
#         'name' : 'Petya',
#         'age' : 25
#     }
# ]
#
# student[1]['age'] = 1
# print(student)


#Задача 15. Проверка наличия элемента и определение длинны кортежа

colors = ('red', 'green', 'blue')

if 'green' in colors:
    print(f'Наличие "green" = {True} \nДлинна кортежа = {len(colors)}')
else:
    print(f'Наличие "green" = {False} \nДлинна кортежа = {len(colors)}')
