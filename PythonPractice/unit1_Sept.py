# problem 1: hundred acre wood
# write a function welcome() that prints the string "welcome to the hundred acre wood!".

import formatter


def welcome():
    print("Welcome to the Hundred Acre Wood!")
welcome()

# parameters example
def function_w_parameters(parameter1, parameter2):
  print("Parameter 1:", parameter1)
  print("Parameter 2:", parameter2)

function_w_parameters("Interview", "Prep")
# Output:
# Parameter 1: Interview
# Parameter 2: Prep

def formatted_function(parameter3):
    print(f"Parameter 3: {parameter3}!")

formatted_function("Hi")

# Problem 3: Catchphrase
# Write a function print_catchphrase() that accepts a string character as a parameter 
# and prints the catchphrase of the given character as outlined in the table.

# If the given character does not match one of the characters included above, 
# print "Sorry! I don't know <character>'s catchphrase!"

def print_catchphrase(character):

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

# Problem 4: Return Item
# Implement a function get_item() that accepts a 0-indexed list items and a 
# non-negative integer x and returns the element at index x in items. 
# If x is not a valid index of items, return None.

def get_item(items, x):
    if 0 <= x < len(items):
        return items[x]
    else:
        return None

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))

# Problem 5: Total Honey
# Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() 
# that accepts a list of integers hunny_jars and returns the sum of all elements in 
# the list. Do not use the built-in function sum().

def sum_honey(hunny_jars):
    sum = 0
    for jar in hunny_jars:
        sum += jar
    return sum

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))

