### Why OOP? ###
# It is a human way of thinking.
# With OOP, the goal is to encapsulate your code into logical, hierachcial groupings
# using classes so taht you can reason about your code at a higher level.

# Example
# Say we want to model a game of poker in our program

# We could have the following entities:
# Game 
# Player
# Card
# Deck
# Hand
# Chip
# Bet

# Card deck possible implementation (pseudocode)
# Deck {class}
# _cards {private list attribute}
# _max_cards {private int attribute}
# shuffle {public method}
# deal_card {public method}
# count {public method}

# The underscore is stating it is private and to be used on that entity only.

# Encapsulation
# Encapsulation - the grouping of public and private attributes and methods into a programmatic class,
# making abstraction possible.

# Example
# Designing the Deck class, I make cards a private attribute (list) 
# I decide that the length of the cards should be accessed via a public method called count() -- i.e. Deck.count()s

# Abstraction
# Abstraction - exposing only "relevant" data in class interface, hiding private attributes and methods 
# (aka the 'inner workings') from users

# In the real world we access the top-level interface of objects, the inner-workings are hiden below. 
# Example: You turn the wheel of your car, you don't have to access the inner-mechanics to engage the movement of the vehicle.
