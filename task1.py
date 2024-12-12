# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Garden:
    def __init__(self, occupied_territory: float, plant_species: list, number_of_plants: int):
        """
        Создание и подготовка к работе объекта "Сад"

        :param occupied_territory: Площадь территории сада
        :param plant_species: Виды растений в саду
        :param number_of_plants: Количество растений в саду

        Примеры:
        >>> moms_garden = Garden(300,['tulip','rose','lily'], 60)  # инициализация экземпляра класса
        """
        if not isinstance(occupied_territory, (int, float)):
            raise TypeError("Площадь сада должна быть типа int или float")
        if occupied_territory <= 0:
            raise ValueError("Площадь сада должна быть положительным числом")
        self.occupied_territory = occupied_territory

        if not isinstance(plant_species, (str,list)):
            raise TypeError("Виды растений должны быть str или list")
        self.plant_species = plant_species

        if not isinstance(number_of_plants, (int)):
            raise TypeError("Количество цветов должно быть int")
        if number_of_plants < 0:
            raise ValueError("Количество цветов не может быть отрицательным числом")
        self.number_of_plants = number_of_plants

    def planting(self, plants: int) -> None:
        """
        Посадка растений.
        :param plants: Количество сажаемых цветов

        Примеры:
        >>> moms_garden = Garden(300,['tulip','rose','lily'], 60)
        >>> moms_garden.planting(4)
        """
        if not isinstance(plants, (int)):
            raise TypeError("Количество сажаемых цветов должнo быть типа int")
        if plants < 0:
            raise ValueError("Количество сажаемых цветов должнo быть положительным числом")
        ...

    def digging_up_plants(self, digged_plants: int) -> None:
        """
        Выкапывание растений.
        :param digged_plants: Количество выкапываемых цветов
        :raise ValueError: Если количество выкапываемых цветов превышает количество цветов в саду, то возвращается ошибка.

        Примеры:
        >>> moms_garden = Garden(300,['tulip','rose','lily'], 60)
        >>> moms_garden.digging_up_plants(3)
        """
        if not isinstance(digged_plants, (int)):
            raise TypeError("Количество выкапываемых цветов должнo быть типа int")
        if digged_plants < 0:
            raise ValueError("Количество выкапываемых цветов должнo быть положительным числом")
        ...


class Bakery:
    def __init__(self, row_bread: int, cooked_bread: int):
        """
        Создание и подготовка к работе объекта "Пекарня"

        :param row_bread: Количество сырого хлеба
        :param cooked_bread: Количество приготовленного хлеба

        Примеры:
        >>> bakery = Bakery(13,30)  # инициализация экземпляра класса
        """
        if not isinstance(row_bread, (int)):
            raise TypeError("Количество сырого хлеба должно быть типа int")
        if row_bread < 0:
            raise ValueError("Количество сырого хлеба не может быть отрицательным числом")
        self.row_bread = row_bread

        if not isinstance(cooked_bread, (int)):
            raise TypeError("Количество приготовленного хлеба должно быть типа int")
        if cooked_bread < 0:
            raise ValueError("Количество приготовленного хлеба не может быть отрицательным числом")
        self.cooked_bread = cooked_bread

    def preparing_row_bread(self, preparation: int) -> None:
        """
        Заготовка сырого хлеба.
        :param preparation: Количество заготаливаемого хлеба

        Примеры:
        >>> bakery = Bakery(13,30)
        >>> bakery.preparing_row_bread(11)
        """
        if not isinstance(preparation, (int)):
            raise TypeError("Количество заготаливаемого хлеба должнo быть типа int")
        if preparation < 0:
            raise ValueError("Количество заготаливаемого хлеба должнo быть положительным числом")
        ...

    def baking_bread (self, breads: int) -> None:
        """
        Выпекание хлеба.
        :param breads: Количество выпекаемого хлеба
        :raise ValueError: Если количество выпекаемого хлеба больше количества сырого хлеба, то возвращается ошибка.

        Примеры:
        >>> bakery = Bakery(13,30)
        >>> bakery.baking_bread(6)
        """
        if not isinstance(breads, (int)):
            raise TypeError("Количество выпекаемого хлеба должнo быть типа int")
        if breads < 0:
            raise ValueError("Количество выпекаемого хлеба должнo быть положительным числом")
        ...

    def sale (self, breads_for_sale: int) -> None:
        """
        Продажа хлеба.
        :param breads_for_sale: Количество продаваемого хлеба
        :raise ValueError: Если количество продаваемого хлеба больше количества приготовленного хлеба, то возвращается ошибка.

        Примеры:
        >>> bakery = Bakery(13,30)
        >>> bakery.sale(10)
        """
        if not isinstance(breads_for_sale, (int)):
            raise TypeError("Количество продаваемого хлеба должнo быть типа int")
        if breads_for_sale < 0:
            raise ValueError("Количество продаваемого хлеба должнo быть положительным числом")
        ...


class IKIZI:
    def __init__(self, students: int, students_on_dopsa: int):
        """
        Создание и подготовка к работе объекта "ИКИЗИ"

        :param students: Количество студентов в институте
        :param students_on_dopsa: Количество студентов на допсе

        Примеры:
        >>> VSHK = IKIZI(187,150)  # инициализация экземпляра класса
        """
        if not isinstance(students, (int)):
            raise TypeError("Количество студентов в институте должно быть типа int")
        if students < 0:
            raise ValueError("Количество студентов в институте не может быть отрицательным числом")
        self.students = students

        if not isinstance(students_on_dopsa, (int)):
            raise TypeError("Количество студентов на допсе должно быть типа int")
        if students_on_dopsa < 0:
            raise ValueError("Количество студентов на допсе не может быть отрицательным числом")
        self.students_on_dopsa = students_on_dopsa

    def otpravit_na_dopsu(self, dopsa: int) -> None:
        """
        Отправить студентов на допсу.
        :param dopsa: Количество студентов, которых отправляют на допсу
        :raise ValueError: Если количество студентов, отправляемых на допсу, превышает количество всех студентов, то вызывается ошибка

        Примеры:
        >>> VSHK = IKIZI(187,150)
        >>> VSHK.otpravit_na_dopsu(11)
        """
        if not isinstance(dopsa, (int)):
            raise TypeError("Количество студентов, которых отправляют на допсу, должнo быть типа int")
        if dopsa < 0:
            raise ValueError("Количество студентов, которых отправляют на допсу, должнo быть положительным числом")
        ...

    def otchislenie(self, pressF: int) -> None:
        """
        Отправить студентов на допсу.
        :param pressF: Количество отчисляемых студентов
        :raise ValueError: Если количество отчисляемых студентов превышает количество всех студентов, то вызывается ошибка

        Примеры:
        >>> VSHK = IKIZI(187,150)
        >>> VSHK.otchislenie(100)
        """
        if not isinstance(pressF, (int)):
            raise TypeError("Количество отчисляемых студентов должнo быть типа int")
        if pressF < 0:
            raise ValueError("Количество отчисляемых студентов должнo быть положительным числом")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
