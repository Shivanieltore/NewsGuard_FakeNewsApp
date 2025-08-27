from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open('models/model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['news']
    vec = vectorizer.transform([input_text])
    prediction = model.predict(vec)[0]
    label = "✅ Real News" if prediction == 1 else "❌ Fake News"
    return render_template('index.html', result=label, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)

