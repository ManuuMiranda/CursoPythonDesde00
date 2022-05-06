
"""                            LISTS:
Lists are mutable sequences, typically used to store collections of homogeneous items
(where the precise degree of similarity will vary by application)
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting a position 4

fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()

"""
The list methods make it very easy to use a list as a stack
    •last element added is the first element retrieved (“last-in, first-out”, LIFO). 
To retrieve an item from the top of the stack, use pop() without an explicit index. 

Lists are not efficient for FIFO queues. 
While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow 
(because all the other elements must be shifted by one).

To implement a queue, use double-ended queues, from collections (collections.deque), pronounced “deck”
                                               Designed to have fast appends and pops from both ends. 
"""

# def sorting_criteria(student: tuple[str, str, int]) -> int: return student[2] == lambda student: student[2]

student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

sorted(student_tuples)


"""                                SETS:
A set (conjunto) is an unordered collection with no duplicate elements. 
Basic uses include membership testing and eliminating duplicate entries. 
Set objects also support mathematical operations like union, intersection, difference, and symmetric 
difference.
Curly braces {} or the set() function can be used to create sets.
            ----> to create an empty set you have to use set(), not {} -> this creates an empty dictionary
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # show that duplicates have been removed
'orange' in basket  # fast membership testing
'crabgrass' in basket

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')


""" OPERATION'S IN SETS """

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
a - b                              # letters in a but not in b
a | b                              # letters in a or b or both
a & b                              # letters in both a and b
a ^ b                              # letters in a or b but not both


"""                           TUPLES:
Tuples are immutable sequences, typically used to store collections of heterogeneous data.
keys in dict, where immutable objects are required
"""

t = 12345, 54321, 'hello!'
t[0]
t
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# Tuples are immutable:
t[0] = 88888 # Da error porque no se puede modificar
# But they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v

"""
Note that it is actually the comma which makes a tuple, not the parentheses -> Except in the empty tuple case, 
or when they are needed to avoid syntactic ambiguity. 
For example, f(a, b, c) is a function call with three arguments, while f((a, b, c)) is a function call with a 3-tuple 
as the sole argument.
"""

tuple([1, 2, 3])


def fib(n):
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b


tuple(fib(10))

"""                       SEQUENCE PACKING AND UNPACKING:
Works for any sequence, requires that there are as many variables on the left side of 
the equals sign as there are elements in the sequence. 
Note that multiple assignment is really just a combination of tuple packing and sequence unpacking."""

# Packing
t = 12345, 54321, 'hello!'
# Unpacking
x, y, z = t
tuple([1, 2, 3])


"""
The range type represents another way of creating an an immutable sequence of numbers and is commonly 
used for looping a specific number of times in forloops.

Not a tuple, items are calculated dynamically

Small amount of memory, no matter the size of the range it represents 
(as it only stores the start, stop and step values)
"""