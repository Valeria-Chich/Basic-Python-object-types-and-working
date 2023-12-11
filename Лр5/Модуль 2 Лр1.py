import doctest

class Rocket:
    """
    Документация на класс.
    Класс описывает моедль ракеты.
    """
    def __init__(self, purpose: str, engine_type: str, thrust: (int, float)):
        """
        Создание и подготовка к работе объекта "Ракета"

        :param purpose: Назначение ракеты
        :param engine_type: Тип двигательной установки ракеты
        :param thrust: Развиваемая тяга ракетой

        Примеры:
        >>> rocket = Rocket('баллистическая', 'ЖРД', 4050)  # инициализация экземпляра класса
        """
        if not isinstance(purpose, str):
            raise TypeError("Назначение ракеты должно записываться типом str")
        self.purpose = purpose

        if not isinstance(engine_type, str):
            raise TypeError("Вид двигательной установки должно записываться типом str")
        self.engine_type = engine_type

        if not isinstance(thrust, (int, float)):
            raise TypeError("Тяга ракеты должна быть типом int или float")
        if thrust < 0:
            raise ValueError("Тяга ракеты должна быть положительным числом")
        self.thrust = thrust

    def setting_the_number_of_steps(self, number_of_steps: int):
        """
        Задание количества ступеней на ракете.

        :param number_of_steps: Количесвто ступеней
        :raise ValueError: Если число задаваемых ступеней не положительно.

        Примеры:
        >>> rocket = Rocket('баллистическая', 'ЖРД', 4050)
        >>> rocket.setting_the_number_of_steps(2)
        """
        ...

    def changing_the_engine_type(self, new_engine_type: str):
        """
        Замена типа двигательной установки на ракете.

        :param new_engine_type: Новой тип двигателя на ракете
        :raise TypeError: Если тип двигателе задается не через str.

        Примеры:
        >>> rocket = Rocket('баллистическая', 'ЖРД', 4050)
        >>> rocket.changing_the_engine_type('РДТТ')
        """
        ...

class Laptop:
    """
    Документация на класс.
    Класс описывает моедль ноутбука.
    """
    def __init__(self, number_of_cores: (int, float), RAM: (int, float)):
        """
        Создание и подготовка к работе объекта "Ноутбук"

        :param number_of_cores: Количество ядер
        :param RAM: Оперативная память

        Примеры:
        >>> laptop = Laptop(2, 8)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_cores, (int, float)):
            raise TypeError("Количество ядер должно быть типом int или float")
        if number_of_cores < 0:
            raise ValueError("Количество ядер должно быть положительным числом")
        self.number_of_cores = number_of_cores

        if not isinstance(RAM, (int, float)):
            raise TypeError("Оперативная память должна быть типом int или float")
        if RAM < 0:
            raise ValueError("Оперативная память должна быть положительным числом")
        self.RAM = RAM

    def changing_the_number_of_cores(self, new_number_of_cores: int):
        """
        Изменение количества ядер.

        :param new_number_of_cores: Новое число ядер на ноутбуке
        :raise ValueError: Если новое количество ядер меньше изначального.

        :return: Новое значения величины количества ядер на ноутбуке.

        Примеры:
        >>> laptop = Laptop(2, 8)
        >>> laptop.changing_the_number_of_cores(4)
        """
        ...

    def filling_free_memory(self, free_memory: int):
        """
        Заполнение свободной памяти ноутбука.

        :param free_memory: Свободная память на ноутбуке
        :raise ValueError: Если новое значение свободной память превышает значение оперативную память.


        Примеры:
        >>> laptop = Laptop(2, 8)
        >>> laptop.filling_free_memory(6)
        """
        ...

class GetEngine:
    """
    Документация на класс.
    Класс описывает моедль реактивного двигателя.
    """
    def __init__(self, number_of_cameras: (int, float), propellant: str):
        """
        Создание и подготовка к работе объекта "Ноутбук"

        :param number_of_cameras: Количество камер сгорания в двигателе
        :param propellant: Топливная пара используемая в двигателе

        Примеры:
        >>> getengine = GetEngine(2, 'НДМГ и АК-27')  # инициализация экземпляра класса
        """
        if not isinstance(number_of_cameras, (int, float)):
            raise TypeError("Количество ядер должно быть типом int или float")
        if number_of_cameras < 1:
            raise ValueError("Количество ядер должно быть положительным числом")
        self.number_of_cameras = number_of_cameras

        if not isinstance(propellant, str):
            raise TypeError("Топливная пара должна записываться типом str")
        self.propellant = propellant

    def adding_a_camera(self, new_number_of_camera: int):
        """
        Изменение числа камер сгорания в двигателе.

        :param new_number_of_camera: Новое число камер сгорания
        :raise ValueError: Если новое количество камер меньше предыдущего.

        :return: Новое значения числа камер сгорания в реактивном двигателе.

        Примеры:
        >>> getengine= GetEngine(2, 'НДМГ И АК-27')
        >>> getengine.adding_a_camera(4)
        """
        ...

    def adding_steering_engines(self, steering_engines: int):
        """
        Добавление рулевых двигателей в систему.

        :param steering_engines: Число рулевых двигателей
        :raise ValueError: Если задаваемое число рудевых двигателей отрицательное и нечётное.

        Примеры:
        >>> getengine= GetEngine(2, 'НДМГ И АК-27')
        >>> getengine.adding_steering_engines(2)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
