# Problem 1: Festival Lineup
# Given two lists of strings artists and set_times of length n, write a function lineup() 
# that maps each artist to their set time.

# An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

# def lineup(artists, set_times):
    # schedule = zip(artists, set_times)
    # return dict(schedule)


# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# Example Output:
# {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
# {}


# Problem 2: Planning App
# You are designing an app for your festival to help attendees have the best experience possible! 
# As part of the application, users will be able to easily search their favorite artist and find out the day, 
# time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist 
# and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, 
# and stage they are playing on. Return the dictionary containing the information about the given artist.

# If the artist searched for does not exist in festival_schedule, 
# return the dictionary {"message": "Artist not found"}.

# def get_artist_info(artist, festival_schedule):
    # not_found = {"message": "Artist not found"}
    # if artist not in festival_schedule:
        # return not_found
    # else:
        # return festival_schedule.get(artist)


# festival_schedule = {
    # "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    # "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    # "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    # "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  
# Example Output:
# {'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
# {'message': 'Artist not found'}



# Problem 3: Breathing Room
# As part of your job as an astronaut, you need to perform routine safety checks. You are given a dictionary oxygen_levels which maps room names to current oxygen levels and two integers min_val and max_val specifying the acceptable range of oxygen levels. Return a list of room names whose values are outside the range defined by min_val and max_val (inclusive).
# list comprehension with dictionary

import enum


oxygen_levels = {"Command Module": 21, "Habitation Module": 20, "Laboratory Module": 19, "Airlock": 22, "Storage Bay": 18}
min_val = 19 
max_val = 22
# Output: ['Storage Bay']
keys_outside_range = [key for key, value in oxygen_levels.items() if value < min_val or value > max_val]
print("Example Answer: ", keys_outside_range)

def check_oxygen_levels(oxygen_levels, min_val, max_val):
    if not min_val or not max_val or not oxygen_levels:
        print("Please enter valid inputs")
        # raise(Exception("Invalid input!"))
        # raise ValueError()

    result = []
    for key, value in oxygen_levels.items():
        if value < min_val or value > max_val:
            result.append(key)
    return result
print("Method: ", check_oxygen_levels(oxygen_levels, min_val, max_val))
oxygen_levels = {}
min_val = 19 
max_val = 22
print("Method: ", check_oxygen_levels(oxygen_levels, min_val, max_val))


oxygen_levels = {"Command Module": 21, "Habitation Module": 20, "Laboratory Module": 19, "Airlock": 22, "Storage Bay": 18}
min_val = 19 
max_val = 22
# Output: ['Storage Bay']

# or filter with lambda does the same thing
# Find keys with values outside the specified range using filter and lambda
keys_outside_range = list(filter(lambda key: oxygen_levels[key] < min_val or oxygen_levels[key] > max_val, oxygen_levels))

print("Lambda: ", keys_outside_range)  # Output: ['Storage Bay']

# Find keys with values within the specified range
keys_within_range = [key for key, value in oxygen_levels.items() if min_val <= value <= max_val]

print(keys_within_range)  # Output: ['Command Module', 'Habitation Module', 'Laboratory Module', 'Airlock']

def most_endangered(species_list):
    # make new dictionary of names to populations
    # get min of values (populations), and return the corresponding name (key) from the dictionary

    if not species_list:
        return None  

    min_population = float('inf')
    endangered_species = None

    for species in species_list:
        if species['population'] < min_population:
            min_population = species['population']
            endangered_species = species['name']

    return endangered_species

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 10
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 10
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))


# Problem 2: Identifying Endangered Species
# As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

# Your task is to determine how many of the observed species are also considered endangered.

# Note: Species are case-sensitive, so "a" is considered a different species from "A".

# Write a function to count the number of endangered species observed.

def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)
    count = 0

    for species in observed_species:
        if species in endangered_set:
            count += 1

    return count


endangered_species1 = "aaaaaaaaA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) # 3
print(count_endangered_species(endangered_species2, observed_species2)) # 0

# Problem 3: Navigating the Research Station
# In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), you start your journey at the first observation point (index 0). To make observations in a specific order represented by a string observations, you need to move from one point to another.

# The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.

# Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.
def navigate_research_station(station_layout, observations):
    station_index = {}
    for index, char in enumerate(station_layout):
        station_index[char] = index

    current_index = 0
    total_time = 0

    for char in observations:
        target_index = station_index[char]

        # calculate the time to move to the target
        total_time += abs(current_index - target_index)

        # update the current_index to the target_index
        current_index = target_index

    return total_time

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  # 45
print(navigate_research_station(station_layout2, observations2)) # 4
# Example 2 explanation: The index moves from 0 to 2 to observe 'c', then to 1 for
# 'b', then to 0 again for 'a'.
# Total time = 2 + 1 + 1 = 4.





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


# 5
word = "encourage"
char_count = {}
for char in word:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1
char_count['e'] += 2
print(char_count['e'])

bart = {"first name": "Bart", "last name": "Simpson", "age": "10", "hometown": "Springfield"}
print(bart["hometown"])
print(bart.get("hometown"))
print(bart.pop("hometown"))

def mystery_function(old_dictionary):
    new_dictionary = {}

    for key, value in old_dictionary.items():
        new_dictionary[value] = key
    return new_dictionary

old_dictionary = {'a': 1, 'b': 2, 'c': 3}
new_dictionary = mystery_function(old_dictionary)
print(new_dictionary)

# Complete the 'get_top_player' function
# It is expected to return a STRING

def get_top_player(dictionary):
    high_score = 0
    top_player = ""

    for name, score in dictionary.items():
        if score > high_score:
            high_score = score
            top_player = name

    return top_player

old_dictionary = {'c': 3, 'a': 1, 'b': 2}
print(get_top_player(old_dictionary))

# 1

def find_min_index_of_repeating(arr):
    if len(arr) == 0:
        return None

    seen = {}
    for i, value in enumerate(arr):
        if value in seen:
            return seen[value]
        seen[value] = i
    return None

arr = [10,21,22,33,44,55,33]
print(find_min_index_of_repeating(arr))


#
# Complete the 'intersection' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums1
#  2. INTEGER_ARRAY nums2
#

def intersection(nums1, nums2):
    # Write your code here
    if len(nums1) == 0 or len(nums2) == 0:
        return []
        
    set1 = set(nums1)
    set2 = set(nums2)
    
    intersection_set = set1.intersection(set2)
    
    return sorted(list(intersection_set))

# Example 1:
nums1 = [1,2,2,1] 
nums2 = [2,2]
print(intersection(nums1, nums2))
# Output: [2]

# Example 2:
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))
# Output: [9,4] <-- incorrect, is [4,9]

# Example 3: Both arrays are empty
nums1 = []
nums2 = []
print(intersection(nums1, nums2))  # Output: []

# Example 4: No intersection
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print(intersection(nums1, nums2))  # Output: []

# Example 5: Single element intersection
nums1 = [1, 2, 3]
nums2 = [3, 4, 5]
print(intersection(nums1, nums2))  # Output: [3]

# Example 6: All elements intersection
nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
print(intersection(nums1, nums2))  # Output: [1, 2, 3]

# Example 7: Different lengths
nums1 = [1, 2, 3, 4, 5]
nums2 = [2, 4]
print(intersection(nums1, nums2))  # Output: [2, 4]

# Example 8: Negative numbers
nums1 = [-1, -2, -3, 4]
nums2 = [-3, 4, 5]
print(intersection(nums1, nums2))  # Output: [-3, 4]



def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in reversed(s): # reversed is a built-in function, does the same as s[::-1]
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

print(roman_to_int("III")) # 3
print(roman_to_int("LVIII")) # 58   <- IIIVL in reverse
print(roman_to_int("MCMXCIV")) # 1994   <-- VICXMCM in reverse
print(roman_to_int("IV")) #4
print(roman_to_int("XI")) #11

# Unit 2 Session 2 Standard B 
# 
# Problem 1: Filter Destinations
# You're planning an epic trip and have a dictionary of destinations mapped to their respective rating scores. Your goal is to visit only the best-rated destinations. Write a function that takes in a dictionary destinations and a rating_threshold as parameters. The function should iterate through the dictionary and remove all destinations that have a rating strictly below the rating_threshold. Return the updated dictionary.

def remove_low_rated_destinations(destinations, rating_threshold):
    keys_to_remove = [key for key, value in destinations.items() if value < rating_threshold]
    print(keys_to_remove)
    for key in keys_to_remove:
        destinations.pop(key)
    return destinations

destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogota": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

print(remove_low_rated_destinations(destinations, 4.0)) # {"Paris": 4.8, "Addis Ababa": 4.9}
print(remove_low_rated_destinations(destinations2, 4.9)) # {}

# Problem 2: Unique Travel Souvenirs
# As a seasoned traveler, you've collected a variety of souvenirs from different destinations. You have an array of string souvenirs, where each string represents a type of souvenir. You want to know if the number of occurrences of each type of souvenir in your collection is unique.

# Write a function that takes in an array souvenirs and returns True if the number of occurrences of each value in the array is unique, or False otherwise.

def unique_souvenir_counts(souvenirs):
    # create a dictionary to count souvenirs
    count_dict = {}
    for souv in souvenirs:
        if souv in count_dict:
            count_dict[souv] += 1
        else:
            count_dict[souv] = 1

    # create a set to track the counts seen
    seen_counts = set()

    # check if the counts are unique
    for count in count_dict.values():
        if count in seen_counts:
            return False
        seen_counts.add(count)

    return True

souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print(unique_souvenir_counts(souvenirs1))  
print(unique_souvenir_counts(souvenirs2)) 
print(unique_souvenir_counts(souvenirs3))
# Expected Outputs:
# True
# Example 1 Explanation: The value "keychain" has 3 occurrences, "hat" has 2 
# and "postcard" has 1. No two values have the same number of occurrences.

# True
# Example 2 Explanation: The value "postcard" appears 4 times There's only one count (4), 
# which is technically unique, so this should also return True.

# False
# Example 3 Explanation: Each item appears 1 time All counts are 1, which is not unique, 
# so this should return False.


# Problem 3: Secret Beach
# You make friends with a local at your latest destination, and they give you a coded message with the name of a secret beach most tourists don't know about! You are given the strings key and message which represent a cipher key and a secret message, respectively. The steps to decode the message are as follows:

# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "travel the world" (an actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('t' -> 'a', 'r' -> 'b', 'a' -> 'c', 'v' -> 'd', 'e' -> 'e', 'l' -> 'f', 'h' -> 'g', 'w' -> 'h', 'o' -> 'i', 'd' -> 'j').

# Write a function decode_message() that accepts the strings key and message and returns a string representing the decoded message.

def decode_message(key, message):
    # create a substitution table
    substitution_table = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    used_chars = set()

    # loop through the key to create the table
    index = 0
    for char in key:
        if char.isalpha() and char not in used_chars:
            substitution_table[char] = alphabet[index] # add to table with corresponding letter from alphabet
            used_chars.add(char) # mark the char as used in the set
            index += 1
            if index == 26:
                break

    # decode the message
    decoded_message = []
    for char in message:
        if char == ' ':
            decoded_message.append(' ')
        else:
            decoded_message.append(substitution_table.get(char, char))

    return ''.join(decoded_message)


key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"

print(decode_message(key1, message1)) # Example Output 1: this is a secret

key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "hntu depcte lxejw lxwntu zwx piqfx"

print(decode_message(key2, message2)) # Example Output 2: find laguna beach behind the grove



# Problem 4: Longest Harmonious Travel Sequence
# In a list of travel packages, we define a harmonious travel sequence as a sequence where the difference between the maximum and minimum travel ratings is exactly 1.

# Given an integer array rating, return the length of the longest harmonious travel sequence among all its possible subsequences.

# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

# You are provided with a partially implemented solution that contains bugs. Your task is to identify and fix the bugs to ensure the solution works correctly.

def find_longest_harmonious_travel_sequence(ratings):
    # Initialize a dictionary to store the frequency of each rating
    frequency = {}

    # Count the occurrences of each rating
    for rating in ratings:
        if rating in frequency:
            frequency[rating] += 1 
        else:
            frequency[rating] = 1

    max_length = 0

    # Find the longest harmonious sequence
    for rating in frequency:
        if rating + 1 in frequency:
            max_length = max(max_length, frequency[rating] + frequency[rating + 1])  

    return max_length

durations1 = [1, 3, 2, 2, 5, 2, 3, 7]
durations2 = [1, 2, 3, 4]
durations3 = [1, 1, 1, 1]
durations4 = [1, 3, 2, 2, 5, 2, 3, 4, 6, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 11]

print(find_longest_harmonious_travel_sequence(durations1)) # 5
print(find_longest_harmonious_travel_sequence(durations2)) # 2
print(find_longest_harmonious_travel_sequence(durations3)) # 0
print(find_longest_harmonious_travel_sequence(durations4)) # 10

# Assessment Standard B #4
students = ["Samarth", "Nicholas", "Lexie", "Theresa"]
next_id = 12348
directory = {12345: "Samarth", 12346: "Nicholas", 12347: "Kenyele"}
for student in students:
    if student not in directory.values():
        directory[next_id] = student
        next_id += 1

print(directory[12348])

#6
princess_movies = {"Snow White": 1937, "The Princess and the Frog": 2009, "Moana": 2016}
print(princess_movies.values())

#7
def mystery_function(word):
    result = {}
    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

word = "banana"
result = mystery_function(word)
print(result)

#5 find the bug

def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = "The quick brown brown brown fox fox"
print(count_words(sentence))

# 1 Contains duplicates - Given an int array nums, return True if any value appears
# at least twice in the array, and return False if every element is distinct

def contains_duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

nums = [1,2,3,1] # True
print(contains_duplicates(nums))

nums = [1,2,3,4] # False
print(contains_duplicates(nums))


# 2 Two Sum - Given an array of int nums and an int target, return indices of the two numbers
# such that they add up to target. You may assume that each input would have exactly one 
# solution, and you may not use the same element twice. Return the answer in ascending order 
# (i.e. sorted from least to greatest).

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return sorted([seen[complement], i])
        seen[num] = i

nums = [2, 7, 11, 15]
target = 9 # output [0, 1] because nums[0] + nums[1] == 9
print(two_sum(nums, 9))

nums = [3,2,4]
target = 6 # output [1,2]
print(two_sum(nums, 6))

nums = [3,3]
target = 6 # output [0,1]
print(two_sum(nums, 6))

# 3 Isomorphic Strings - given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    iso_map = {}
    mapped_values = set()
    zipped_values = zip(s,t)

    for char_s, char_t in zipped_values:
        if char_s in iso_map:
            if iso_map[char_s] != char_t:
                return False
        else:
            if char_t in mapped_values:
                return False
            iso_map[char_s] = char_t
            mapped_values.add(char_t)

    return True    

s = "egg"
t = "add"
print(is_isomorphic(s, t)) # True

s = "too" 
t = "sar"
print(is_isomorphic(s, t)) # False

s = "paper" 
t = "title"
print(is_isomorphic(s, t)) # True

# Assessment Unit 2 Advanced A
# 4
student = {"name": "Emma", "class": 9, "grade": 'A'}
student.pop("grade")
print(student.items())

# 5
gradebook = {"class": {"student":{"name":"Mike", "grade":{"physics":'C', "history": 'B'}}}}
print(gradebook['class']['student']['grade']['history'])

# 6
def process_data(names, scores):
    result = {}
    for i in range(len(names)):
        name = names[i]
        score = scores[i]
        if name not in result:
            result[name] = []
        result[name].append(score)
    return result

names = ["Alice", "Bob", "Alice", "Bob", "Charlie"]
scores = [85, 90, 95, 80, 70]
result = process_data(names, scores)
print(result)

#7 find the bug
def filter_below_threshold(dict1, threshold):
    filtered_dict = {}
    for key, value in dict1.items():
        if value < threshold:
            filtered_dict[key] = value
    return filtered_dict

names = ["Alice", "Bob", "Alice", "Bob", "Charlie"]
scores = [85, 90, 95, 80, 70]
dict1 = dict(zip(names, scores))
print(filter_below_threshold(dict1,85))

# Test the function
sample_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 3}
threshold = 10
result = filter_below_threshold(sample_dict, threshold)
print(result)  # Output should be {'b': 5, 'd': 3}

# 1 Array Intersection 2 - given two int arrays nums1 and nums2, return
# an array of their intersection. your answer should be returned in
# ascending order
def intersect(nums1, nums2):
    from collections import Counter
    count1 = Counter(nums1)
    count2 = Counter(nums2)

    intersection = []
    for num in count1:
        if num in count2:
            intersection.extend([num] * min(count1[num], count2[num]))

    return sorted(intersection)

nums1 = [1,2,2,1]
nums2 = [2,2] # [2,2]
print(intersect(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4] # [4,9]
print(intersect(nums1, nums2))

#2 Word Pattern - given a pattern and a string s, return True if s follows
# the same pattern and False otherwise. 
def word_pattern(pattern, s):
    words = s.split()    
    if len(pattern) != len(words):
        return False

    pattern_to_word = {}
    word_to_pattern = {}

    for p, w in zip(pattern, words):
        if p in pattern_to_word:
            if pattern_to_word[p] != w:
                return False
        else:
            if w in word_to_pattern:
                return False
            pattern_to_word[p] = w
            word_to_pattern[w] = p
        
    return True

pattern = "abba"
s = "dog cat cat dog"
print(word_pattern(pattern, s)) # True

pattern = "abba"
s = "dog cat cat fish"
print(word_pattern(pattern, s)) # False

# 3 Grouped Anagrams - given a list of strings strs, group the anagrams together.
# You can return the answer in any order.

def grouped_anagrams(strs):
    if len(strs) == 0:
        return strs
    anagrams = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(grouped_anagrams(strs)) 

strs = ["a"]
print(grouped_anagrams(strs)) 

strs = [""]
print(grouped_anagrams(strs)) 


# Unit 2 Advanced B
# 5
friends = {1:{'name': 'Rachel', 'age': '27', 'job': 'Designer'}, 3:{'name': 'Ross', 'age': '277', 'job': 'Designeeeeer'}}

print(friends[3]['job'])

# 6
numbers = [1,2,3,4,5]
squared = {num: num ** 2 for num in numbers}
print(squared)

# 7
def mystery_function(words):
    result = {}
    for word in words:
        initial = word[0]
        if initial not in result:
            result[initial] = []
        result[initial].append(word)
    return result

words = ["apple", "banana", "cherry", "apricot", "blueberry", "avocado"]
result = mystery_function(words)
print(result)

# 4 debug
# merge_dicts should accept two dictionaries dict1 and dict2 and merge them into a new dictionary.
# If the same key is in both dictionaries, the value from dict2 should overwrite the value from dict1

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = value
    return merged

princess_movies = {"Snow White": 1937, "The Princess and the Frog": 2009, "Moana": 2016}
princess_movies2 = {"Snow White": 2222, "The Princess and the Frog": 2555}
print(merge_dicts(princess_movies, princess_movies2))

# does the exact same
def merge_dicts(dict1, dict2):
    merged = dict1.copy()  # Create a copy of dict1 to avoid modifying the original dictionary
    merged.update(dict2)   # Update the copy with dict2
    return merged

# Example usage
princess_movies = {"Snow White": 1937, "The Princess and the Frog": 2009, "Moana": 2016}
princess_movies2 = {"Snow White": 2222, "The Princess and the Frog": 2555}
print(merge_dicts(princess_movies, princess_movies2))

# 2 Rank Transform an Array
# given an int array, replace each element with its rank. Ranks starts from 1, if two elements
# are equal, give them the same rank.

def array_rank_transform(arr):
    # create a list of tuples (value, index)
    indexed_arr = [(value, index) for index, value in enumerate(arr)]

    # sort the list based on values
    sorted_arr = sorted(indexed_arr)

    # create a list to store the ranks
    ranks = [0] * len(arr)

    # assign ranks based on sorted order
    current_rank = 1
    for i in range(len(sorted_arr)):
        if i > 0 and sorted_arr[i][0] != sorted_arr[i-1][0]:
            current_rank += 1
        ranks[sorted_arr[i][1]] = current_rank

    return ranks

arr = [37,12,28,9,100,56,80,5,12]
print(array_rank_transform(arr)) # output [5,3,4,2,8,6,7,1,3]

arr = [40,10,20,30]
print(array_rank_transform(arr)) # [4,1,2,3]

arr = [100,100,100]
print(array_rank_transform(arr)) # [1,1,1]

# 3 Longest Substring Without Repeating Characters
# Given a string s, return the length of the longest substring without repeating characters

def length_of_longest_substring(s):
    max_length= 0
    char_set = set()
    left = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

s = "abcabcbb"
print(length_of_longest_substring(s)) # output 3

s = "bbbb"
print(length_of_longest_substring(s)) # 1

s = "pwwkew"
print(length_of_longest_substring(s)) # 3 "wke" length 3. Notice the answer must be a substring, "pwke" is 
# a subsequence, not a substring