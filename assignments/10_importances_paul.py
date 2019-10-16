import pandas
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFE  # Recursive Feature Elimination
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


with open('mc_feat_names_new.txt') as name_file:
    names = name_file.read().strip().split('\t')
len_names = len(names)
with open('mc_features_new.csv') as mc_file:
    dataset = pandas.read_csv(mc_file, names=names,  # pandas DataFrame object
                              keep_default_na=False, na_values=['_'])  # avoid 'NA' category being interpreted as missing data  # noqa
print(list(dataset))  # easy way to get feature (column) names

array = dataset.values  # numpy array
feats = array[:, 0:len_names - 1]  # to understand comma, see url in next line:
# https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html#advanced-indexing
labels = array[:, -1]


# fit an Extra Trees model to *your* data
ETCmodel = ExtraTreesClassifier()
ETCmodel.fit(feats, labels)   # rather than dataset.data, dataset.target

# display the relative importance of each attribute
print('Importances:', ETCmodel.feature_importances_)

# create a base classifier used to evaluate a subset of features
# LRmodel = LogisticRegression()

LDAmodel = LinearDiscriminantAnalysis()

# train model based on all features
# LRmodel_allfeats = LRmodel.fit(feats, labels)
# print(LRmodel_allfeats.coef_)

LDAmodel_allfeats = LDAmodel.fit(feats, labels)
print(LDAmodel_allfeats.coef_)


# create the RFE feature selection model and select # of features
# rfe = RFE(LRmodel, 3)
rfe = RFE(LDAmodel, 6)
rfe = rfe.fit(feats, labels)

print('summarize the selection of the features')
print(rfe.support_)  # did the feature make the cut?
print(rfe.ranking_)  # the feature's rank (all "passing" features share 1st)

# print('comparing predictions of full model and RFE model...done?')
toy_data = [(1, 2, 3, 4), (1, 1, 1, 1), (5, 3, 2, 1), (5, 5, 5, 5)]
# print('Full:', LRmodel_allfeats.predict(toy_data))
# add LDA model?
# print('RFE: ', rfe.predict(toy_data))
