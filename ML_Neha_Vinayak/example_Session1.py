from sklearn.tree import DecisionTreeClassifier
# import the necessary libraries

# from sklearn.externals.six import StringIO
from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
import os
# Import pandas library
from sklearn.model_selection import train_test_split
import pandas as pd

dataset = pd.read_csv('zoo.csv')

# check the size of the dataset
dataset.shape
dataset.head()
# The first column which are names of the animals is not a fature that can used.
# Extract the column and save for later.

animal_names = dataset['animal_name'].tolist()

# Drop the first column which are the animal names

dataset=dataset.drop('animal_name',axis=1)

X = dataset.loc[:, dataset.columns != 'class_type']

# copy the last column only
Y = dataset['class_type']

(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, stratify=Y, test_size= 0.3)

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
Y_predict = model.predict(X_test)

# extract the feature names
feature_names = list(dataset.columns.values)

# drop the last column name
feature_names = feature_names[:-1]

# extact the class names
class_int = dataset['class_type'].unique().tolist()

class_names = ['Mammal', 'Fish', 'Bird', 'Invertebrate', 'Bug', 'Amphibian', 'Reptile']

# map the class names to the class number as specified in the dataset

dictionary = dict(zip(class_names, class_int))

os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz-14.0.2-win64\\lib\\graphviz' # Windows OS

# may need to install
# pip install pydotplus

dot_data = StringIO()

export_graphviz(model, out_file=dot_data,
                filled=True, rounded=True,
                feature_names = feature_names,
                class_names = class_names,
                proportion = False, precision = 2,
                special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

Image(graph.create_png())