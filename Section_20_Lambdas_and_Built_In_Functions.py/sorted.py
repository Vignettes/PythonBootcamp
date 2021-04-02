### Returns a new sorted list from the items in the iterable
### sorted (works on anything that is iterable)

more_numbers = [6, 1, 8, 2]
sorted(more_numbers) # [1, 2, 6, 8]
print(more_numbers) # [6, 1, 8, 2]
# It does not permanently alter the iterable. 

# With sorted() you can use the following sorted(more_numbers, reverse=True) to reverse the order
sorted(more_numbers, reverse=True) # [8, 6, 2, 1]

# Now let's try this with a dictionary
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

print(sorted(users, key=len)) # sorts the dictionary, by length of the dictionary, ascending order.

#[{'username': 'samuel', 'tweets': ['I love cake', 'I love pie', 'hello world!']}, 
# {'username': 'katie', 'tweets': ['I love my cat']}, {'username': 'doggo_luvr', 
# 'tweets': ['dogs are the best', "I'm hungry"]}, {'username': 'guitar_gal', 'tweets': []}, 
# {'username': 'jeff', 'tweets': [], 'color': 'purple'}, {'username': 'bob123', 'tweets': [], 
# 'num': 10, 'color': 'teal'}]

print(sorted(users, key=lambda user: user['username'])) 
# setting key to lambda, then inserting the lambda causes us to sort based on the username in dictionary, ascending order

print(sorted(users, key=lambda user: len(user['tweets']))) 
# sorts by the number of tweets within users