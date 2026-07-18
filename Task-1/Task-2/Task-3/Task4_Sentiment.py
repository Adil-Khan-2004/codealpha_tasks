import pandas as pd
from textblob import TextBlob

# Load Dataset
df = pd.read_csv("Amazon product review.csv")

# Function for Sentiment Analysis
def get_sentiment(text):
    analysis = TextBlob(str(text))

    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply Sentiment Analysis
df["Sentiment"] = df["reviews.text"].apply(get_sentiment)

# Show Result
print(df[["reviews.text", "Sentiment"]].head(10))

# Count Sentiments
print("\nSentiment Count:")
print(df["Sentiment"].value_counts())
import matplotlib.pyplot as plt

df["Sentiment"].value_counts().plot(
    kind="bar",
    title="Sentiment Analysis"
)

plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()