class Transport:
    """Базовый класс для всех транспортных средств."""

    def __init__(self, make: str, model: str, year: int):
        """Конструктор базового классa Transport.

        Args:
            make (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска транспортного средства.
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        """Возвращает строковое представление транспортного средства."""
        return f"{self.make} {self.model} ({self.year})"

    def __repr__(self):
        """Возвращает представление транспортного средства в формате Python."""
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r})"


class Bus(Transport):
    """Дочерний класс для автобусов."""

    def __init__(self, make: str, model: str, year: int, seats: int):
        """Конструктор дочернего класса Bus.

        Args:
            make (str): Марка автобуса.
            model (str): Модель автобуса.
            year (int): Год выпуска автобуса.
            seats (int): Количество мест в автобусе.
        """
        super().__init__(make, model, year)
        self.seats = seats

    def __str__(self):
        """Возвращает строковое представление автобуса."""
        return super().__str__() + f" с {self.seats} местами"

    def get_seats(self) -> int:
        """Возвращает количество мест в автобусе.

        Returns:
            int: Количество мест.
        """
        return self.seats


if __name__ == "__main__":
    # Создаем экземпляр класса Transport
    transport1 = Transport("УАЗ", "Патриот", 2021)

    # Создаем экземпляр класса Bus
    bus1 = Bus("ГАЗ", "Газель", 2019, 8)

    # Выводим строковые представления объектов
    print(transport1)  # УАЗ Патриот (2021)
    print(bus1)  # ГАЗ Газель (2019) с 8 местами

    # Получаем количество дверей у автомобиля
    seats = bus1.get_seats()
    print(f"Количество мест у автобуса: {seats}")
