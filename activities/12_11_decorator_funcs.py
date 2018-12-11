"""In-class activities for 04-16."""


print('''Decorator functions

Decorator functions wrap other functions, modifying their behavior. Usually
they take a function as an argument, and they return a function that does
something before or after (or before AND after) it calls the input function.
''')


def demo_decorator(input_func):
    """Decorator function to demonstrate how decorators work."""
    print(f'demo_decorator is wrapping {input_func.__name__}!')

    def wrapper_func():
        print(f'Something BEFORE {input_func.__name__} is called.')
        input_func()
        print(f'Something AFTER {input_func.__name__} is called.')

    return wrapper_func


def some_function():
    print('I am some_function!')


print('Decorate the function...')
some_function = demo_decorator(some_function)

print('\n\nCall the decorated function...')
some_function()

input('Press [return] to continue.\n')


print('''Now let's do something a little more meaningful with a wrapper.

In order to time how long something takes, the following idiom is common:

from time import time

t1 = time()
some_function()
t2 = time()
print(f'Time it took to run the function: {t2 - t1} seconds')

PRACTICE A

Write and use a decorator function that times how long the following function
takes to complete.

def time_waster():
    for i in range(1000000):
        i = i / 7

''')

input('Press [return] to continue.\n')


print('''Python has a very succint way to implement decorators. This syntactic
sugar can be referred to as "pie syntax." Instead of...

>>> some_function = demo_decorator(some_function)

...you simply write @demo_decorator on the line before the function
declaration. The code below implements demo_decorator using pie syntax.
''')

print('Declare another_function with pie-syntax decorator...')


@demo_decorator
def another_function():
    print('I am another_function!')


print('\n\nCall the decorated function...')
another_function()

input('Press [return] to continue.\n')
