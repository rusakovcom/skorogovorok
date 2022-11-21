import random
import time
n = int(input('Сколько всего скороговорок вывести?\n'))
t = int(input('Введите время паузы (с) между скороговорками: \n(или цифру 0 для вывода каждой следующей скороговорки вручную клавишей enter)\n'))
a = '' # переменная для перехода к сл. скороговорке при нажатии enter в цикле for
if t == 0:
        for i in range(n):
                print('\n', random.choice(open('list.txt').readlines()), '\n',  '_____________________________')
                a = input()

else:
        for i in range(n):
                print('\n', random.choice(open('list.txt').readlines()), '\n',  '_____________________________')
                time.sleep(t)
