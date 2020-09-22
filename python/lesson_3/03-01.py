# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
#


def input_numbers():
    """
    Функция запроса данных от пользователя.
    :return:
    Вывод в виде кортежа 2-х действительных чисел
    """
    return float(input('Введите делимое: ')), float(input('Введите частное: '))


def div_num(x, y):
    """
    Функция, реализующая деление 2-х чисел
    :param x:
    :param y:
    :return:
    Вывод - частное, либо уведомление о делении на ноль
    """
    try:
        return x / y
    except ZeroDivisionError:
        return 'деление на ноль'
    # if y != 0:
    #     return x / y
    # else:
    #     return 'деление на ноль'


div_x, div_y = input_numbers()
print('Результат деления: ', div_num(div_x, div_y))