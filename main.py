import json

with open ('tricks.json','r') as file:
    data = json.load(file)

print(data)
user_tricks = ["ollie","frontside 180","pop shuvit"]