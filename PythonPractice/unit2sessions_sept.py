cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
for count, cereal in enumerate(cereals, start=1):
  print(count, cereal)

# dictionary methods
d = {'a': 1, 'b':2, 'c': 3}
d['d'] = 4          # Adds a new key 'd' with value 4
print(d)            # Outputs: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d['a'] = 10
print(d)
print(d['a']) # direct access by key, or use the get() method next which is considered safer since it won't raise an error if none is found
print(d.get('z'))
print(d.get('c'))
print(d.get('z', 'Not Found'))
print(d.keys())
keys = d.keys()
print(keys)
print(d.values())
print(d.items()) # each key-value pair is represented as a tuple
print(d)

# Example 1: Retrieving Album Data 
albums = [
            ["Sabrina Carpenter", "Short n' Sweet"], 
            ["FKA Twigs", "Magdalene"],
            ["Elliot Smith", "Either/Or"]]

first_album = albums[0]
print(first_album) # Output: ["Sabrina Carpenter", "Short n' Sweet"]

# Example 2: Updating a Row in a Matrix
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix[2] = [100, 200, 300]
print(matrix) # Output: [[1, 2, 3], [4, 5, 6], [100, 200, 300]]

fka_twigs = albums[1][0]
print(fka_twigs)

# Example 1: Nested Dictionaries
address_book = {
    "John Doe": {
        "phone": "555-1234",
        "email": "johndoe@example.com",
        "address": {
            "street": "123 Maple Street",
            "city": "Springfield",
            "state": "IL",
            "zip": "62701"
        }
    },
    "Jane Smith": {
        "phone": "555-5678",
        "email": "janesmith@example.com",
        "address": {
            "street": "456 Oak Avenue",
            "city": "Shelbyville",
            "state": "IL",
            "zip": "62565"
        }
    }
}

address_book["John Doe"]["email"]
john_email = address_book["John Doe"]["email"]
print(john_email) # Output: 'johndoe@example.com'
print(address_book)
print(address_book["John Doe"]["phone"])
# Example 2: List of Dictionaries
students = [
    {
        "name": "John Doe",
        "age": 16,
        "grade": "11th",
        "favorite_subject": "Math"
    },
    {
        "name": "Jane Smith",
        "age": 17,
        "grade": "12th",
        "favorite_subject": "English"
    },
    {
        "name": "Emily Johnson",
        "age": 16,
        "grade": "11th",
        "favorite_subject": "Biology"
    }
]

jane_age = students[1]["age"]
print(jane_age) # Output: 17

# Nested Loops
for i in range(1, 4):
    print("Outer loop incremented")
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

numbers = [3, 5, 2]

# Outer for loop iterates over each number in the list
for num in numbers:
    print(f"Counting down from {num}:")
    
    # Inner while loop counts down from the current number to 0
    while num >= 0:
        print(num)
        num -= 1  # Decrement the number by 1 each time
    
    print("---")  # Separator to indicate moving to the next number

numbers = [3, 5, 2]
for num in numbers[::-1]:
    print(f"Counting down from {num}:")
    print(num)
    num -= 1  # Decrement the number by 1 each time    
    print("---")  # Separator to indicate moving to the next number

# list comprehension with dictionary
oxygen_levels = {"Command Module": 21, "Habitation Module": 20, "Laboratory Module": 19, "Airlock": 22, "Storage Bay": 18}
min_val = 19 
max_val = 22
# Output: ['Storage Bay']
keys_outside_range = [key for key, value in oxygen_levels.items() if value < min_val or value > max_val]
print(keys_outside_range)

# or filter with lambda does the same thing
# Find keys with values outside the specified range using filter and lambda
keys_outside_range = list(filter(lambda key: oxygen_levels[key] < min_val or oxygen_levels[key] > max_val, oxygen_levels))

print(keys_outside_range)  # Output: ['Storage Bay']

# Find keys with values within the specified range
keys_within_range = [key for key, value in oxygen_levels.items() if min_val <= value <= max_val]

print(keys_within_range)  # Output: ['Command Module', 'Habitation Module', 'Laboratory Module', 'Airlock']