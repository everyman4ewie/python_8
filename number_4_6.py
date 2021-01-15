# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие
# для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за
# приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class MyErr(ValueError):
    def __init__(self, txt):
        self.txt = txt

class OfficeEquipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} цена {self.price}'

class StoreWarehouse:
    def __init__(self, name):
        self.name = name
        self.my_stocks = {}

    def __str__(self):
        result = f'Количество товаров - {self.name} \n'
        for necessary, available in self.my_stocks.items():  # необходимое и имеющееся количество товаров
            result = result + f'Количество = {available} (шт.) - {necessary}  \n'
        return result

    # Получаю товар на склад
    def reception(self, necessary):
        try:  # делаю проверку на ввод
            available = input(f'Введите количество товара ({necessary.type}ов) передаваемого на {self.name}: ')
            if available.isdigit():
                available = int(available)
            else:
                raise MyErr("Ошибка ввода данных! Попробуйте еще раз")

            self.my_stocks[necessary] = available  # определяю количество товаров
        except MyErr as err:
            print(err)
            return StoreWarehouse.reception(self, necessary)

    # Передача в трансфер
    def transfer(self, store, necessary):  # сопоставляю значение склада и магазина.
        try:
            available = input(f'Введите количество товара ({necessary.type}ов) передаваемого в {store.name}: ')
            if available.isdigit():
                available = int(available)
            else:
                raise MyErr("Вы ввели не число! Попробуйте еще раз!")

            if self.my_stocks[necessary] - available < 0:  # если на складе не хватает товара, то прошу ввести меньшее количество
                raise MyErr("Не хватает товара на складе! Попробуйте уменьшить количество товара!")
            else:
                self.my_stocks[necessary] = self.my_stocks[necessary] - available  # если все ОК, то выдаю товар со склада в магазин
                store.my_stocks[necessary] = available
        except MyErr as err:
            print(err)
            return StoreWarehouse.transfer(self, store, necessary)

# задаю тип элементов, которые будут на складе. Тут можно добавить сколько угодно товаров.
# По идее если их будет больше, то их лучше загнать в другой файл и вызывать оттуда, иначе загромождение кода будет.
# скину еще 2 файла дополнительно, там будет показано. Файл с именем main.py и numbers4.py
# (это чисто для удобства, хотя, возможно, в этом нет особо смысла)

class Printer(OfficeEquipment):
    def __init__(self, name, price, printer_view):
        super().__init__(name, price)
        self.printer_view = printer_view
        self.type = 'принтер'

    def to_print(self):
        return f'Печатаем текст на принтере {self.name}'

    def __str__(self):
        return super().__str__() + f', тип принтера = {self.printer_view}'


class Scanner(OfficeEquipment):
    def __init__(self, name, price, document_size):
        super().__init__(name, price)
        self.document_size = document_size
        self.type = 'сканер'

    def to_scan(self):
        return f'Сканируем текст на сканере {self.name}'

    def __str__(self):
        return super().__str__() + f', размер бумаги = {self.document_size}'


class Copier(OfficeEquipment):
    def __init__(self, name, price, copy_speed):
        super().__init__(name, price)
        self.copy_speed = copy_speed
        self.type = 'ксерокс'

    def to_copier(self):
        return f'Копируем текст на ксероксе {self.name}'

    def __str__(self):
        return super().__str__() + f', скорость печати = {self.copy_speed}'


my_store = StoreWarehouse('Мой магазин')
my_warehouse = StoreWarehouse('Мой склад')
printer_1 = Printer('Samsung', 1800, 'Лазерный')
scanner_2 = Scanner('Canon', 570, 'А4')
copier_3 = Copier('Xerox', 1200, '29 стр/мин')

print(printer_1)
print(scanner_2)
print(copier_3)

my_warehouse.reception(printer_1)
my_warehouse.reception(scanner_2)
my_warehouse.reception(copier_3)
print(my_warehouse)

my_warehouse.transfer(my_store, printer_1)
my_warehouse.transfer(my_store, scanner_2)
my_warehouse.transfer(my_store, copier_3)
print(my_warehouse)
print(my_store)

print(printer_1.to_print())
print(scanner_2.to_scan())
print(copier_3.to_copier())