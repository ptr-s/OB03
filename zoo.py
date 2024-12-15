"""
Задание
1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
   (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые
   наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
   если требуется (например, различный звук для `make_sound()`).

3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая
   принимает список животных и вызывает метод `make_sound()` для каждого животного.

4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
   о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут
   иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()`
   для `Veterinarian`).

Дополнительно:
Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации
о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние"
между запусками программы.
"""

#=========================================
# Animals

class Animals:
    def __init__(self, animals_list: []):
        self.__items = []
        self.__animals = animals_list

    def show(self):
        print(f"Животных в зоопарке: {len(self.__items)}")
        for i, animal in enumerate(self.__items):
            print(f"{i}. ", end='')
            animal.info()

    def accept(self, **animal):
        pass

    def release(self, animal_number: int):
        if 0 <= animal_number < len(self.__items):
            message = f"Животное '{self.__items[animal_number].name}' - отпущено"
            del self.__items[animal_number]
            print(message)
        else:
            print(f"Животное c №{animal_number} не найдено")


class Animal:
    __biology_class = None

    def __init__(self, species, nickname, age, voice, food):
        self.species = species
        self.nickname = nickname
        self.age = age
        self.voice = voice
        self.food = food

    @staticmethod
    def get_biology_class():
        return Animal.__biology_class

    def get_my_biology_class(self):
        return self.__biology_class

    def make_sound(self):
        print(f"{self.species} '{self.nickname}' {self.voice}")

    def eat(self):
        print(f"{self.species} '{self.nickname}' ест {self.food}")

    def make_move(self):
        pass

    def info(self):
        pass

    def load(self, data: {}):
        pass

    def save(self):
        pass

class Bird(Animal):
    __biology_class = "Птицы"

    def __init__(self, species, nickname, age, voice, food, wingspan):
        super().__init__(species, nickname, age, voice, food)
        self.wingspan = wingspan

    @staticmethod
    def get_biology_class():
        return Bird.__biology_class

    def make_move(self):
        print(f"{self.species} '{self.nickname}' летает по вольеру")

class Mammal(Animal):
    __biology_class = "Млекопитающие"

    def __init__(self, species, nickname, age, voice, food, weight):
        super().__init__(species, nickname, age, voice, food)
        self.weight = weight

    @staticmethod
    def get_biology_class():
        return Mammal.__biology_class

    def make_move(self):
        print(f"{self.species} '{self.nickname}' ходит по вольеру")

class Reptile(Animal):
    __biology_class = "Пресмыкающиеся"

    def __init__(self, species, nickname, age, voice, food, length):
        super().__init__(species, nickname, age, voice, food)
        self.length = length

    @staticmethod
    def get_biology_class():
        return Reptile.__biology_class

    def make_move(self):
        print(f"{self.species} '{self.nickname}' ползает по террариуму")

#=========================================
# Staff

class Staff:
    def __init__(self, job_list: []):
        self.__items = []
        self.__jobs = job_list

    def show(self):
        print(f"Сотрудников в зоопарке: {len(self.__items)}")
        for i, employee in enumerate(self.__items):
            print(f"{i}. ", end='')
            employee.info()

    def hire(self, **employee):
        job_class = employee['job_class']
        job_title = employee['job_title']
        name = employee['name']
        # if job_class and job_class in self.__jobs:
        #     print("")
        # elif job_title and in [for item in ]
        # else:
        #     print("")

    def fire(self, employee_number: int):
        if 0 <= employee_number < len(self.__items):
            message = f"Сотрудник {self.__items[employee_number].name} - сокращён"
            del self.__items[employee_number]
            print(message)
        else:
            print(f"Сотрудника с №{employee_number} не найдено")

    def load(self, data: {}):
        pass

    def save(self):
        pass


class Employee:
    __job_title = None

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_job_title():
        return Employee.__job_title

    def info(self):
        print(f"{self.name} - {self.get_job_title}")

    def action(self, animal):
        pass

    def load(self, data: {}):
        pass

    def save(self):
        pass

class ZooKeeper(Employee):
    __job_title = "Смотритель зоопарка"

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_job_title():
        return ZooKeeper.__job_title

    def action(self, animal: Animal):
        print(f"{self.get_job_title} {self.name} кормит животное: {animal.species} '{animal.nickname}'")

class Veterinarian(Employee):
    __job_title = "Ветеринар"

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_job_title():
        return Veterinarian.__job_title

    def action(self, animal: Animal):
        print(f"{self.get_job_title} {self.name} лечит  животное: {animal.species} '{animal.nickname}'")

#=========================================
# Zoo

class Zoo:
    def __init__(self):
        self.staff = Staff([ZooKeeper, Veterinarian])
        self.animals = Animals([Bird, Mammal, Reptile])

    def load(self, file_name: str):
        pass

    def save(self, file_name: str):
        pass

#=========================================

FILE_NAME = "zoo.json"

def main():
    zoo = Zoo()
    zoo.load("FILE_NAME")
    try:
        if not zoo.staff and not zoo.animals:
            # Значение по умолчанию
            # Сотрудники
            zoo.staff.hire(job_class=ZooKeeper, name="Семён Семёныч")
            zoo.staff.hire(job_class=Veterinarian, name="Наталья Юрьевна")
            # Животные
            zoo.animals.accept(animal_class=Bird, species="Филин", nickname="Соня", age=27, voice="ухает", food="мышь", wingspan=1.3)
            zoo.animals.accept(animal_class=Mammal, species="Бурый медведь", nickname="Потапыч", age=21, voice="рычит", food="мясо", weight=250)
            zoo.animals.accept(animal_class=Mammal, species="Белый медведь", nickname="Умка", age=18, voice="рычит", food="мясо", weight="400")
            zoo.animals.accept(animal_class=Reptile, species="Королевская кобра", nickname="Наг", age=27, voice="шипит", food="мышь", length=3.5)

        zoo.staff.show()
        print(" ")
        zoo.animals.show()
        """
        while True:
            print("\nУправление зоопарком."
                  f"Сотрудников в зоопарке: {len(zoo.employees)}"
                  f"Животных в зоопарке: {len(zoo.animals)}"
                  "Выберите задачу:")
            print("1. Список сотрудников")
            print("2. Нанять сотрудника")
            print("3. Сократить сотрудника ")
            print("4. Список животных")
            print("5. Приобрести животное")
            print("6. Отпустить животное")
            print("7. Посмотреть что твориться в зоопарке")
            print("0. Выход")

            try:
                choice = int(input("Введите номер задачи: "))

                if choice == 0:
                    print("Завершение программы.")
                    break
                elif choice == 1:
                    pass
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    pass
                elif choice == 5:
                    pass
                else:
                    print("Неверный выбор. Попробуйте снова.")

            except ValueError:
                print("Ошибка: Введите числовое значение.")
             """
    finally:
        zoo.save("FILE_NAME")
        pass


if __name__ == "__main__":
    main()
