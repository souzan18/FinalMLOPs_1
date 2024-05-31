# Amazon Review Sentiment Analysis Application

## Overview

This application performs sentiment analysis on product reviews. Users can input their reviews, and the application will analyze the text to determine if the sentiment is positive, negative, or neutral. The app is built using Flask for the web interface and a pre-trained model for sentiment analysis.

## Features

- Submit a product review for sentiment analysis.
- Receive feedback on whether the review sentiment is positive, negative, or neutral.
- Input validation to ensure only valid reviews are analyzed.

## Setup and Installation

### Local Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/souzan18/FinalMLOPs_1.git
    cd FinalMLOPs_1
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Download NLTK data** (if not already installed):
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

5. **Ensure you have the required model and tokenizer files**:
    - `cnnv2.pkl`
    - `tokenizer_1.pkl`
    - `le.pkl`
  
    These files should be placed in the root directory of the project.

### Running the Application Locally

1. **Start the Flask application**:
    ```sh
    python app.py
    ```

2. **Open your browser and navigate to**:
    ```
    http://localhost:5000
    ```

### Docker Setup

1. **Build the Docker image**:
    ```sh
    docker build -t my-flask-app .
    ```

2. **Run the Docker container**:
    ```sh
    docker run -p 5000:5000 sentimentanalysisapp
    ```

3. **Open your browser and navigate to**:
    ```
    http://localhost:5000
    ```

## Usage

### Home Page

The home page provides instructions on how to use the application. It includes guidelines for writing a review and examples of valid and invalid reviews.

### Submitting a Review

1. Navigate to the submission page by clicking the "Submit Your Review" button on the home page.
2. Enter your review in the text box. Ensure that your review does not contain any numbers or special characters.
3. Click "Submit" to analyze the sentiment of your review.

### Example Reviews

**Valid Reviews**:
- "The phone never skips a beat. File transfers are speedy with no corruption issues."
- "Purchased this device and it worked as advertised. Never had much phone memory before but this is a no-brainer."
- "Works as expected. Higher capacity and seems well-made. Paint looks clean."

**Invalid Reviews**:
- "Great product! 100% satisfied!! #awesome"
- "The price was $299.99 but totally worth it!!"
- "Loved it!!! <3 <3 <3"




## Directory Structure
├── app.py
├── templates
│ ├── home.html
│ ├── submit.html
├── static
│ └── (if you have any static files like CSS or JS)
├── cnnv2.pkl
├── tokenizer_1.pkl
├── le.pkl
├── requirements.txt
└── README.md

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.




