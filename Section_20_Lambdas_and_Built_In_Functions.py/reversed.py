### Reversed
### Returns a reverse iterator

nums = [1,2,3,4]
nums.reverse()
print(nums) # prints the reverse [4,3,2,1]

# Say we want to reverse the string 'hello'
list(reversed('hello')) # ['o', 'l', 'l', 'e', 'h']
print(''.join(list(reversed('hello')))) # olleh
# Above uses the .join() to join together the list after reversing it. 