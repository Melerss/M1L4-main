from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_ability()
        self.index = self.get_index()
        self.hp = randint(200,400)
        self.power = randint(30, 60)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSf9-0zxEU08dL4PqB5hliJ1DAq6jDIuNoiNFAYb1QiB7yjlT9Hf_Qo455Dw7bhuzA_681WoqshcjjTRPyuSs693cBngS6uMA4jk9MM3BfsDw"
    def get_ability(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['abilities'][0]["ability"]["name"])
        else:
            return "ability"
    def get_index(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["game_indices"][1]["game_index"])
        else:
            return "Pikachu"    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\nспособность твоего покемона:{self.ability}\nиндекс твоего покемона:{self.index}\nжизни твоего покемона: {self.hp}\nсила твоего покемона: {self.power}"
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return "Покемон противник применил щит сражений"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer} здоровье @ {enemy.pokemon_trainer} теперь {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}"


    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
class Wizard(Pokemon):
    def info(self):
        return f"У тебя покемон волшебник\n\n" + super().info()
class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nбоец применил супер атаку силы: {super_power}"
    def info(self):
        return f"У тебя покемон боец\n\n" + super().info()
if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))      




