from flask import Flask, request, jsonify
from réponses import répondre

app = Flask(__name__)

@app.route('/question', methods=['GET'])
def question():
    q = request.args.get('q', '')
    réponse = répondre(q)
    return jsonify({
        "réponse": réponse,
        "assistant": "YvanGPT 💬"
    })

if __name__ == '__main__':
    app.run(debug=True)
