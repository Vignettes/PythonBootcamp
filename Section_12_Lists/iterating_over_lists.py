### FOR LOOP ###

numbers = [1,2,3,4] #list of 1-4

for number in numbers: #for each number in the list numbers
    print(number) #print the number
    
    
### WHILE LOOP ###    

numb = [1, 2, 3, 4]
i = 0

while i < len(numb):
    print(numb[i])
    i += 1
    
    
    
### Write code that loops over the list and adds all the strings together to form one large combined string.
### Oh, it should be in UPPERCASE as well. Save it to a variable called result.

result = ''  #sets a variable called result empty

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"] #creates a list with these strings

for sound in sounds: #for each value sound initialized in the list sounds 
    result += sound.upper() #combine them in uppercase. 
