### Write a function called compact. This function should accept a list and return a list of values
### that are truthy values withou any of the falsey ones.

def compact(listed):
    cleaned = [x for x in listed if x]
    print(cleaned)
    return cleaned

compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]