spisok = []
command = ''

while True:
    x = input()
    if x != 'stop':
        spisok.append(x)
        print(spisok)
    else:
        print('Останавливаю добавление! Вот Ваш отсортированный список')
        spisok.sort()
        print(spisok)