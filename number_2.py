# Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
# пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

# комментарии писать нет смысла, думаю, что тут все понятно
class OwnZeroDivError(ZeroDivisionError):
    def __str__(self):
        return "На нуль делить нельзя!"

    @staticmethod
    def division(x, y):
        try:
            if y == 0:
                raise OwnZeroDivError()
            return x / y
        except OwnZeroDivError as err:
            return err

while True:
    try:
        a = int(input('Введите делимое: '))
        b = int(input('Введите делитель (попробуйте ввести 0): '))
    except Exception:
        print('Вы ввели не число! Попробуйте еще раз!')
    else:
        print(OwnZeroDivError.division(a, b))
        break