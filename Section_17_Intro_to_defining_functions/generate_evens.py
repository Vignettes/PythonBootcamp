## Write a function that returns even numbers 1-50 not including 50

def generate_evens():
    evens = []
    i = 1
    while i < 49:
        if i % 2 == 0:
            evens.append(i)
        i += 1
    print(evens)
    return evens

generate_evens()


def generate_evens():
    evens = [num for num in range(1,50) if num % 2 == 0]
    print(evens)
generate_evens()