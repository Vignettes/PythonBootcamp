### We can try, we can do something else, and finally we can do more

# try:
# except:
# else:
# finally:

try:
    num = int(input("please enter a number"))
except:
    print("that is not a number")
else:
    print("Good work you entered a number")
    break # stops the loop
finally:
    print("Runs no matter what")
    