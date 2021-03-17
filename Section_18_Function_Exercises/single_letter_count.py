### Write a function called single_letter_count. This function takes in two parameters (two strings).
### The first parameter shoul dbe a word and the second shoul dbe a letter. The function returns the
### number of times that letter appears in the word. The function should be case insensitive.
### If the letter is not found in the word, the function should return 0.
### Hint: use count()

'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:

def single_letter_count(a,b): # first should be word, second should be letter
    counted = a.lower().count(b) # counted variable equal to the number of times b appears in a as a lowercase string
    if counted > 0: # if counted is higher than 0
        return counted # return counted
    return 0 # otherwise we return 0
    
single_letter_count("Hi", "i")