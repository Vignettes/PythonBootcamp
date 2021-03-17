### Write a function called is_palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same
### backwards as it reads forward. This function should take in one parameter and return True or False depending on where it is a palindrome.
### As a bonus, allow your function to ignore whitespace and capitilization so that is_palindrome('a man a plan a canal Pamama') returns True.

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(a):
    b = a[::-1]  # create new variable b, which is the inverse of a
    if a == b:
        return True
    return False
    
    
is_palindrome("hi")
    