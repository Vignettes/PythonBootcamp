### Set comprehension ###

print({x**2 for x in range(10)}) # Notice no k: v like in dictionary comprehension

string = "hello"
string_comp = {char for char in string if char in 'aeiou'} # character in string if character in aeiou
string_test = len({char for char in string if char in 'aeiou'})

if string_comp == string_test: # if the length of string_test == string_comp meaning all letters present, print great
    print("Great")
else:
    print("Fail")
