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
from os.path import exists
import json
import random

#=========================================
# Animals

class Animals:
    def __init__(self, acceptable: []):
        self.__items = []
        self.__acceptable = acceptable

    def get_count(self):
        return len(self.__items)

    def clear(self):
        self.__items.clear()

    def get_animal(self, animal_number: int):
        if 0 <= animal_number < len(self.__items):
            return self.__items[animal_number]
        else:
            print(f"Животное c №{animal_number} не найдено")
            return None

    def get_random_animal(self, biology_class = None) :
        animals = []
        if biology_class:
            for animal in self.__items:
                if isinstance(animal, biology_class):
                    animals.append(animal)
        else:
            animals = self.__items
        if len(animals) > 0:
            return random.choice(animals)
        else:
            return None

    def show(self):
        print(f"Животных в зоопарке: {len(self.__items)}")
        for i, animal in enumerate(self.__items):
            print(f"{i}. ", end='')
            animal.info()

    def show_required_animals(self):
        print(f"Список классов животных:")
        for i, b_c in enumerate(self.__acceptable):
            print(f"{i}. {b_c.get_biology_class()}")

    def animal_class(self, index: int):
        if 0 <= index < len(self.__acceptable):
            return self.__acceptable[index]
        else:
            print("Ошибка: не верный номер животного")
            return None

    def __add(self, **candidate):
        animal = None
        species = candidate['species']
        nickname = candidate['nickname']
        age = candidate['age']
        voice = candidate['voice']
        food = candidate['food']
        wingspan = candidate.get('wingspan', None)
        weight = candidate.get('weight', None)
        length = candidate.get('length', None)
        animal_class = candidate['animal_class']
        if species:
            if isinstance(animal_class, str):
                for a_c in self.__acceptable:
                    if animal_class == a_c.__name__:
                        animal_class = a_c
                        break
                else:
                    print(f"Животные класса '{animal_class}' не требуется")
                    animal_class = None
            elif not animal_class in self.__acceptable:
                print(f"Животные класса '{animal_class.get_biology_class()}' не требуется")
                animal_class = None
        else:
            print("Ошибка: не указан вид животного")
            animal_class = None

        if animal_class:
            animal = animal_class(species, nickname, age, voice, food)
            if isinstance(animal, Bird) and wingspan: animal.wingspan = wingspan
            if isinstance(animal, Mammal) and weight: animal.weight = weight
            if isinstance(animal, Reptile) and length: animal.length = length
            self.__items.append(animal)

        return animal

    def accept(self, **candidate):
        animal = self.__add(**candidate)
        if animal:
            print(f"Животное {animal.species} '{animal.nickname}' принят в зоопарк")
        return animal

    def release(self, animal_number: int):
        if 0 <= animal_number < len(self.__items):
            message = f"Животное {self.__items[animal_number].species} по имени '{self.__items[animal_number].nickname}' - отпущено"
            del self.__items[animal_number]
            print(message)
        else:
            print(f"Животное c №{animal_number} не найдено")

    def load(self, data: {}):
        self.__items.clear()
        for i, value in data.items():
            self.__add(**value)

    def save(self):
        data = {}
        for i, animal in enumerate(self.__items):
            data[i] = animal.save()
        return data

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
        print(f"{self.species} '{self.nickname}'")

    def save(self):
        return {"animal_class": type(self).__name__, "species": self.species, "nickname": self.nickname,
                "age": self.age, "voice": self.voice, "food": self.food}

class Bird(Animal):
    __biology_class = "Птицы"

    def __init__(self, species, nickname, age, voice, food, wingspan = None):
        super().__init__(species, nickname, age, voice, food)
        self.wingspan = wingspan

    @staticmethod
    def get_biology_class():
        return Bird.__biology_class

    def make_move(self):
        print(f"{self.species} '{self.nickname}' летает по вольеру")

    def save(self):
        data = super().save()
        data.update({"wingspan": self.wingspan})
        return data

class Mammal(Animal):
    __biology_class = "Млекопитающие"

    def __init__(self, species, nickname, age, voice, food, weight = None):
        super().__init__(species, nickname, age, voice, food)
        self.weight = weight

    @staticmethod
    def get_biology_class():
        return Mammal.__biology_class

    def make_move(self):
        print(f"{self.species} '{self.nickname}' ходит по вольеру")

    def save(self):
        data = super().save()
        data.update({"weight": self.weight})
        return data


class Reptile(Animal):
    __biology_class = "Пресмыкающиеся"

    def __init__(self, species, nickname, age, voice, food, length = None):
        super().__init__(species, nickname, age, voice, food)
        self.length = length

    @staticmethod
    def get_biology_class():
        return Reptile.__biology_class

    def make_move(self):
        print(f"{self.species} '{self.nickname}' ползает по террариуму")

    def save(self):
        data = super().save()
        data.update({"length": self.length})
        return data

#=========================================
# Staff

class Staff:
    def __init__(self, job_list: []):
        self.__items = []
        self.__jobs = job_list

    def get_count(self):
        return len(self.__items)

    def clear(self):
        self.__items.clear()

    def get_employee(self, employee_number: int):
        if 0 <= employee_number < len(self.__items):
            return self.__items[employee_number]
        else:
            print(f"Сотрудник с №{employee_number} не найден")
            return None

    def get_random_employee(self, job_class = None):
        employees = []
        if job_class:
            for employee in self.__items:
                if isinstance(employee, job_class):
                    employees.append(employee)
        else:
            employees = self.__items
        if len(employees) > 0:
            return random.choice(employees)
        else:
            return None

    def show(self):
        print(f"Сотрудников в зоопарке: {len(self.__items)}")
        for i, employee in enumerate(self.__items):
            print(f"{i}. ", end='')
            employee.info()

    def show_required_jobs(self):
        print(f"Список профессий:")
        for i, job in enumerate(self.__jobs):
            print(f"{i}. {job.get_job_title()}")

    def job_class(self, index: int):
        if 0 <= index < len(self.__jobs):
            return self.__jobs[index]
        else:
            print("Ошибка: не верный номер профессии")
            return None

    def __add(self, **candidate):
        employee = None
        name = candidate['name']
        if name:
            job_class = candidate['job_class']
            if isinstance(job_class, str):
                for j_c in self.__jobs:
                    if job_class == j_c.__name__:
                        job_class = j_c
                        break
                else:
                    print(f"Сотрудник со специальностью '{job_class}' не требуется")
                    job_class = None
            elif not job_class in self.__jobs:
                print(f"Сотрудник со специальностью '{job_class.get_job_title()}' не требуется")
                job_class = None
        else:
            print("Ошибка: не указано имя сотрудника")
            job_class = None

        if job_class:
            employee = job_class(name)
            self.__items.append(employee)

        return employee

    def hire(self, **candidate):
        employee = self.__add(**candidate)
        if employee:
            print(f"Сотрудник {employee.name} принят на работу по специальности '{employee.get_job_title()}'")
        return employee

    def fire(self, employee_number: int):
        if 0 <= employee_number < len(self.__items):
            message = f"Сотрудник {self.__items[employee_number].name} - сокращён"
            del self.__items[employee_number]
            print(message)
        else:
            print(f"Сотрудник с №{employee_number} не найден")

    def load(self, data: {}):
        self.__items.clear()
        for i, value in data.items():
            self.__add(**value)

    def save(self):
        data = {}
        for i, employee in enumerate(self.__items):
            data[i] = employee.save()
        return data


class Employee:
    __job_title = None

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_job_title():
        return Employee.__job_title

    def info(self):
        print(f"{self.name} - {self.get_job_title()}")

    def action(self, animal):
        pass

    def save(self):
        return {"name": self.name, "job_class": type(self).__name__}

class ZooKeeper(Employee):
    __job_title = "Смотритель зоопарка"

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_job_title():
        return ZooKeeper.__job_title

    def action(self, animal: Animal):
        self.feed_animal(animal)

    def feed_animal(self, animal: Animal):
        print(f"{self.get_job_title()} {self.name} кормит животное: {animal.species} по имени '{animal.nickname}'")

class Veterinarian(Employee):
    __job_title = "Ветеринар"

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_job_title():
        return Veterinarian.__job_title

    def action(self, animal: Animal):
        self.heal_animal(animal)

    def heal_animal(self, animal: Animal):
        print(f"{self.get_job_title()} {self.name} лечит  животное: {animal.species} по имени '{animal.nickname}'")

#=========================================
# Zoo

class Zoo:
    def __init__(self, staff: [], animals: []):
        self.staff = Staff(staff)
        self.animals = Animals(animals)

    def load(self, file_name: str):
        try:
            with open(file_name) as f_in:
                zoo_data = json.load(f_in)
                self.staff.load(zoo_data.get("staff", {}))
                self.animals.load(zoo_data.get("animals", {}))
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден")

    def save(self, file_name: str):
        zoo_data = {"staff": self.staff.save(), "animals": self.animals.save()}
        with open(file_name, "w", encoding='utf-8') as f_out:
            return json.dump(zoo_data, f_out, ensure_ascii=False)

    def default_staff(self):
        self.staff.clear()
        self.staff.hire(job_class=ZooKeeper, name="Семён Семёныч")
        self.staff.hire(job_class=Veterinarian, name="Василиса Никитична")

    def default_animals(self):
        self.animals.clear()
        self.animals.accept(animal_class=Bird, species="Филин", nickname="Дрёма",
                           age="5", voice="ухает", food="мышь",wingspan="1.3")
        self.animals.accept(animal_class=Mammal, species="Бурый медведь", nickname="Потапыч",
                           age="21", voice="рычит", food="мясо", weight="250")
        self.animals.accept(animal_class=Mammal, species="Белый медведь", nickname="Умка",
                           age="18", voice="рычит", food="мясо", weight="400")
        self.animals.accept(animal_class=Reptile, species="Королевская кобра", nickname="Наг",
                           age="11", voice="шипит", food="мышь", length="2.5")

    def show_staff(self):
        self.staff.show()

    def show_animals(self):
        self.animals.show()

    def hire(self):
        self.staff.show_required_jobs()
        job_class_number = int(input("Введите номер профессии: "))
        job_class = self.staff.job_class(job_class_number)
        if job_class:
            name = input("Введите имя нового сотрудника: ")
            self.staff.hire(job_class=job_class, name=name)

    def fire(self):
        number = int(input("Введите номер сотрудника: "))
        self.staff.fire(number)

    def accept(self):
        self.animals.show_required_animals()
        animal_class_number = int(input("Введите номер биологического класса: "))
        animal_class = self.animals.animal_class(animal_class_number)
        if animal_class:
            species = input("Биологический вид: ")
            nickname = input("Кличка: ")
            age = input("Возраст: ")
            voice = input("Издаваемые звуки: ")
            food = input("Еда: ")
            wingspan, weight, length = None, None, None
            if animal_class == Bird: wingspan = input("Размах крыльев: ")
            if animal_class == Mammal: weight = input("Вес: ")
            if animal_class == Reptile: length = input("Длина: ")
            self.animals.accept(animal_class=animal_class, species=species, nickname=nickname, age=age,
                               voice=voice, food=food, wingspan=wingspan, weight=weight, length=length)

    def release(self):
        number = int(input("Введите номер животного: "))
        self.animals.release(number)

    @staticmethod
    def animal_sound(animals):
        for animal in animals:
            animal.make_sound()

    def get_animal(self, index: int):
        return self.animals.get_animal(index)

    def one_day(self):
        # random animal move
        animal = self.animals.get_random_animal()
        if animal:
            animal.make_move()

        # random Veterinarian heal and animal sound
        veterinarian = self.staff.get_random_employee(Veterinarian)
        animal = self.animals.get_random_animal()
        if veterinarian and animal:
            veterinarian.heal_animal(animal)
            animal.make_sound()

        # random Zookeeper feed animal and animal eat
        zookeeper = self.staff.get_random_employee(ZooKeeper)
        animal = self.animals.get_random_animal()
        if zookeeper and animal:
            zookeeper.feed_animal(animal)
            animal.eat()

#=========================================

FILE_NAME = "zoo.json"

def main():
    zoo = Zoo([ZooKeeper, Veterinarian], [Bird, Mammal, Reptile])
    zoo.load(FILE_NAME)
    try:
        if not exists(FILE_NAME):
            # Значение по умолчанию при первом вызове
            zoo.default_staff()
            zoo.default_animals()

        print("")
        zoo.show_staff()
        print("")
        zoo.show_animals()
        input("\nPress Enter to continue...")

        while True:
            print("\nУправление зоопарком.\n"
                  f"Сотрудников в зоопарке: {zoo.staff.get_count()}\n"
                  f"Животных в зоопарке: {zoo.animals.get_count()}")
            print("1. Список сотрудников")
            print("2. Нанять сотрудника")
            print("3. Сократить сотрудника ")
            print("4. Список животных")
            print("5. Приобрести животное")
            print("6. Отпустить животное")
            print("7. Голоса животных")
            print("8. Посмотреть что твориться в зоопарке")
            print("0. Выход")

            try:
                choice = int(input("Введите номер: "))

                if choice == 0:     # Выход
                    print("Завершение программы.")
                    break
                elif choice == 1:   # Список сотрудников
                    zoo.show_staff()
                elif choice == 2:   # Нанять сотрудника
                    zoo.hire()
                elif choice == 3:   # Сократить сотрудника
                    zoo.fire()
                elif choice == 4:   # Список животных
                    zoo.show_animals()
                elif choice == 5:   # Приобрести животное
                    zoo.accept()
                elif choice == 6:   # Отпустить животное
                    zoo.release()
                elif choice == 7:  # Голоса животных
                    animal1 = zoo.get_animal(0)
                    animal2 = zoo.get_animal(1)
                    animal3 = zoo.get_animal(3)
                    zoo.animal_sound([animal1, animal2, animal3])
                    pass
                elif choice == 8:  # Посмотреть что твориться в зоопарке
                    zoo.one_day()
                else:
                    print("Неверный выбор. Попробуйте снова.")

                input("\nPress Enter to continue...")
            except ValueError:
                print("Ошибка: Введите числовое значение.")
    finally:
        zoo.save(FILE_NAME)


if __name__ == "__main__":
    main()
