
import matplotlib.pyplot as plt
import numpy as np
import scipy. interpolate
import getch


#№значение функции
def count_function(xs, func):
    ys = []

    for i in range(len(xs)):
        x = xs[i]
        ys.append(eval(func))
    return ys


##максимальное отклонение
def count_raznosti(iy, fy):
    raznosti = [[0, 0, 0]]
    k = 0

    for i in range(len(iy)):
        r = fy[i] - iy[i]
        if abs(r) > abs(raznosti[0][2]):
            raznosti[0][2] = r
            raznosti[0][0] = i
            raznosti[0][1] = fy[i]

    for i in range(len(iy)):
        r = fy[i] - iy[i]
        if abs(r) == abs(raznosti[0][2]) and i != raznosti[0][0]:
            raznosti.append([])
            k += 1
            raznosti[k].append(i)
            raznosti[k].append(fy[i])
            raznosti[k].append(r)

    return raznosti


def h_calc():
    for i in range(len(x1)-1):
        h[i] = x1[i + 1] - x1[i]

def c_calc():
    for i in range(len(h)):
         = 6 *  

##вывод значений
def print_table(st):
    for i in range(len(st)):
        drop = 3
        print(str(st[i]), end = "")
        
        if abs(st[i]) >= 100:
            drop = drop - 2
        elif abs(st[i]) >= 100:
            drop = drop - 1
        for g in range (drop):
          print(" ", end = " ")
    print("\n")


x1 = []
x_ = []
y1 = []
y_ = []
h = []

##чтение файла со значениями
with open("file.txt", "r") as file:
    temp = file.readline()
    x1 = [float(t) for t in temp.split()]
    x1.sort()
    temp = file.readline()
    y1 = [float(t) for t in temp.split()]
    y1.sort()
    temp = file.readline()
    x_ = [float(t) for t in temp.split()]
    x_.sort()       ##сортировка значений в массиве
    
file.close()   ##закрытие файла

print("Значения X:    ", end = "")
print_table(x1)
print("Значения Y:    ", end = "")
print_table(y1)
temp = float(input("Введите значение X: "))      ##ввод значения
  

print("\n\nВведите функцию: ", end = "")        ##ввод функции для построения

funciya = input()
for i in range(len(x_)):
    x = float(x_[i])
    y_.append(eval(funciya))
    print('x = ', x_[i], '   y = ', y_[i], sep='')


f = []
neuton(x_, y_, f)

##Построение графика
x = np.arange(x_[0], x_[len(x_) - 1], 0.001)

#cou_neut = count_neuton(x, f, x_)
#plt.plot(x, cou_neut, 'y')
#plt.plot(x, cou_neut, 'k')

#fy = count_function(x, funciya)
#plt.plot(x, fy, 'm', label=r'f(x)')

#plt.plot(x_, y_, 'bo')
#plt.grid(True)
#plt.legend(loc='best', fontsize=12)

#plt.xlabel(r'$x$', fontsize=14)
#plt.ylabel(r'$y$', fontsize=14)

raznosti = count_raznosti(count_splain, fy)

for i in range(len(raznosti)):
    raznosti[i][0] = x_[0] + raznosti[i][0] * 0.001
    ## plt.plot([raznosti[i][0], raznosti[i][0]], [raznosti[i][1], raznosti[i][1] - raznosti[i][2]], 'c')

print('\n\nМаксимальное отклонение: ', abs(raznosti[0][2]))
plt.show()