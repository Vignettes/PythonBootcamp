
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