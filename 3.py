from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

bag = BaggingClassifier(random_state=42)
bag.fit(X_train, y_train)
bag_pred = bag.predict(X_test)

boost = AdaBoostClassifier(random_state=42)
boost.fit(X_train, y_train)
boost_pred = boost.predict(X_test)

print("Actual Labels          :", y_test[:10])
print("Bagging Predictions    :", bag_pred[:10])
print("Boosting Predictions   :", boost_pred[:10])

print("\nBagging Accuracy :", accuracy_score(y_test, bag_pred))
print("Boosting Accuracy:", accuracy_score(y_test, boost_pred))