### Lambdas are often used when you have code that you need to pass a function into another function as a parameter.
### and that function will never be used again.

square2 = lambda num: num * num 
add = lambda a,b: a + b # variable created, lambda a,b: a + b sets add(a,b) to add a + b and return

print(add(3,10))


### Example use below ###
''' 
import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)

button = tk.Button(frame,
                   text='Click Me!',
                   fg='red',
                   command=lambda: print('Hello')) # Lambda is useful here, as it's a function used only here. 

button.pack(side=tk.LEFT)
root.mainloop()
 '''



### Write a lambda that accepts a single number and cubes it. Save it in a variable called 'cube'. 

cube = lambda a: a * a * a
print(cube(3)) # 27

# or

cube = lambda num: num ** 3