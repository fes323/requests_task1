import requests

heroes_list = ['Hulk', 'Captain', 'Thanos']
res_id = []
heroes_intel = []

for i in heroes_list:
    res_url_tmp = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{i}")
    res_id_tmp = res_url_tmp.json()['results'][0]['id']
    res_id.append(res_id_tmp)

for i in res_id:
    id_url = requests.get(f"https://superheroapi.com/api/2619421814940190/{i}")
    heroes_int_tmp = id_url.json()['powerstats']['intelligence']
    heroes_intel.append(heroes_int_tmp)

heroes_intel = list(map(int,heroes_intel))

heroes_dict = {}
for i in range(0, len(heroes_list)):
    heroes_dict[heroes_list[i]] = heroes_intel[i]

top_int =  max(zip(heroes_dict.values(),heroes_dict.keys()) )

print(top_int)