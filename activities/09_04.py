"""Prepare to complete Assignment 1."""

###############################################################################
# Control flow: `if`, `elif` and `else`
# `if` introduces a code block that only runs if the condition evaluates to True

print('Does 2 equal 2?')
if 2 == 2:
    print('Yes! Math works!')

print('Is True always true?')
if True:
    print('Yes! Always print this sentence because True is always True.')
print()

# `elif` introduces a code block that only runs if the `if` condition was False
# and the `elif` condition is True.

print('Example 1:')
if 2 == 2:  # This is True
    print('Math works!')
elif 2 == 2:  # This is also True
    print('Math still works!')  # This does not run because `if` was True
print()

print('Example 2:')
if 2 == 3:  # This is False
    print('Math is broken!')
elif 2 == 2:  # This is True
    print('Math works!')  # This runs because `if` was False
print()

# `else` introduces a code block that only runs if all preceding conditions
# were False. `else` does not have a truth condition.

print('Example 3:')
if 2 == 3:  # This is False
    print('Math is broken!')
elif 2 == 4:  # This is False
    print('Math is still broken!')
else:
    print('All numbers are not created equal!')
print()


###############################################################################
# `while` loops
# A `while` loop is a block of code that runs while the condition is True.

print('Countdown from 4 using a `while` loop')
x = 4
while x > 0:
    print(x)
    x -= 1  # This is shorthand for `x = x - 1`
print()

# To make a loop run "forever", write a condition that is always True.
# To "break" an infinite loop, type [Ctrl] [C]
# input('Guess my favorite color: ')
# while True:
#     input('Nope! Try again: ')
# print()

###############################################################################
# Testing for membership using `in`
# You can test whether an object is in a dict, list, set, str, tuple, etc.
# using the keyword `in`

print('T/F: There is an "i" in "team":', 'i' in 'team')
print('T/F: 4 is a prime number:', 4 in [2, 3, 5, 7, 11, 13, 17, 19])
print('T/F: Bob is in The Chipmunks:', 'Bob' in ['Alvin', 'Simon', 'Theodore'])
print()

###############################################################################
# Replace text in a string using `replace()` method
# Strings have a handy method to replace characters

orig_str = 'I want to hug you!'
print(orig_str, '-->', orig_str.replace('ug', 'it'))
print()

###############################################################################
# Slicing sequence objects
# You can access parts of strings, lists and tuples by 'slicing' them

my_list = list(range(10))
print('my_list', '-->', my_list, sep='\t')
print('my_list[4]', '-->', my_list[4], sep='\t')
print('my_list[-1]', '-->', my_list[-1], sep='\t')
print('my_list[2:4]', '-->', my_list[2:4], sep='\t')
print('my_list[:4]', '-->', my_list[:4], sep='\t')
print('my_list[4:]', '-->', my_list[4:], sep='\t')
print('my_list[4:-1]', '-->', my_list[4:-1], sep='\t')
print('my_list[-3:]', '-->', my_list[-3:], sep='\t')
print("'working'[:4]", '-->', 'working'[:4], sep='\t')
print("'working'[-3:]", '-->', 'working'[-3:], sep='\t')

###############################################################################
# str.endswith()
# 'who' + 'le'
