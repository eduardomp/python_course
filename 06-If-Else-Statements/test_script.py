"""
client = {
    "name": "Toad",
    "age": 16,
    "coins": 100
}

store = {
    "mushrooms": 10,
    "stars": 5,
    "coins": 1000,
    "minimal_age_mushrooms": 15,
    "minimal_age_stars": 18
}


'''
CHALLENGE 1 

Toad wants to buy a mushroom, check if he has sufficient coins and if his age is greater or equal
to the minimum age to buy mushrooms.
Every mushroom costs 20, so debit this amount from their account and add it to the store account.
'''
toad_can_buy_mushroom = None

# complete this condition and fix the errors, remember the identation
if client["coins"] >= 20 and client["age"] >= store["minimal_age_mushrooms"]:
    toad_can_buy_mushroom = True
    # complete the code to debit from client and deposit to store
    client["coins"] = client["coins"] - 20
    store["coins"] = store["coins"] + 20
    store["mushrooms"] = store["mushrooms"] - 1
    print("Thanks!")
else:
    toad_can_buy_mushroom = False
    print("Stoped transaction!")

'''
CHALLENGE 2

Now Toad wants to buy a star, check if he has sufficient coins 
and if his age is greater than minimal age to buy stars.
Every star costs 80
'''


toad_can_buy_star = None

# complete this condition and fix the errors, remember the identation
if client["coins"] >= 80 and client["age"] >= store["minimal_age_stars"]:
    toad_can_buy_star = True
    # complete the code to debit from client and deposit to store
    client["coins"] = client["coins"] - 80
    store["coins"] = store["coins"] + 80
    print("Thanks!")
else:
    toad_can_buy_star = False
    print("Stoped transaction!")
"""

def check_toad_can_buy_mushroom(toad_can_buy_mushroom, client, store):
    assert toad_can_buy_mushroom \
    and client["coins"] == 80 \
    and store["coins"] == 1020 \
    and store["mushrooms"] == 9 , "CHALLENGE 1 - ERROR"
    print("CHALLENGE 1 - OK")

def check_toad_can_buy_star(toad_can_buy_star, client, store):
    assert toad_can_buy_star == False \
    and client["coins"] == 80 \
    and store["coins"] == 1020 \
    and store["mushrooms"] == 9 \
    and store["stars"] == 5 , "CHALLENGE 2 - ERROR"
    print("CHALLENGE 2 - OK")