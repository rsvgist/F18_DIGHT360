"""In-class activities for 02-21."""


###############################################################################
print('Sentiment analysis')

from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia

sentences = [
            'Jeremy is smart, handsome, and funny.', # positive sentence example
            'Jeremy is smart, handsome, and funny!', # punctuation emphasis handled correctly (sentiment intensity adjusted)
            'Jeremy is very smart, handsome, and funny.',  # booster words handled correctly (sentiment intensity adjusted)
            'Jeremy is VERY SMART, handsome, and FUNNY.',  # emphasis for ALLCAPS handled
            'Jeremy is VERY SMART, handsome, and FUNNY!!!',# combination of signals - Jeremy appropriately adjusts intensity
            'Jeremy is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!',# booster words & punctuation make this close to ceiling for score
            'The book was good.',         # positive sentence
            'The book was kind of good.', # qualified positive sentence is handled correctly (intensity adjusted)
            'The plot was good, but the characters are uncompelling and the dialog is not great.', # mixed negation sentence
            'A really bad, horrible book.',       # negative sentence with booster words
            "At least it isn't a horrible book.", # negated negative sentence with contraction
            ':) and :D',     # emoticons handled
            '',              # an empty string is correctly handled
            'Today sux',     #  negative slang handled
            'Today sux!',    #  negative slang with punctuation emphasis handled
            'Today SUX!',    #  negative slang with capitalization emphasis
            "Today kinda sux! But I'll get by, lol", # mixed sentiment example with slang and constrastive conjunction 'but'
             'This is awful.',
             'My date was really memorable!',
             'What a terrible show! Do not waste your money!',
             'I can\'t wait to get started on my new project.',
             'Python is the BEST!!!!!!!',
             'It was meh.',
             'I never want to do that again!'
            ]

hal = sia()
for sentence in sentences:
    print(sentence)
    ps = hal.polarity_scores(sentence)
    for k in sorted(ps):
        print('\t{}: {:> 1.4}'.format(k, ps[k]), end='  ')
    print()
input('[enter] to continue...')

###############################################################################
print('Machine learning')

print('https://machinelearningmastery.com/machine-learning-in-python-step-by-step/')
    

import matplotlib.pyplot as plt
import pandas
from pandas.tools.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# import model classes
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Load dataset
filename = 'iris.data'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
with open(filename) as iris_file:
    dataset = pandas.read_csv(iris_file, names=names)  # pandas DataFrame
print(type(dataset))
input('[enter] to continue...')

# Summarize the data
print('"Shape" of dataset:', dataset.shape,
      '({} instances of {} attributes)'.format(*dataset.shape))
print()
print('"head" of data:\n', dataset.head(20))  # head() is a method of DataFrame
print()
print('Description of data:\n:', dataset.describe())
print()
print('Class distribution:\n', dataset.groupby('class').size())
print()
input('[enter] to continue...')

# Visualize the data
print('Drawing boxplot...')
dataset.plot(kind='box', subplots=True, layout=(2, 2),
             sharex=False, sharey=False)
fig = plt.gcf()  # get current figure
fig.savefig('boxplots.png')

# histograms
print('Drawing histograms...')
dataset.hist()
fig = plt.gcf()
fig.savefig('histograms.png')

# scatter plot matrix
print('Drawing scatterplot matrix...')
scatter_matrix(dataset)
fig = plt.gcf()
fig.savefig('scatter_matrix.png')
print()
input('[enter] to continue...')

print('Splitting training/development set and validation set...')
# Split-out validation dataset
array = dataset.values
features = array[:,0:4]  # comma in slice signifies a tuple (tuples in slices is a numpy array thing)
labels = array[:,4]
print('\tfull original data and their respective labels:')
print(features[:5], labels[:5], sep='\n\n', end='\n\n\n')
validation_size = 0.20
seed = 7
feats_train, feats_validation, labels_train, labels_validation = model_selection.train_test_split(features, labels, test_size=validation_size, random_state=seed)
print('\ttraining data:\n', feats_train[:5],
      '\ttraining labels:\n', labels_train[:5],
      '\tvalidation data:\n', feats_validation[:5],
      '\tvalidation labels:\n', labels_validation[:5], sep='\n\n')

# Test options and evaluation metric
seed = 7  # seeds the randomizer so that 'random' choices are the same in each run
scoring = 'accuracy'
print()

print('Initializing models...')
# Spot Check Algorithms
models = [('LR', LogisticRegression()),
          ('LDA', LinearDiscriminantAnalysis()),
          ('KNN', KNeighborsClassifier()),
          ('CART', DecisionTreeClassifier()),
          ('NB', GaussianNB()),
          ('SVM', SVC())]
print('Training and testing each model using 10-fold cross-validation...')
# https://chrisjmccormick.files.wordpress.com/2013/07/10_fold_cv.png
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, feats_train, labels_train,
                                                 cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = '{}:\t{:.4f}\t({:.4f})'.format(name, cv_results.mean(),
                                         cv_results.std())
    print(msg)
print()

print('Drawing algorithm comparison boxplots...')
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
fig = plt.gcf()
fig.savefig('compare_algorithms.png')
print()

# Make predictions on validation dataset
# Using svc because it performed best on cross-validation
final_model = SVC()
final_model.fit(feats_train, labels_train)
predictions = final_model.predict(feats_validation)
print('Accuracy:', accuracy_score(labels_validation, predictions))
print()
print('Confusion matrix:')
cm_labels = 'Iris-setosa Iris-versicolor Iris-virginica'.split()
print('labels:', cm_labels)
print(confusion_matrix(labels_validation, predictions, labels=cm_labels))
print()
print('Classification report:')
print(classification_report(labels_validation, predictions))
print(dir(final_model))
if hasattr(final_model, 'feature_importances_'):
    print('Feature "importances":')
    print(final_model.feature_importances_)
if hasattr(final_model, 'coef_'):
    print('Feature correlation coefficients:')
    print(final_model.coef_)
