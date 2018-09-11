"""Practice string manipulation and regular expressions."""

# Practice:
"""1) Create a program that asks the user for a number between 1 and 10 and
prints back to the user one of two messages stating whether the number is:
(a) less than five, or (b) greater than or equal to five.

2) Modify the previous program so that the program prints back to the user
one of three messages: (a) less than, (b) equal to, or (c) greater than five.

3) Modify the previous program so that the message printed back to the user
indicates whether the number is: (a) between one and three, (b) between four
and six, or (c) between seven and ten.

4) Create a program that asks the user for his/her two favorite fruits and
prints a message stating whether the first fruit given by the user comes
before or after the second one in a dictionary (in alphabetical order).

5) Modify the previous program so that the message printed back to the user
indicates which of the two fruits given by the user, or neither or both,
falls between "guava" and "passion fruit" in the dictionary.  Hint: You'll
need both and and or, several elif statements, and parentheses to force order
of operations.  Bonus: Modify your program so that if the user gives "guava"
or "passion fruit," the message states this fact."""

###############################################################################

"""6) Write a program that asks the user for a word of at least six letters in
length, then prints back to the user on one line the first three letters, and
then on a second line prints the last three letters.

7) Modify the program to print out every other letter.

8) Modify the program to print out the word spelled backward."""


###############################################################################
REGULAR EXPRESSIONS
"""A domain-specific language (or mini language or tiny language) to concisely
match patterns of characters within strings.

Use regex101.com or pythex.org if you'd like to test regexes (but make sure to
run each regex in pythonanywhere or on your own machine to see how to actually implement it in a script, e.g. `import re`, etc.):"""
# 1)  a string with "ed" at the end
# 2)  a word with "ed" at the end
# 3)  a word with "anti" at the beginning
# 4)  both the American and British spellings of "labour/labor"
# 5)  'Jack', 'Mack', 'Pack'
# 6)  both the American and British spellings of "center/centre"
# 7)  an eight-letter word with 'j' as the third letter and 't' as the sixth letter
# 8)  words other than "best" that end in "est"
# 9)  a more concise regex than "(make|makes|made)"
# 10) two words next to each other with the same final letter (Hint: Use parentheses to capture and then "\1" to match the previously caught match.)
# 11) modify the previous regex to not consume the second word (so that it's available for another search) Hint: Use positive lookahead, that is, "(?=...)"
# 12) The bracketed portion of "Thi{s is a first example s}entence." Hint: Use greedy matching.
# 13) The bracketed portions of "Thi{s is} a fir{st example s}entence." Hint: Use lazy/non-greedy matching.
# 14) Words that begin with "t" regardless of case, that is, "T" and "t", in the following sentence: "The deal is that I make dinner every night, but Juanito made it last night." Hint1: Look up the "re.IGNORECASE" parameter of the re.findall() function.  Hint2: "re.IGNORECASE" has an abbreviation of "re.I".  Hint3: You may need to escape the word boundary character "\b" with an additional backslash, that is, "\\b".
#
