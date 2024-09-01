import nltk
import string
import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Download popular NLTK data sets and models (e.g., tokenizers, lemmatizers)
nltk.download('popular', quiet=True)

# Load and preprocess the data
with open('./corpus/Lahore.txt', 'r', encoding='utf8', errors='ignore') as f:
    raw = f.read().lower()

# Tokenize the text into sentences and words
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

# Initialize the WordNet Lemmatizer for reducing words to their base form
lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    """
    Lemmatize a list of tokens (words) using the WordNet lemmatizer. 
    Lemmatization is a natural language processing (NLP) technique that 
    reduces words to their base or dictionary form, known as the lemma
    
    Examples: 
    "am," "are," and "is" are all lemmatized to "be."
    "flies" (noun) and "flew" (verb) are both reduced to "fly."
    """
    return [lemmer.lemmatize(token) for token in tokens]


# Create a translation table to remove punctuation
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    """
    Normalize text by converting to lowercase, removing punctuation, and lemmatizing.
    """
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Predefined greetings and responses for user interaction
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "heya", "Hello", "hola")
GREETING_RESPONSES = ["hi", "hello mate!", "hey", "hi there", "hello", "I am glad! You are talking to me", "Heya", "Hi!", "Hello!"]


def greeting(sentence):
    """
    Check if the user's input sentence contains a greeting and respond accordingly.
    """
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    """
    Generate a response to the user's input by finding the most similar sentence from the corpus.
    """
    robo_response = ''

    # Append the user's response to the list of sentence tokens
    sent_tokens.append(user_response)

    # Vectorize the sentences using TF-IDF and normalize using LemNormalize
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)

    # Compute cosine similarity between the user's response and all other sentences
    vals = cosine_similarity(tfidf[-1], tfidf)

    # Get the index of the most similar sentence (excluding the user's response itself)
    idx = vals.argsort()[0][-2]

    # Flatten and sort the cosine similarity values
    flat = vals.flatten()
    flat.sort()

    # Get the value of the second highest similarity score
    req_tfidf = flat[-2]

    # Determine the response based on the similarity score
    if req_tfidf == 0:
        robo_response = "I am sorry! I don't understand you"
    else:
        robo_response = sent_tokens[idx]
    
    # Remove the user's response from the list of sentence tokens
    sent_tokens.remove(user_response)
    return robo_response
