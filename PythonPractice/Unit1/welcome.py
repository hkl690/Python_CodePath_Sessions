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
def get_item(items: list, x: int):
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
        