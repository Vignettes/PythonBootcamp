
# The Syntax #
#[___ for ____ in ___]

nums = [1, 2, 3]
nums2 = [x*10 for x in nums] #multiplies each value in list by 10 creating new list.
print(nums2)


name = 'colt'
new_name = [char.upper() for char in name]
print(new_name)

friends = ['ashley', 'matt', 'michael']
friends_new = [friend[0].upper() + friend[1:] for friend in friends] # takes capital letter of each name first value, and then rest lower after 1st value
print(friends_new) 

# To create a list iterating by 10
list = [num*10 for num in range(1,6)] #[10, 20, 30, 40, 50]
print(list)


# To convert to boolean function
list = [bool(val) for val in [0, [], '']] # [False, False, False] because the boolean of True or False is evaluated on each
print(list)   # to answer the above, empty strings are false, 0 is false, empty list is false.


numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers] #loops over each value in numbers and returns it as string in new list
print(string_list)