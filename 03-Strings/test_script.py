"""
# Put all chars in uppercase
uppercase = "Easy Task UH?"
uppercase_answer = uppercase.upper()
print(uppercase_answer)

# Choose Luigi to replace Mario
replace = "My name is Mario!"
replace_answer = replace.replace("Mario","Luigi")
print(replace_answer)

# just the first letter capitalized
capitalize = "capitalized"
capitalize_answer = capitalize.capitalize()

# do the math
do_the_math = "Two + Two = {2+2}" # put this expression to work inside this string
do_the_math_answer = f"Two + Two = {2+2}"

# only digits allowed here
digits = "Only digits here >>>>> % <<<<<" * 7 # expects: "Only digits here >>>>> 7 <<<<<"
digits_answer = "Only digits here >>>>> %d <<<<<" % 7

# list of foods from string
food_list = "Banana tomato pineaple pasta and rice" # make a list of this
food_list_answer = food_list.split()

# from food_list_answer, get pasta
pasta = food_list_answer[3]

# the word "and" is not a food, do the needed operations to remove the word "and" and store in a list called just_foods_list
just_foods_list = food_list.replace("and","").split()


"""



def check_uppercase_answer(uppercase_answer):
    assert uppercase_answer == "EASY TASK UH?", "uppercase_answer is WRONG"
    print("uppercase_answer is OK")

def check_replace_answer(replace_answer):
    assert replace_answer == "My name is Luigi!", "replace_answer is WRONG"
    print("replace_answer is OK")

def check_capitalize_answer(capitalize_answer):
    assert capitalize_answer == "Capitalized", "capitalize_answer is WRONG"
    print("capitalize_answer is OK")

def check_do_the_math_answer(do_the_math_answer):
    assert do_the_math_answer == "Two + Two = 4", "do_the_math_answer is WRONG"
    print("do_the_math_answer is OK")

def check_digits_answer(digits_answer):
    assert digits_answer == "Only digits here >>>>> 7 <<<<<", "digits_answer is WRONG"
    print("digits_answer is OK")

def check_food_list_answer(food_list_answer):
    assert len(food_list_answer) == 6 and "and" == food_list_answer[4], "food_list_answer is WRONG"
    print("food_list_answer is OK")

def check_pasta(pasta):
    assert "pasta" == pasta, "pasta is WRONG"
    print("pasta is OK")

def check_just_foods_list(just_foods_list):
    assert "and" not in just_foods_list and len(just_foods_list) == 5, "just_foods_list is WRONG"
    print("just_foods_list is OK")