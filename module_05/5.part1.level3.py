from random import randint

class Warrior:
    def __init__(self, name):
        self.health = 100
        self.stamina = 100
        self.armor = 100
        self.name = name

    def attack(self, other):
        if other.move == "attack":
            if other.stamina > 0:
                self.health -= randint(10, 30)
            else:
                self.health -= randint(0, 10)
            print(f"Игроки аттакуют друг друга. У игрока {self.name} осталось {self.health} очков здоровья")
        self.stamina -= 10

    def defense(self, other):
        if other.move == "defense":
            print("Оба игрока защищаются")
        else:
            if self.armor > 0:
                self.health -= randint(0, 20)
                self.armor -= randint(0, 10)
            else:
                self.health -= randint(0, 30)
            print(f"Игрок {other.name} атакует игрока {self.name}. У игрока {self.name} осталось {self.health} очков здоровья и {self.armor} очков брони")

def battle(player_one, player_two):
    n = 1
    while player_one.health > 10 and player_two.health > 10:
        print(f"Раунд {n} начинается: ")
        # определяем текущее действие первого игрока
        if randint(0, 1):
            player1.move = "attack"
        else:
            player1.move = "defense"
        # определяем текущее действие второго игрока
        if randint(0, 1):
            player2.move = "attack"
        else:
            player2.move = "defense"
        # Выполняем действие обоими игроками
        if player1.move == "attack":
            player1.attack(player2)
        else:
            player1.defense(player2)
        if player2.move == "attack":
            player2.attack(player1)
        else:
            player2.defense(player1)
        n += 1
    if player_one.health == player_two.health:
        print("Оба игрока пали в битве")
    elif player_one.health > player_two.health:
        print(f"Игрок {player_two.name} проиграл!")
        defeated = player_two
    else:
        print(f"Игрок {player_one.name} проиграл!")
        defeated = player_one
    police_verso = input("live or die? ")
    if police_verso == "die":
        defeated.health = 0
        print(f"Игрок {defeated.name} погибает")
    else:
        print(f"Игроки сразятся вновь, но в следующий раз")

player1 = Warrior('Vi')
player2 = Warrior('Jinx')
battle(player1, player2)
