import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

df = pd.read_json('sim_data.json')
df.describe()

drop_cols = ['prior_exp','usage_hours','utility']
df = df.drop(columns=drop_cols)
df.info()

#splitting / training
y = df['conversion']
x = df.drop(columns='conversion')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=9)

# into 3 seperate data frames
x_train_10k = x_train[0:10000]
x_train_25k = x_train[0:25000]
x_train_50k = x_train[0:50000]

y_train_10k = y_train[0:10000]
y_train_25k = y_train[0:25000]
y_train_50k = y_train[0:50000]

# predictive power benchmark
def class_metrics(prediction):
    a = print("Accuracy:",metrics.accuracy_score(y_test, prediction))
    p = print("Precision:",metrics.precision_score(y_test, prediction))
    r = print("Recall:",metrics.recall_score(y_test, prediction))
    f = print("F-1 Score:",metrics.f1_score(y_test, prediction))
    return a, p, r, f;

#running first on x_train_10k
gn1 = GaussianNB()
gnm1 = gn1.fit(x_train_10k, y_train_10k)
gnr1 = gnm1.predict(x_test)
print(class_metrics(gnr1))
print(gnm1.get_params())

#running second time on x_train_20k
gn2 = GaussianNB()
gnm2 = gn2.fit(x_train_25k, y_train_25k)
gnr2 = gnm2.predict(x_test)
print(class_metrics(gnr2))
print(gnm2.get_params())

#running second time on x_train_20k
gn3 = GaussianNB()
gnm3 = gn3.fit(x_train_50k, y_train_50k)
gnr3 = gnm3.predict(x_test)
print(class_metrics(gnr3))
print(gnm3.get_params())
