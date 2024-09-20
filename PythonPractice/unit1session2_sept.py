# Problem 1: Reverse Sentence
# Write a function reverse_sentence() that takes in a string sentence and returns the sentence 
# with the order of the words reversed. The sentence will contain only alphabetic characters 
# and spaces to separate the words. If there is only one word in the sentence, the function 
# should return the original string.

def reverse_sentence(sentence):
   new_sentence = sentence.split()
   if len(new_sentence) == 1:
       return sentence
   else:
       reversed_sentence = ' '.join(new_sentence[::-1])
       return reversed_sentence

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))


# Session 2 problem 7

def nanana_batman(x):
    # Initialize an empty string to accumulate the "na"s
    na_string = ""
    
    # Use a for loop to repeat "na" x times
    for _ in range(x):
        na_string += "na"
    
    # Concatenate " batman!" to the repeated "na" string
    result = na_string + " batman!"
    
    # Print the result
    print(result)

nanana_batman(6)