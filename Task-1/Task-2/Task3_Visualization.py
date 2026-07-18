import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Amazon product review.csv")

# Show first 5 rows
print(df.head())

# Graph 1 - Rating Distribution
sns.countplot(x="reviews.rating", data=df)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Graph 2 - Top 10 Brands
plt.figure(figsize=(10,5))
df["brand"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Brands")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Graph 3 - Rating Percentage (Pie Chart)
df["reviews.rating"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Rating Percentage")
plt.ylabel("")
plt.show()