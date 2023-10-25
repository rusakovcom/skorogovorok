import random
n = int(input('Сколько скороговорок вывести?: (Enter - показать следующую)\n'))
a = '' # переменная для перехода к сл. скороговорке при нажатии enter в цикле for
for i in range(n):
        print('\n', random.choice(open('list.txt').readlines()), '\n',  '_____________________________')
        a = input()
