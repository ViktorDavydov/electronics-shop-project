import csv


class InstantiateCSVError(Exception):
    """Родительский класс от Exception"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Item.all.append(self)

    def __repr__(self):
        """Magic method __repr__ initializing"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Magic method __str__ initializing"""
        return f"{self.__name}"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            total_sum = self.quantity + other.quantity
            return total_sum
        return f"Нельзя складывать объекты разных классов"

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """Class method creating for opening csv file and adding instances to new
        empty all list. Making an exceptions if csv is empty or broken"""
        cls.all = []
        try:
            with open(file_name) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls.all.append(cls(row["name"], row["price"], row["quantity"]))

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

        except KeyError:
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(string_num):
        """Static method creating for returning number from string"""
        if string_num.isdigit():
            return int(string_num)
        return float(string_num) // 1

    @property
    def name(self):
        """Class name getter"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Class name setter"""
        self.__name = new_name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
