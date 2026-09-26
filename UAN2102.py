class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.pet = None

    def adopt_pet(self, pet):
        self.pet = pet
        print(f"Людина {self.name} завела улюбленця на ім'я {pet.name} ({pet.species})")

    def play_with_pet(self):
        if self.pet:
            print(f"Людина {self.name} грається з {self.pet.name}. Звук: {self.pet.make_sound()}")
        else:
            print(f"У людини {self.name} немає улюбленця, щоб погратися")


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        if self.species.lower() in ["кіт"]:
            return "Мяу"
        elif self.species.lower() in ["собака"]:
            return "Гав"


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)
        print(f"Пасажир {human.name} сів у {self.brand}")

    def print_passengers_names(self):
        if self.passengers:
            print(f"Імена пасажирів {self.brand}: ")
            for passenger in self.passengers:
                if passenger.pet:
                    print(f"- {passenger.name} (з улюбленцем {passenger.pet.name})")
                else:
                    print(f"- {passenger.name}")
        else:
            print(f"В автомобілі {self.brand} немає пасажирів")


nick = Human("Нік")
kate = Human("Кейт")
car = Auto("Мерседес")

my_cat = Pet("Барсік", "кіт")
kate.adopt_pet(my_cat)
kate.play_with_pet()

car.add_passenger(nick)
car.add_passenger(kate)

car.print_passengers_names()
