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

# Problem 7: Poohsticks
# Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks 
# in a stream and race them. They time how long it takes each player's stick to float under 
# Poohsticks Bridge to score each round.

# Write a function count_less_than() to help Pooh and his friends determine how many players 
# should move on to the next round of Poohsticks. count_less_than() should accept a 
# list of integers race_times and an integer threshold and return the number of race times less 
# than threshold.

def count_less_than(race_times, threshold):
    counter = 0
    for race_time in race_times:
        if race_time < threshold:
            counter += 1

    return counter

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print("Poohsticks 3: ", count_less_than(race_times, threshold)) # output 3

race_times = []
threshold = 4
print("Poohsticks 0: ", count_less_than(race_times, threshold)) # output 0

race_times = [91, 32, 83, 54, 5, 6]
threshold = 10
print("Poohsticks 10: ", count_less_than(race_times, threshold)) # output 2