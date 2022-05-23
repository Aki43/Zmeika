import random
bank = int(input('''\t\tВас приветсвует мое CASINO
Это рулетка с диапазоном от 1 до 10
Красное - четное и черное - нечетное
Если вы угадали цифру, мы увеличим вашу ставку в 9 раз
Если угадали цвет, то увеличим ставку в 2 раза
\t\t Удачи, сынок
Ваш баланс: 
'''))
while True:
    stavka = int(input('Ваше число: '))
    stavka_money = int(input('Ваша ставка на число: '))
    color = input('Выберети цвет red or black: ')
    color_money = int(input('Ваша ставка на цвет: '))

    all_money = bank - stavka_money - color_money
    CASINO = random.randint(1,10)
    print('Шар попал на цифру',CASINO)
    bank -= stavka_money
    bank -= color_money

    if bank >= 0 and CASINO == stavka:
        stavka_money *= 9
        bank += stavka_money
        print('Наконец вы ВЫЙГРАЛИ\nВаш выигрыш: ',stavka_money,
        'Баланс составляет: ', bank)

    elif bank >= 0 and CASINO != stavka and stavka < 11 and stavka > 0:
        print('''Попробуйте еще раз, 
Ваш остаток на счете''', bank)
    elif bank >= 0 and CASINO != stavka and stavka < 1 or stavka > 10:
        bank += stavka_money
        print('Вы ввели неправильное значение. Не забываем про диапазон от 1 до 10\nВаш остаток на счете', bank)
    else:
        bank == 0
        print('недостаточно средств')

#2й блок
    red = CASINO % 2
    if bank >= 0 and color == 'red' and red == 0:
        color_money *= 2
        bank += color_money
        print('с цветом ты угадал Выигрыш', color_money, 'твой баланс', bank)
    elif bank >= 0 and color == 'black' and red != 0:
        color_money *= 2
        bank += color_money
        print('с цветом ты угадал Выигрыш', color_money, 'твой баланс', bank)
    elif bank >= 0 and color != 'red' and color != 'black':
        bank += color_money
        print('Ошибка ввода цвета')



