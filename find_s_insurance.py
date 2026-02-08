import pandas as pd

df = pd.read_csv("insurance_finds_clean.csv")

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

def find_s(X, y):
    h = None
    for i in range(len(y)):
        if y[i] == "High":
            if h is None:
                h = X[i].copy()
            else:
                for j in range(len(h)):
                    if h[j] != X[i][j]:
                        h[j] = "?"
    return h

print("Final Hypothesis:", find_s(X, y))
