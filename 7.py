import numpy as np
import pandas as pd
import os
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination

filename = "7-dataset.csv"

if not os.path.exists(filename):
    np.random.seed(42)
    n = 500
    age, gender, exang = np.random.choice([0, 1, 2], n), np.random.choice([0, 1], n), np.random.choice([0, 1], n)
    cp = np.random.choice([0, 1, 2, 3], n)
    risk = np.clip(0.15 + 0.12*age + 0.10*exang + 0.08*(cp == 0) + 0.03*gender, 0.05, 0.90)
    heartdisease = np.random.binomial(1, risk)

    data = pd.DataFrame({
        "age": age, "gender": gender, "exang": exang, "cp": cp,
        "heartdisease": heartdisease,
        "restecg": np.where(heartdisease == 1, np.random.choice([1, 2], n), np.random.choice([0, 1], n)),
        "chol": np.where(heartdisease == 1, np.random.choice([1, 2], n), np.random.choice([0, 1], n))
    })
    data.to_csv(filename, index=False)
    print("Sample dataset created successfully.")

df = pd.read_csv(filename).replace("?", np.nan)
print("\nSample instances from the dataset:")
print(df.head())
print("\nAttributes and data types:")
print(df.dtypes)

cols = ["age", "gender", "exang", "cp", "heartdisease", "restecg", "chol"]
df = df[cols].dropna().astype(int)

model = DiscreteBayesianNetwork([
    ("age", "heartdisease"), ("gender", "heartdisease"),
    ("exang", "heartdisease"), ("cp", "heartdisease"),
    ("heartdisease", "restecg"), ("heartdisease", "chol")
])

print("\nLearning CPDs using Maximum Likelihood Estimation")
model.fit(df)

print("\nLearned Conditional Probability Distributions:")
for cpd in model.get_cpds():
    print(cpd)

infer = VariableElimination(model)

print("\nInferencing with Bayesian Network")
for evidence in [{"restecg": 1}, {"cp": 2}]:
    print(f"\nProbability of Heart Disease given {list(evidence)[0]} = {list(evidence.values())[0]}")
    print(infer.query(variables=["heartdisease"], evidence=evidence, show_progress=False))