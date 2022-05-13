# A Dictionary is a set of key:value pairs, keys have to be unique
# {} creates an empty dictionary

# Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dict

tel = {'jack': 4098, 'sape': 4139}
print(tel)

"""
Dictionaries are indexed by keys not by a range of numbers like sequences
    Keys  can be any inmutable type:
        Strings and numbers can always be keys
        Tuples can be used as keys if they contain only strings, numbers or tuples
        If a tuple contains any mutable object directly or indirectly, it cannot be used as a key
        Lists can not be keys because lists can be modified in place using index,slice or methods like append()
        
    Mutable vs Inmutable Objects: Mutable if internal state of the object can be changed.
                                  Inmutable does not allow any change in the object once it has been created
"""


# Operations with Dictionaries I:
# Main are storing a value with some key and extracting the value given the key
# Also deleting a key:value pair with -> del
# If you store using a key that is already in use, the old value associated with that key is forgotten.
# Error to extract a value using a non-existing key

tel['guido'] = 4127
tel
tel['jack']
del tel['sape']
tel['irv'] = 4127

"""
Dictionaries insertion order:
    Dictionaries preserve insertion order, updating a key does not affect the order
    Keys added after deletion are inserted at end
"""

d = {"one": 1, "two": 2, "three": 3, "four": 4}
it = d.popitem()
d.update({"one": 3, "five": 5})
print(d)


# Operations with Dictionaries II:
# Performing list() on a dictionary returns a list of all the keys used in the dictionary, in insertion order
# If you want it sorted -> use sorted()

# To check whether a single key is in the dictionary, use the 'in' keyword.

list(tel)
sorted(tel)

'guido' in tel
'jack' not in tel


"""
As discussed earlier, dictionary raises a KeyError if key is not in the map, a way of controlling this behavior 
is creating a subclass of dict and adding a __missing__() method:

    •If a subclass of dict defines a method __missing__() and key is not present, the d[key] operation calls that 
    method with the key key as argument. 
    
    •The d[key] operation then returns or raises whatever is returned or raised by the __missing__(key) call. 
    
    •__missing__() must be a method -> it cannot be an instance variable
"""

"""        DEFAULT DICT:        """
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
sorted(d.items())

s = 'mississippi'
d = defaultdict(lambda: 0)
for k in s:
    d[k] += 1
sorted(d.items())
