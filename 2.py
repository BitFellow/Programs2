import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

print("First 5 rows of Iris Dataset:")
print(df.head())

X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)

print("CLASSIFICATION RULES")
print(export_text(dt, feature_names=list(X.columns)))

print("FOIL LEARNED RULES")

positive = df[df['target'] == 0]
negative = df[df['target'] != 0]

for feature in iris.feature_names:
    p = positive[feature].mean()
    n = negative[feature].mean()

    if p < n:
        print(f"IF {feature} < {round((p+n)/2, 2)} THEN Class = Setosa")