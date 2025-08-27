import pickle

model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

test_text = "Narendra Modi is alive"
X = vectorizer.transform([test_text])
prediction = model.predict(X)[0]
proba = model.predict_proba(X)[0]

print("🧠 Prediction:", "✅ Real" if prediction == 1 else "❌ Fake")
print(f"📊 Confidence → Fake: {proba[0]:.4f}, Real: {proba[1]:.4f}")

