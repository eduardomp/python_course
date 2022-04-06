"""
# CHALLENGE - 1 Iterate fruits list and change every fruit to UPPERCASE, storing in the uppercased_list variable

fruits = ["Banana","Apple","Pineapple","Kiwi","Açaí"]
uppercased_list = []

for fruit in fruits:
    uppercased_list.append(fruit.upper())

print(f"uppercased_list: {uppercased_list}")

# CHALLENGE - 2 Create a list with numbers beetween 0 and 6

zero_to_six = []
for i in range(7):
    zero_to_six.append(i)
    
print(f"zero_to_six: {zero_to_six}")
    
# CHALLENGE - 3 Iterate the list skipping all non int elements
elements = ["Mario", 1, ['hi'] , "banana", {"progress":0.99}, 42, 100, 0.3, True]
integers = []
for element in elements:
    if type(element) != int:
        continue
    integers.append(element)
    
print(f"integers: {integers}")

# CHALLENGE - 4 Use list comprehensions to lowercase all elements of the list uppercased_list
lowercased = [fruit.lower() for fruit in uppercased_list]
print(f"lowercased: {lowercased}")

# CHALLENGE - 5 append i as long i is less than 6
i = 1
i_list = []
while i < 6:
    i_list.append(i)
    i += 1

print(f"i_list: {i_list}")
"""

def check_uppercased_list(uppercased_list):
    response = ['BANANA', 'APPLE', 'PINEAPPLE', 'KIWI', 'AÇAÍ']
    assert uppercased_list == response, "CHALLENGE-1 ERROR"
    print("CHALLENGE-1 OK")

def check_zero_to_six(zero_to_six):
    assert zero_to_six is not None \
    and len(zero_to_six) == 7 \
    and zero_to_six == [0, 1, 2, 3, 4, 5, 6], "CHALLENGE-2 ERROR"
    print("CHALLENGE-2 OK")

def check_integers(integers):
    assert integers is not None \
    and len(integers) == 3 \
    and integers == [1, 42, 100], "CHALLENGE-3 ERROR"
    print("CHALLENGE-3 OK")

def check_lowercased(lowercased):
    assert lowercased == ['banana', 'apple', 'pineapple', 'kiwi', 'açaí'], "CHALLENGE-4 ERROR"
    print("CHALLENGE-4 OK")

def check_i_list(i_list):
    assert i_list == [1, 2, 3, 4, 5], "CHALLENGE-5 ERROR"
    print("CHALLENGE-5 OK")












