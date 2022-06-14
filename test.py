import pandas as pd

df = pd.read_csv("adult.data.csv")

a = df.loc[(df["salary"] == ">50K") & (df["education"] == "Masters") | (df["education"] == "Doctorate") | (df["education"] == "Doctorate"), ["salary","education"]]


print(df.head)

print("------------------------------------")

print(a)
