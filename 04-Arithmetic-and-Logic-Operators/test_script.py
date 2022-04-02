"""
# variables (dont modify this values, but use this variables in your tests)
name = "Mario"
age = 30
job = "PLUMBER"
account_balance = 100.52
lives = 3

# conditions (complete the code replacing *** with expressions using operators to fill the variables with the rigth result)

# Considering age of majority in US is 21, is Mario a minor?
is_mario_minor = 21 >= age

# To enter on the castle, you have to pay 100 coins... Mario can enter in the castle?
sufficient_funds_to_enter_in_the_castle = account_balance >= 100 

# Mario enter in the castle, debit 100 from the account...
account_balance = account_balance - 100

# can he enter in the secret pipe paying 1 coin?
can_enter_in_the_secret_pipe = account_balance >= 1

# To fix the pipe, we need a Pumbler... can you check if Mario is a Plumber?
is_plumber = job == "Plumber" #Appears to be right, but is not. Remember to test your tests... fix this

# Mario loses 1 life trying to fix the pipe full of lava, so complete the code and check 
# if he can try again and have more than 0 lifes
lives = lives - 1

can_try_again = lives > 0

"""

def check_is_mario_minor(is_mario_minor):
    assert is_mario_minor == False, f"Your expression is incorrect, expected result is False"
    print("OK")

def check_sufficient_funds_to_enter_in_the_castle(sufficient_funds_to_enter_in_the_castle):
    assert sufficient_funds_to_enter_in_the_castle == True, f"Your expression is incorrect, expected result is True"
    print("OK")

def check_account_balance(account_balance):
    assert account_balance == (100.52 - 100), f"Your expression is incorrect... do the MATH"
    print("OK")

def check_can_enter_in_the_secret_pipe(can_enter_in_the_secret_pipe):
    assert can_enter_in_the_secret_pipe == False, f"Your expression is incorrect, expected result is False"
    print("OK")

def check_is_pumbler(is_pumbler):
    assert is_pumbler == True, f"Your expression is incorrect, expected result is True... remember to review the code"
    print("OK")

def check_lives(lives):
    assert lives > 0, f"Your expression is incorrect!!!! You killed Mario?"
    print("OK")
