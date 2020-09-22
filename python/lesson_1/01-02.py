# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
#
# Здесь используется для форматирования f-строка с использованием дополнительных параметров
# для вывод 2-значного целого числа
# Также используется групповая операция присваивания для упрощения
#
t_sec = int(input('Введите время в секундах: '))
t_min, t_sec = t_sec // 60, t_sec % 60
t_hour, t_min = t_min // 60, t_min % 60
print(f'{t_hour:02d}:{t_min:02d}:{t_sec:02d}')
