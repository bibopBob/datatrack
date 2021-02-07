import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


fpath = 'diamonds.csv'
fhand = pd.read_csv(fpath)
# fhand.tail()

# target var
y_var = fhand['price']

# pred var
laben = LabelEncoder()
X_lab = pd.DataFrame(laben.fit_transform(fhand['color']))
# fhand['color'].tail()

X_lab['color'] = X_lab.values
X_lab = X_lab.drop(X_lab.columns[0], axis=1)
# X_lab.tail()

new_data = pd.DataFrame()
new_data['color'] = X_lab['color'].values
new_data['price'] = y_var.values
new_data['carat'] = fhand['carat'].values

# sns.lmplot(x='color',y='price',hue='carat',data=new_data)
sns.lmplot(x='carat',y='price',hue='color',data=new_data)
