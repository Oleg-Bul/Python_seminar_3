# Задайте список. Напишите программу, которая определит,
#  присутствует ли в заданном списке строк некое число.
# Пример:
# ['114411', 'sjngsjgng', '123fsghs'] -> No
# ['12', 12] -> Yes

List = ['114411', 'sjngsjgng', 123]
j = 0
for i in range(len(List)):
    if type(List[i]) == int or type(List[i]) == float:
        print("Элемент ", i, "- число")
        j += 1
if j == 0:
    print("Среди элементов нет чисел.")

# можно и так
# mass = ['ssss', 'sngujn556', 44]
# types = [str(type(i)) for i in mass]
# if "<class 'int'>" in types or "<class 'float'>" in types:
#     print('Yes')
# else:
#     print('No')

