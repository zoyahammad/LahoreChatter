# LahoreChatter
A chatbot which gives the user information on Lahore (Pakistan) and its history.

## Overview 

This chatbot uses Natural Language Processing (NLP) fundamentals that I learnt via DataCamp courses.

- Text Pre - Processing with NLTK (Tokenization, Removing Noise/Stop Word, Stemming, Lemmatization)
- Created a Bag of Words
- Used the TF-IDF Approach to Estimate the Importance of Different Words
- Used Cosine Similarity to Find The Chatbot's Appropriate Response

## Tech

- Python3 (it would not work on previous versions)
- nltk for Natural Language Processing
- scikit-learn
- Flask for creating a web-app

## How to Use

1. Clone the repo
```
git clone https://github.com/zoyahammad/LahoreChatter.git
```

2. Install the dependencies

```
pip install -r requirements.txt
```

3. Run the Flask web app

```
python app.py
```

Head to http://127.0.0.1:5000/ in your web browser to test the application.

## How to Modify

To modify the natural language processing, you can modify the app.py file. To modify the user interface, you can modify the HTML/CSS within templates/index.html.

## Further Imporvements

- Need to find/build a better corpus so that the chatbot covers more subtopics and can answer more questions about Lahore.
- Deployment as a live application (which requires a paid domain)




