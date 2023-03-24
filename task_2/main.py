'''
Задача 18: Требуется найти в массиве A[1..N]
самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N –
количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
'''

n = int(input('Введите максимальный элемент последовательности чисел от 1: '))
n_list = list(range(1, n + 1, 3))
print(n_list)
k = int(input('Введите число которое требуется найти в массиве: '))
if k in n_list:
    print(f'Число {k} находится в массиве по индексу {n_list.index(k)}')
else:
    closest_value = n_list[0]
    for i in range(len(n_list)):
        if n_list[i] // k < 1:
            if abs(n_list[i] - k) < abs(n_list[i + 1] - k):
                closest_value = n_list[i]
            else:
                closest_value = n_list[i + 1]
    print(closest_value)

