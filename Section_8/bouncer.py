#ask for age

age = input("How old are you: ")
if age: 
    age = int(age) #if there is an age string creates age integer.
    if age >= 18 and age < 21:
        #18-21 wristband
        print("You can enter, but need a wristband")
    elif age >= 21:
        #21+ drink, normal entry
        print("You can enter, and buy drinks")
    else: 
        #<18 too young, sorry
        print("You are too young, kiddo")
else:
    print("Please enter an age!")
        





