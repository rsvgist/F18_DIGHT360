"""In-class activities for 11-08."""

###############################################################################
print('#' * 79)
print('''Feature evaluation (machine-learning)

https://machinelearningmastery.com/feature-selection-in-python-with-scikit-learn/

Not all features are extracted equal, and including only the most useful
features in your model has many benefits:
    * Reduces Overfitting: Less redundant data means less opportunity to make
        decisions based on noise.
    * Improves Accuracy: Less misleading data means modeling accuracy improves.
    * Reduces Training Time: Less data means that algorithms train faster.
    * Reduces Feature Extraction Time: Less work to process data in the wild.
''')


from sklearn import datasets
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFE  # Recursive Feature Elimination
from sklearn.linear_model import LogisticRegression

# load the iris datasets
dataset = datasets.load_iris()
print('Feature names:')
print(dataset['feature_names'])
print('Class names:')
print(dataset['target_names'])

print('#' * 79)
print('Feature Importance')
print('All "tree" models in sklearn have a `feature_importances_` attribute.')

# fit an Extra Trees model to the data
ETCmodel = ExtraTreesClassifier()
ETCmodel.fit(dataset.data, dataset.target)

# display the relative importance of each attribute
print('Importances:', ETCmodel.feature_importances_)


input('Press [return] to continue.')
print()

print('''PRACTICE A

Train an ExtraTreesClassifier on your csv data and print the 'importances' of
the model. How well do they correspond to the output of the RFE?

(see ../assignments/importances.py)''')

input('Press [return] to continue.')
print()

print('Regression models have a coef_ attribute with correlation coefficients'
      ' of each feature with each label/class')
# create a base classifier used to evaluate a subset of features
LRmodel = LogisticRegression()

# train model based on all features
LRmodel_allfeats = LRmodel.fit(dataset.data, dataset.target)
print(LRmodel_allfeats.coef_)

input('Press [return] to continue.')
print()

print('''Recursive Feature Elimination (RFE)''')
print('''Given an external estimator that assigns weights to features (e.g.,
        the coefficients of a linear model), the goal of recursive feature
        elimination (RFE) is to select features by recursively considering
        smaller and smaller sets of features. First, the estimator is trained
        on the initial set of features and the importance of each feature is
        obtained either through a coef_ attribute or through a
        feature_importances_ attribute. Then, the least important features are
        pruned from current set of features. That procedure is recursively
        repeated on the pruned set until the desired number of features to
        select is eventually reached.''')

# create the RFE feature selection model and select 3 features
rfe = RFE(LRmodel, 3)
rfe = rfe.fit(dataset.data, dataset.target)

print('summarize the selection of the features')
print(rfe.support_)  # did the feature make the cut?
print(rfe.ranking_)  # the feature's rank (all "passing" features share 1st)

print('comparing predictions of full model and RFE model...')
toy_data = [(1,2,3,4), (1,1,1,1), (5,3,2,1), (5,5,5,5)]
print('Full:', LRmodel_allfeats.predict(toy_data))
print('RFE: ', rfe.predict(toy_data))

print('''PRACTICE B - this is basically your hw

Use RFE with the csv file you generated in assignment 8 to identify the 6 best
features in your best-performing model.

(see ../assignments/RFE.py)
''')
