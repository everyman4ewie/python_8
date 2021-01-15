# 7. Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число», реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


# вариант программы с выводом знаков идущих подряд(+-), если ввести все числа отрицательные.
def my_input1():
    a = int(input('Введите целую часть числа: '))
    return a

def my_input2():
    a = int(input('Введите комплексную часть числа: '))
    return a

class NumComplex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 'x + yi'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.x + other.x}+{self.y + other.y}i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.x * other.x - (self.x * other.y)}+{self.y * other.x}i'

    def __str__(self):
        return f'z = {self.x}+{self.y}i'

z_1 = NumComplex(my_input1(), my_input2())
z_2 = NumComplex(my_input1(), my_input2())
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)


# кривой вариант той же программы с выводом без знаков идущих подряд(+-)
# def my_input1():
#     a = int(input('Введите целую часть числа: '))
#     return a
#
# def my_input2():
#     a = int(input('Введите комплексную часть числа: '))
#     return a
#
# class NumComplex:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.z = 'x + yi'
#
#     def __add__(self, other):
#         print(f'Сумма z1 и z2 равна')
#         a = ' '
#         if self.y < 0:
#             a = '-'
#         else:
#             a = '+'
#         return f'z = {self.x + other.x}{a}{(abs(self.y + other.y))}i'
#
#     def __mul__(self, other):
#         print(f'Произведение z1 и z2 равно')
#         a = ' '
#         if self.y < 0:
#             a = '-'
#         else:
#             a = '+'
#         return f'z = {self.x * other.x - (self.x * other.y)}{a}{abs(self.y * other.x)}i'
#
#     def __str__(self):
#         a = ' '
#         if self.y < 0:
#             a = ''
#         else:
#             a = '+'
#         return f'z = {self.x}{a}{self.y}i'
#
# z_1 = NumComplex(my_input1(), my_input2())
# z_2 = NumComplex(my_input1(), my_input2())
# print(z_1)
# print(z_1 + z_2)
# print(z_1 * z_2)