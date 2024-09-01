from flask import Flask, render_template, request, jsonify
from src.nlp import greeting, response

app = Flask(__name__)

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
