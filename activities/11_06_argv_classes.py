"""In-class activities for 11-06."""

# argv
# classes (objects)

##############################################################################
print('#' * 79)
print('''sys.argv

When you define a function, you can specify parameters that are used to pass
data inside the function:

def test(arg1):
    print(f'The argument is {repr(arg1)}.')

>>> test('over')
The argument is 'over'.

A similar thing can be done at the script level, so that when you execute it at
the command line, you can pass arguments that will be used inside the script.

import sys
print(sys.argv)
''')

print()
print('#' * 79)
print('''PRACTICE A

At the bash command line, read argv.py using `less`. Then, run argv.py with
arguments and see what happens. Pass more than one argument. By default, bash
splits arguments on spaces. Can you get bash to pass an argument to python that
includes a space?
''')
input('Press return to continue.')
print()

print('''PRACTICE B

Write a script named `write_a_file_named.py` that takes an argument through
sys.argv and saves it as a variable `filename`. Then open a new file with that
name and write the string 'It worked!' to that file. Finally, call your script
as follows:

$ python3 write_a_file_named.py arbitrary.txt
''')
input('Press return to continue.')
print()

print('''PRACTICE C

Write a script called `print_count.py` that takes any number of argv arguments
and prints each filename and the number of print function calls in that file.

''')
input('Press return to continue.\n\n\n')


print('#' * 79)
print('''Classes (objects)

Python is a strongly-typed programming language, which means that it is likely
to generate an error or refuse to compile if the argument passed to a function
does not closely match the expected type. We already know many of the built-in
objects, like str, list, dict, tuple, int, float, etc. We have also seen how
programmers have built custom objects, like nltk.Text and nltk.FreqDist.

Today, we will learn to build our own objects. See the following minimal
example. Note that by convention, class names are always CapWords.
''')


class Example:
    """Example class that does absolutely nothing."""
    pass


e = Example()  # create an instance of an Example object
print('Printing e...', e, dir(e), type(e))
input('Press return to continue.')
print()

print('Object attributes')
print('Each instance of an object has a local namespace.')

e.pi = 3.14  # store a float
e.magic_word = 'please'  # store a str
e.print_function = print  # store a function

print('e.print_function-ing e.pi and e.magic_word ...')
e.print_function(e.pi, e.magic_word)
print()

print('printing e.__dict__ ...', e.__dict__)  # dict of namespace

input('Press return to continue.')
print()

print('Making a class actually do something.')

print('''A class declaration tells python how to build an instance of a class. A
class is the cookie cutter that makes the cookies. The workhorse of building the
instance is the __init__() method. This method defines what attributes belong to
the instance. When you initialize an instance, the arguments given are passed
directly to the __init__() method.

`self` is always the first argument of every method. It refers to the instance
that will be created by the class.
''')


class Pet:
    """Animal that belongs to a human."""

    def __init__(self, name, age, species=None):
        """Build a Pet object.

        name -- name of the Pet
        age -- age (in years) of the Pet
        """
        self.name = name
        self.age = age
        self.species = species

    def __repr__(self):  # Return unambiguous string representation of self
        """Return repr(self)."""
        return f'Pet(name={self.name}, age={self.age}, species={self.species})'

    def print_name(self):
        """Print the name attribute."""
        print(self.name)


fido = Pet('Fido', 2)
luna = Pet('Luna', 3)
print(fido, luna)

input('Press return to continue.')
print()

print('''Now if you want to make an object that inherits all the structure and
methods of an existing object, you can subclass an object. The following example
subclasses the Pet object. ''')


class Dog(Pet):
    """Canine version of Pet."""

    def __init__(self, name, age):
        """Build a Dog object."""
        # Run the __init__() method of Pet class; super() refers to Pet
        super().__init__(name, age, species='Dog')
        self.has_tail = True
        self.has_fur = True
        self.is_mammal = True


oscar = Dog('Oscar', 4)
print(oscar)

input('Press return to continue.')
print()

print('''PRACTICE D

Write a script using `snakes_and_ladders_template.py` to play Snakes & Ladders.

''')
input('Press return to continue.')
