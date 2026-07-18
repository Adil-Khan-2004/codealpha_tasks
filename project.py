import pandas as pd

df = pd.read_csv("7817_1.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Info:")
print(df.info())
import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x="reviews.rating", data=df)

plt.title("Rating Distribution")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("7817_1.csv")

print(df.head())

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Info:")
print(df.info())

sns.countplot(x="reviews.rating", data=df)
plt.title("Rating Distribution")
plt.show()