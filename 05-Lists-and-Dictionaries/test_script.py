"""
################################### Lists ###################################

# Given the list
fruits = ["Banana","Apple","Samsung","Pineapple"]

#CHALLENGE 1 - Get the value Banana, store in a variable called banana
banana = fruits[0]

#CHALLENGE 2 - Get the Pineapple
pineapple_negative_index = -1 # change just this variable
pineapple = fruits[pineapple_negative_index]

#CHALLENGE 3 - Remove Samsung and store the value in a variable
not_apple = fruits.pop(2)

#CHALLENGE 4 - Store size of the list inside a variable and after add two new fruits "Cherry" and "Orange"
fruits_size = len(fruits)
# place here the code to add new fruits 
fruits.append("Cherry")
fruits.append("Orange")

#CHALLENGE 5 - Create a new list with values from the second untill last value of fruits list
new_list = fruits[1:]

################################### Dictionaries ###################################

# Given the Dictionarie
profile = {
    "name":"Bruce",
    "age":36,
    "sex":"Male",
    "hobbies": ["ski","gamming","do nothing"],
    "mobile":"555-555-555",
    "address": {
       "code":"1234-123",
       "street":"champs elysees",
       "number":"333",
       "country": "France" 
    },
    "friends":["Mario","Luigi","Browser","Pierre"]
}


#CHALLENGE 6  - Get the street from profile
street = profile["address"]["street"]

#CHALLENGE 7 - Get friends, store in a variable, add a new friend "Toad" to this list and asign this new list to profile friends

friends = profile["friends"]
friends.append("Toad")
profile["friends"] = friends

#CHALLENGE 8 - Get the sorted key list and store into a variable
key_list = sorted(profile)

#CHALLENGE 9 - Add a new key/value to profile address called "city" with value "Paris"
profile["address"]["city"] = "Paris"

#CHALLENGE 10 - Clone this profile into another variable and change the name, age, sex and remove friends completely

new_profile = profile.copy()
new_profile["name"] = "Fiona"
new_profile["age"] = 40
new_profile["sex"] = "Female"
del new_profile["friends"]

"""

def check_banana(banana):
    assert banana is not None and banana == "Banana", "CHALLENGE 1 - ERROR"
    print("CHALLENGE 1 - OK")

def check_pineapple(pineapple,pineapple_negative_index):
    assert pineapple is not None and pineapple == "Pineapple" and pineapple_negative_index == -1, "CHALLENGE 2 - ERROR"
    print("CHALLENGE 2 - OK")

def check_not_apple(not_apple, fruits):
    assert not_apple is not None and not_apple == "Samsung" and "Samsung" not in fruits, "CHALLENGE 3 - ERROR"
    print("CHALLENGE 3 - OK")

def check_fruits_size(fruits_size, fruits):
    assert fruits_size == 3 and len(fruits) == 5 and "Orange" in fruits and "Cherry" in fruits, "CHALLENGE 4 - ERROR"
    print("CHALLENGE 4 - OK")

def check_new_list(new_list, fruits):
    assert new_list is not None and len(new_list) == 4 and fruits[1:] == new_list, "CHALLENGE 5 - ERROR"
    print("CHALLENGE 5 - OK")

def check_street(street, profile):
    assert street is not None and street == profile["address"]["street"], "CHALLENGE 6 - ERROR"
    print("CHALLENGE 6 - OK")

def check_friends(friends, profile):
    assert friends is not None and "Toad" in friends and profile["friends"] == friends, "CHALLENGE 7 - ERROR"
    print("CHALLENGE 7 - OK")

def check_key_list(key_list,profile):
    assert key_list is not None and key_list == sorted(profile), "CHALLENGE 8 - ERROR"
    print("CHALLENGE 8 - OK")

def check_paris(profile):
    assert profile["address"]["city"] is not None and profile["address"]["city"] == "Paris",  "CHALLENGE 9 - ERROR"
    print("CHALLENGE 9 - OK")

def check_new_profile(new_profile, profile):
    assert new_profile is not None \
        and new_profile["name"] is not None and new_profile["name"] != profile["name"] \
        and new_profile["age"] is not None and new_profile["age"] != profile["age"] \
        and new_profile["sex"] is not None and new_profile["sex"] != profile["sex"] \
        and new_profile.get("friends",0) == 0 and "friends" not in list(new_profile) \
        and profile["friends"] is not None,  "CHALLENGE 10 - ERROR"
    print("CHALLENGE 10 - OK")
