# Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать
# два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например,
# месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


# комментарии писать нет смысла, думаю, что тут все понятно
class MyDay:
    def __init__(self, str_day):
        self.str_day = str_day

    @classmethod
    def number_day(cls, str_day):
        return [int(x) for x in str_day.split('-')]

    @staticmethod
    def check_data_day(day, month, year):
        result = ''
        if not (1 <= day <= 31):
            result = 'Такого дня не существует!'

        if not (1 <= month <= 12):
            result = 'Такого месяца не существует!'

        if not (0 <= year <= 2030):
            result = 'Этот год еще не наступил!'

        return result if result else 'Такая дата существует'

while True:
    try:
        my_day = int(input('Введите день: '))
        my_mounth = int(input('Введите месяц: '))
        my_year = int(input('Введите год: '))
    except Exception:
        print('Вы ввели не число! Попробуйте еще раз!')
    else:
        print(MyDay.number_day(f'{my_day}-{my_mounth}-{my_year}'))
        print(MyDay.check_data_day(my_day, my_mounth, my_year))
        break
