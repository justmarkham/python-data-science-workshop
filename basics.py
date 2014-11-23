'''
Multi-line comments go between 3 quotation marks.
You can use single or double quotes.
'''

# One-line comments are preceded by the pound symbol


# BASIC DATA TYPES

x = 5               # creates an object
print type(x)       # check the type: int (not declared explicitly)
type(x)             # automatically prints
type(5)             # assigning it to a variable is not required
type(5.0)           # float
type('five')        # str , single or double quotes
type(True)          # bool


# LISTS

nums = [5, 5.0, 'five']     # multiple data types
nums                        # print the list
type(nums)                  # check the type: list
len(nums)                   # check the length: 3
nums[0]                     # print first element
nums[0] = 6                 # replace a list element
nums[3]
nums.append(7)              # list 'method' that modifies the list
help(nums.append)           # help on this method
help(nums)                  # help on a list object
nums.remove('five')         # another list method
nums.append("five")
nums.append("apple")
sorted(nums)                # 'function' that does not modify the list
nums                        # it was not affected
nums = sorted(nums)         # overwrite the original list
sorted(nums, reverse=True)  # optional argument
sum(nums)                   # returns sum of a list of numbers


# FUNCTIONS

def give_me_five():         # function definition ends with colon
    print "about to give you five"    
    return 5                # indentation required for function body
print "gave you five"
give_me_five()              # prints the return value (5)
a_new_variable = give_me_five()        # assigns return value to a variable, doesn't print it

a_new_variable == 6

def calc(x=1, y=2, op = "add"):         # three arguments (without any defaults)
    if op == 'add':         # conditional statement
        return x + y
    elif op == 'subtract':
        return x - y
    elif op == "multiply":
        return x * y
    else:
        print 'Valid operations: add, subtract, multiply'

calc(5, 3, 'add')
calc(5, 3, 'subtract')
calc(5, 3, 'multiply')
calc([1,2],[3,4], "add")
calc("sinan",[1,2], "add")
calc(5, 3)

calc()

import math				# import statement

flubber = [2, 5, 7, 4, 2, 5]
len(flubber)
[x**2 for x in flubber]    # list comprehension
[x / 2.0 for x in flubber] #note the 2.0 instead of 2
[math.sqrt(x) for x in flubber]


point_1 = (1, 2, 2)   #tuples have a paranthesis
point_2  = (3, 4, 5)

pairs = zip(point_1, point_2)
for x in pairs:
    print x
    print x[0]
    print x[1]

[x[0] for x in pairs]


def euclidean_distance(point_1, point_2): # == 4.123105625617661
    zipped_numbers = zip(point_1, point_2) #zips the two tuples together, also works on lists
    differences_squared = [(x1 - y1)**2 for x1, y1 in zipped_numbers]
    sum_of_differences = sum(differences_squared)
    return math.sqrt(sum_of_differences)
    
    
def euclidean_distance2(point_1, point_2): # == 4.123105625617661
    zipped_numbers = zip(point_1, point_2) #zips the two tuples together, also works on lists
    differences_squared = [(x[0] - x[1])**2 for x in zipped_numbers]
    sum_of_differences = sum(differences_squared)
    return math.sqrt(sum_of_differences)
    
def euclidean_distance3(point_1, point_2): # == 4.123105625617661
    zipped_numbers = zip(point_1, point_2) #zips the two tuples together, also works on lists
    sum_of_list = 0    
    for pair in zipped_numbers:
        print pair
        print pair[0] - pair[1]
        sum_of_list = sum_of_list + (pair[0] - pair[1])**2
    return math.sqrt(sum_of_list)   


    
    
    
    
euclidean_distance3(point_1, point_2)












