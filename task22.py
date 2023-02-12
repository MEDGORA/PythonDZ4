"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""
n = int(input('Введите количество элементов в первом массиве n: '))
list1 = []
i = 0
for i in range(n) :
  print('Введите',i + 1,'-й элемент массива')
  list1.append(int(input()))

m = int(input('Введите количество элементов во вотором массиве m: '))
list2 = []
for i in range(m) :
  print('Введите',i + 1,'-й элемент массива')
  list2.append(int(input()))

list1_set = set(list1)
list2_set = set(list2)
intersection = list1_set.intersection(list2_set)
intersection = list(intersection)

min = intersection[0]
for i in range(len(intersection)) :
  if intersection[i] < min :
    intersection[i] = min
    intersection.pop(i)
    intersection.append(min)

print(intersection)

