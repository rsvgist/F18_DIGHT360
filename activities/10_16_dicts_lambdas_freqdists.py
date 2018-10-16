"""In-class activities for 02-14."""

# Dictionaries
# sorting and lambdas
# Frequency distributions


###############################################################################
print('Dictionaries')

print("Dictionaries map 'values' to 'keys'. You look up a key to find the value.")
print('Initializing a dictionary')
dict1 = {'Rachael': 38, 'Rob': 37, 'Hyrum': 12, 'Eliza': 10,
         'Wesley': 8, 'Mark': 5}
as_list = [('Rachael', 38), ('Rob', 37), ('Hyrum', 12), ('Eliza', 10),
           ('Wesley', 8), ('Mark', 5)]
dict2 = dict(as_list)
dict3 = {}
for name, age in as_list:
    dict3[name] = age
dict4 = {name: age for name, age in as_list}
print('T/F: All these dicts are the same:', dict1 == dict2 == dict3 == dict4)
print()

print('Ways to loop over a dictionary')
print('looping directly over keys...')
for key in dict1:
    print(key, dict1[key])
print()
print('Looping over .items() which is a list of 2-tuples...')
print('dict1.items():', list(dict1.items()))
for key, value in dict1.items():
    print(key, value)
print()
print('Looping over .values() (not usually very useful)...')
for value in dict1.values():
    print(value)
print()



###############################################################################
print('Lambda functions')

print('''Lambda functions are simple, disposable functions that have no name. In
order to demonstrate how they work, we will give them names by assigning them to
variables, but this is usually not how they are used. The next section will show
an excellent use case for lambdas.''')

print('Let\'s say we want a function to return the second element of a sequence.')
print('Here is the standard way to declare a function:')
def std_func_decl(x):
    return x[1]
print()

print('...and here is how to achieve the same thing using lambda notation:')
lamb_func_decl = lambda x: x[1]  # we don't usually assign a lambda to anything
print()

print('Are they the same?')
print(std_func_decl([0, 1]), lamb_func_decl([0, 1]))
print()

print('''PRACTICE A
Write lambda functions to do the following:
    * always return 4
    * given a string, return the string in lower-case
    * return the last element of a sequence
    * print whatever it is given
''')

###############################################################################
print('Sorting with keys and/or reversed ')
print('Sorting "keys" are not the same kind of key as in dict key-value pairs.')

print('Let\'s sort as_list from the dictionary section.')
print(as_list)
print(list(sorted(as_list)))
print()

print('By default, sorted() sorts by >  and < operators.')
print('Tuples (and really all sequences) are compared by their first item:', ('Rob', 36) < ('Hyrum', 11))
print('What if we want to sort by a specific part of the tuple?')

print('Sorting by age:')
print(list(sorted(as_list, key=lambda x: x[1])))
print()

print('''This is the same as sorted(as_list, key=std_func_decl) or
sorted(as_list, key=lamb_func_decl), but you never have to give the function a
name. Notice that we would not be calling these functions because they do not
have (). We are passing the function itself as an argument.''')
print()

print('''PRACTICE B:
Sort as_list by...
    * the second letter of the name
    * the last letter of the name
''')
print()

print('Sorting in reverse order:')
print(list(sorted(as_list, key=lambda x: x[1], reverse=True)))
print()

