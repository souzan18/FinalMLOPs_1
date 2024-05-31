import re
import joblib
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

def preprocess_text(text):
    # Remove symbols and numbers using regex
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load the trained model
    clf = tf.keras.models.load_model('cnnv22.h5')
    tokenizer = joblib.load('tokenizer_1.pkl')
    le = joblib.load('le.pkl')
    
    if request.method == 'POST':
        # Get input data from the form
        review = request.form['review']
        
        # Preprocess input text
        review = preprocess_text(review)
        
        # Validate the review input
        if not review:
            return render_template('submit.html', error="Invalid characters detected. Please enter only letters and spaces.")
        
        # Preprocess Input
        sequences = tokenizer.texts_to_sequences([review])
        padded_sequences = pad_sequences(sequences, maxlen=100)
        
        # Make predictions using the loaded model
        my_prediction = clf.predict(padded_sequences)
        sentiment_predicted = le.classes_[np.argmax(my_prediction)]

        # Render the result template with the prediction and the entered review
        return render_template('submit.html', prediction=sentiment_predicted, review=review)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
