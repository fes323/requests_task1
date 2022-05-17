import requests

First_hero = input("Введите имя первого героя: ")
Second_hero = input("Введите имя второго героя: ")
Third_hero = input("Введите имя третьего героя: ")

First_hero = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{First_hero}")
hulk_ID = First_hero.json()['results'][0]['id']
hulk_original_url = requests.get("https://superheroapi.com/api/2619421814940190/" + hulk_ID)
hulk_int = hulk_original_url.json()['powerstats']['intelligence']

Second_hero = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{Second_hero}")
captain_ID = Second_hero.json()['results'][0]['id']
captain_original_url = requests.get("https://superheroapi.com/api/2619421814940190/" + captain_ID)
captain_int = captain_original_url.json()['powerstats']['intelligence']

Third_hero = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{Third_hero}")
thanos_ID = Third_hero.json()['results'][0]['id']
thanos_original_url = requests.get("https://superheroapi.com/api/2619421814940190/" + thanos_ID)
thanos_int = thanos_original_url.json()['powerstats']['intelligence']


class SuperHero(object):
    def __init__(self, name, int):
        self.name = name
        self.int = int
    def __repr__(self):
        return "%s(%r)" % (self.name, self.int)

First_hero = SuperHero('Hulk', hulk_int)
Second_hero = SuperHero('Captain Amerika', captain_int)
Third_hero = SuperHero('Thanos', thanos_int)

heroes = [First_hero, Second_hero, Third_hero]

def intelligence(superhero):
    return superhero.int

heroes_sorted = sorted(heroes, key = intelligence)
print(heroes_sorted[0])