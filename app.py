from flask import Flask, render_template, request, jsonify
import nltk
import string
import random
import warnings 
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load and preprocess the data
with open('Lahore.txt', 'r', encoding='utf8', errors='ignore') as f:
    raw = f.read().lower()

nltk.download('popular', quiet=True)

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hello mate!", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response = "I am sorry! I don't understand you"
    else:
        robo_response = sent_tokens[idx]
    sent_tokens.remove(user_response)
    return robo_response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_response = request.form["message"]
    user_response = user_response.lower()
    if user_response not in ['bye', 'thanks', 'thank you']:
        if greeting(user_response) is not None:
            return jsonify({"response": greeting(user_response)})
        else:
            return jsonify({"response": response(user_response)})
    elif user_response == 'bye':
        return jsonify({"response": "Bye! take care.."})
    else:
        return jsonify({"response": "You are welcome.."})

if __name__ == "__main__":
    app.run(debug=True)
