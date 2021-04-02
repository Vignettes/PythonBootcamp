#A range is just a slice of a number line. 

range(7) #gives you 0 to 6
range(1,8) #gives you 1 to 7  || two parameters
range(1,10,2) #give you odds from 1 to 10

r = range(10)
print(list(r))
print(r)

for num in range(0,100,5): #print 0-99 by 5
    print(num)
    
    

x = 0
for num in range(10,21,2):
    x += num
print(x)