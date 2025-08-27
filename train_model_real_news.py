import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# === Load only extra_data.csv ===
csv_path = "datasets/extra_data.csv"

try:
    df = pd.read_csv(csv_path)
    print(f"✅ Loaded {len(df)} entries from {csv_path}")
except FileNotFoundError:
    print(f"❌ File not found: {csv_path}")
    exit()

# === Preprocess: ensure columns are clean
df = df[["text", "label"]].dropna()
df["label"] = df["label"].astype(int)

# === Split into X and y
X = df["text"]
y = df["label"]

# === TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_vec = vectorizer.fit_transform(X)

# === Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# === Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# === Evaluate
accuracy = model.score(X_test, y_test)
print(f"🎯 Model trained with accuracy: {accuracy * 100:.2f}%")

# === Save model and vectorizer
os.makedirs("models", exist_ok=True)
pickle.dump(model, open("models/model.pkl", "wb"))
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

print("✅ Model and vectorizer saved to models/")
