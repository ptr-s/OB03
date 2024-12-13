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

class Animal:
    def __init__(self, name, age, voice, food):
        self.name = name
        self.age = age
        self.voice = voice
        self.food = food

    def make_sound(self):
        print(f"{self.name} издаёт звук: {self.voice}")

    def eat(self):
        print(f"{self.name} ест {self.food}")

    def make_move(self):
        pass

    def info(self):
        pass

    def load(self, data: {}):
        pass

    def save(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, voice, food, wingspan):
        super().__init__(name, age, voice, food)
        self.wingspan = wingspan

    def make_move(self):
        print(f"{self.name} летает по вольеру")

class Mammal(Animal):
    def __init__(self, name, age, voice, food, weight):
        super().__init__(name, age, voice, food)
        self.weight = weight

    def make_move(self):
        print(f"{self.name} ходит по вольеру")

class Reptile(Animal):
    def __init__(self, name, age, voice, food, length):
        super().__init__(name, age, voice, food)
        self.length = length

    def make_move(self):
        print(f"{self.name} ползает по террариуму")

#=========================================
# Employees

class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    def info(self):
        print(f"{self.name} - {self.job_title}")

    def action(self, animal):
        pass

    def load(self, data: {}):
        pass

    def save(self):
        pass

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Смотритель зоопарка")

    def action(self, animal: Animal):
        print(f"{self.job_title} {self.name} кормит {animal.name}")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def action(self, animal: Animal):
        print(f"{self.job_title} {self.name} лечит {animal.name}")

#=========================================
# Zoo

class Zoo:
    def __init__(self):
        self.employees = []
        self.animals = []

    def show_employees(self):
        print(f"Сотрудников в зоопарке: {len(self.employees)}")
        for i, employee in enumerate(self.employees):
            print(f"{i}. ", end='')
            employee.info()

    def hire(self, employee: {}):
        pass

    def fire(self, employee_number: int):
        employee_number = int(employee_number)
        if 0 <= employee_number < len(self.employees):
            message = f"Сотрудник {self.employees[employee_number].name} - сокращён"
            del self.employees[employee_number]
            print(message)
        else:
            print(f"Сотрудника с №{employee_number} не найдено")

    def show_animals(self):
        print(f"Животных в зоопарке: {len(self.animals)}")
        for i, animal in enumerate(self.employees):
            print(f"{i}. ", end='')
            animal.info()

    def accept(self, animal: {}):
        pass

    def release(self, animal_number: int):
        animal_number = int(animal_number)
        if 0 <= animal_number < len(self.animals):
            message = f"Животное '{self.animals[animal_number].name}' - отпущено"
            del self.animals[animal_number]
            print(message)
        else:
            print(f"Животное c №{animal_number} не найдено")

    def load(self, file_name: str):
        pass

    def save(self, file_name: str):
        pass

FILE_NAME = "zoo.json"

def main():
    zoo = Zoo()
    zoo.load("FILE_NAME")
    try:
        if not zoo.employees and not zoo.animals:
            # Значение по умолчанию
            zoo.hire({"name"})
            pass

        zoo.show_employees()
        print(" ")
        zoo.show_animals()
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
    finally:
        zoo.save("FILE_NAME")
        pass


if __name__ == "__main__":
    main()
