import requests

hulk_url = requests.get("https://superheroapi.com/api/2619421814940190/search/hulk")
hulk_ID = hulk_url.json()['results'][0]['id']
hulk_original_url = requests.get("https://superheroapi.com/api/2619421814940190/" + hulk_ID)
hulk_int = hulk_original_url.json()['powerstats']['intelligence']

captain_url = requests.get("https://superheroapi.com/api/2619421814940190/search/captain")
captain_ID = captain_url.json()['results'][0]['id']
captain_original_url = requests.get("https://superheroapi.com/api/2619421814940190/" + captain_ID)
captain_int = captain_original_url.json()['powerstats']['intelligence']

thanos_url = requests.get("https://superheroapi.com/api/2619421814940190/search/thanos")
thanos_ID = thanos_url.json()['results'][0]['id']
thanos_original_url = requests.get("https://superheroapi.com/api/2619421814940190/" + thanos_ID)
thanos_int = thanos_original_url.json()['powerstats']['intelligence']


class SuperHero(object):
    def __init__(self, name, int):
        self.name = name
        self.int = int
    def __repr__(self):
        return "%s(%r)" % (self.name, self.int)

hulk = SuperHero('Hulk', hulk_int)
captain = SuperHero('Captain Amerika', captain_int)
thanos = SuperHero('Thanos', thanos_int)

heroes = [hulk, captain, thanos]

def intelligence(superhero):
    return superhero.int

heroes_sorted = sorted(heroes, key = intelligence)
print(heroes_sorted[0])