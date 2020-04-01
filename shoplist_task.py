shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать', len(shoplist), "покупок")

print("Покупки:", end=" ")
for item in shoplist:
    print(item, end=" ")

while len(shoplist) >= 0:
    if len(shoplist) == 0:
        print("Я все купил!!!")
        break
    olditem = shoplist[0]
    del shoplist[0]
    print('\nЯ купил', olditem)
    print('Теперь мой список:', shoplist)