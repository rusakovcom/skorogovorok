import random
print("Для Вас будут выводится случайные скороговорки из базы. Нажмите клавишу enter (с любым, например, пустым вводом) для печати следующей скороговорки или введите exit с нажатием enter для выхода из программы")
a = input()
while a != 'exit':
    if a != 'exit':
        line = random.choice(open('list.txt').readlines())
        print(line)
        a = input()
    else:
        print("Досвидос")