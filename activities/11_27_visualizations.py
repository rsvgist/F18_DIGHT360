"""In-class activities for 11-29."""

import numpy as np

print('''Visualizations with matplotlib.pyplot

I recommend working on your laptop today if you have one. If you don't, you may
want to sit next to someone who has a laptop. This is because pythonanywhere
only gives us bash/python consoles, and consoles cannot display images.

All of the following code will only work in a gui environment. However, you can
save image files by using the idiom instead of `plt.show()`:

>>> fig = plt.gcf()  # get current figure
>>> fig.savefig('filename.png')

The following code is adapted from this website:
https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

''')
input('[enter] to continue...')
print('drawing simple line...')
import matplotlib.pyplot as plt
seq = [1, 2, 3, 4, 5, 6]
plt.plot(seq)
plt.ylabel('some numbers')
plt.show()
input('[enter] to continue...')


print('drawing parabolic line...')
seq2 = [i ** 2 for i in seq]
plt.plot(seq, seq2)
plt.show()
input('[enter] to continue...')


print('''PRACTICE A

Write a new list `myseq` and try generating plots. Change the numbers to higher
and lower values. Use more or fewer numbers. Play around until you are
comfortable drawing line graphs.

''')
input('[enter] to continue...')


print('Plotting points using custom marking shape/color...')
plt.plot(seq, seq2, 'ro')  # r = red; o = circle
plt.axis([0, 10, 0, 100])  # Usually automatic axis lengths are best; this is just an example of how to change it if needed.
plt.show()
print('For all marker formatting options, see https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot')
input('[enter] to continue...')

print('''PRACTICE B

Use different combinations of marker formatting on the website shown above.
Draw lines and dots of different colors and shapes. Tinker.

''')
input('[enter] to continue...')


print('Drawing multiple series using various shapes/colors...')
seq3 = [i ** 3 for i in seq]
plt.plot(seq, seq, 'r--', seq, seq2, 'bs', seq, seq3, 'g^')
plt.show()
input('[enter] to continue...')

print('''PRACTICE C

Write a script that plots the sorted document length distributions from the
Mini-CORE corpus, with a different marker style for each genre.

Compute a document's length by using `nltk.word_tokenize()` and `len()`.

For each genre, you need a list of integers in reverse sorted order (highest
first).

''')
input('[enter] to continue...')

print('drawing barplot, scatterplot, and boxplots...')
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.bar(names, values)
plt.show()

plt.scatter(names, values)
plt.show()

plt.plot(names, values)
plt.show()

plt.boxplot([1, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 11])
plt.show()

plt.boxplot([[1, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 11],
             [1, 1, 1, 1, 1, 2, 2, 2, 4, 7, 8, 9, 13]])
plt.show()
input('[enter] to continue...')


print('drawing a histogram...')
# Generate a normal distribution
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)  # numpy syntax is different, just ignore this

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
print(n)
print(bins)
print(patches)

# add some text
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
