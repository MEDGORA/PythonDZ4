"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены 
только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте 
выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и
нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
"""
n = int(input('Введите количество кустов N: '))
list1 = [] 
i = 0
for i in range(n) :
  print('Введите количество ягода на',i + 1,'-м кусте')
  list1.append(int(input()))

list2 = [] 
sum = 0

for i in range(n) :
    if i == len(list1) - 1 :
        sum = list1[i-1]+list1[i]+list1[0]
    else :
        sum = list1[i-1]+list1[i]+list1[i+1]
    list2.append(sum)

print('Номер куста',list2.index(max(list2))+1)