number = int(input('Введите номер месяца'))
if number < 1 or number > 12:
    print('Такого месяца нет')
else:
    number=number-1
    month = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
    month_day =(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print('Вы ввели', month[number],'. ', month_day[number],'дней')


# Да, но зачем создавать два кортежа. Можно же просто все в словарь объеденить)

m = int(input('Введите номер месяца и нажмите Enter: '))
months = {1:'январь, 31 день', 2:'февраль, 28 дней', 3:'март, 31 день', 4:'апрель, 30 дней', 5:'май, 31 день', 6:'июнь, 30 дней', 7 :'июль, 31 день', 8 : 'август, 31 день', 9 :'сенябрь, 30 дней', 10 :'октябрь, 31 день', 11 :'ноябрь, 30 дней', 12 :'декабрь, 31 день'}

if m in months:
    print(f"Вы ввели {months[m]}")
else:
    print('Такого месяца нет!')
