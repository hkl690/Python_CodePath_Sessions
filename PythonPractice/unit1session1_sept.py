from typing import Optional, Any

# Problem 1
def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

# Problem 2
def greeting(name: str):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
    
greeting("Michael")
greeting("Winnie the Pooh")

# Problem 3
def print_catchphrase(character: str):
    if character == "Pooh": 
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")
        
print_catchphrase("Pooh")
print_catchphrase("Tigger")
print_catchphrase("Eeyore")
print_catchphrase("Christopher Robin")
print_catchphrase("Chris")

# Dictionary version
# def print_catchphrase(character: str):
#     catchphrases = {
#         "Pooh": "Oh bother!",
#         "Tigger": "TTFN: Ta-ta for now!",
#         "Eeyore": "Thanks for noticing me.",
#         "Christopher Robin": "Silly old bear."
#     }
#     print(catchphrases.get(character, f"Sorry! I don't know {character}'s catchphrase!"))

# Problem 4: Return Item
# Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x 
# and returns the element at index x in items. If x is not a valid index of items, return None.
def get_item(items: list, x: int) -> Optional[Any]:
    if 0 <= x < len(items):
        return items[x]
    else:
        return None
    
# Example tests
items1 = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items1, x)) # output "roo"

items2 = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items2, x)) # output None
        
# Problem 5: Total Honey
# Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts 
# a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the 
# built-in function sum().
def sum_honey(hunny_jars: list) -> int:
    total = 0
    for jar in hunny_jars:
        total += jar
    return total

# Example tests
hunny_jars1 = [2, 3, 4, 5]
print(f"Hunny jars sum total: {sum_honey(hunny_jars1)}") # output 14

hunny_jars2 = []
print(f"Hunny jars sum total: {sum_honey(hunny_jars2)}") # output 0

# Problem 6: Double Trouble
# Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers
# hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.

def doubled(hunny_jars):    
    for i in range(len(hunny_jars)):
        hunny_jars[i] *= 2
    return hunny_jars
    
hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))