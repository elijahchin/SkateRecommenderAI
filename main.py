#import json module 
import json

#open json file
with open ('tricks.json','r') as file:
    
    # name the json using variable data
    data = json.load(file)

#  list of tricks as input
user_tricks = ["ollie","frontside 180","pop shuvit","kickflip"]

# list of known tricks based on identical user_tricks from input stored in variable known_tricks
known_tricks = [trick for trick in data if trick["name"] in user_tricks]

# list of unknown tricks the user does not have in their trick bag/arsenal ; stored in variable unknown_tricks
uknown_tricks = [trick for trick in data if trick["name"] not in user_tricks]

# initialize a set to avoid duplicates and collect unigue tags from the tricks
unique_tags = set()

# loop through the data using trick as a loop variable
for trick in data:
    # loop through the tags in the trick data
    for tags in trick["tags"]:
        # add the tags to the set
        unique_tags.add(tags)

# store the set in a list, then sort the set in alphabetical order
unique_tags = sorted(list(unique_tags))

# vectorize the tricks tags into 0's and 1's 
def_tags_to_vector(data,unique_tags):

    # loop through each trick in data
    for trick in data:
        vector = []
        #  loop through unique_tags
        for tag in unique_tags:
            # if the trick in data has the tag put a 1, if it doesn't put a 0
            if tag in trick["tags"]:
                vector.append(1)

            else:
                vector.append(0)
        
        trick["tag_vector"] = vector






