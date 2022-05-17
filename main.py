import requests

first_hero = input("Введите имя первого героя: ")
second_hero = input("Введите имя второго героя: ")
third_hero = input("Введите имя третьего героя: ")

first_hero = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{first_hero}")
first_hero_ID = first_hero.json()['results'][0]['id']
first_hero_original_url = requests.get("https://superheroapi.com/api/2619421814940190/" + first_hero_ID)
first_hero_int = first_hero_original_url.json()['powerstats']['intelligence']

second_hero = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{second_hero}")
second_hero_ID = second_hero.json()['results'][0]['id']
second_hero_original_url = requests.get("https://superheroapi.com/api/2619421814940190/" + second_hero_ID)
second_hero_int = second_hero_original_url.json()['powerstats']['intelligence']

third_hero = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{third_hero}")
third_ID = third_hero.json()['results'][0]['id']
third_original_url = requests.get("https://superheroapi.com/api/2619421814940190/" + third_ID)
third_int = third_original_url.json()['powerstats']['intelligence']


class SuperHero(object):
    def __init__(self, name, int):
        self.name = name
        self.int = int
    def __repr__(self):
        return "%s(%r)" % (self.name, self.int)

First_hero = SuperHero('Hulk', first_hero_int)
Second_hero = SuperHero('Captain Amerika', second_hero_int)
Third_hero = SuperHero('Thanos', third_int)

heroes = [First_hero, Second_hero, Third_hero]

def intelligence(superhero):
    return superhero.int

heroes_sorted = sorted(heroes, key = intelligence)
print(heroes_sorted[0])