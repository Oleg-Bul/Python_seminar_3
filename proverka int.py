def input_correct_int():
    while True:
        try:
            return int(input())
            break
        except ValueError:
            print('Некорректный ввод')

a = input_correct_int()
print(a)
