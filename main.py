import json

with open ('tricks.json','r') as file:
    data = json.load(file)


user_tricks = ["ollie","frontside 180","pop shuvit","kickflip"]

known_tricks = [trick for trick in data if ['name'] in user_tricks]
uknown_tricks = [trick for trick in data if ['name'] not in user_tricks]

unique_tags = set()

for trick in data:
    for tags in data['tags']:
        unique_tags.add(tags)

unique_tags = sorted(list(unique_tags))     