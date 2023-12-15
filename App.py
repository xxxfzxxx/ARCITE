from flask import Flask, request, jsonify
from flask_cors import CORS
from GenerateCitation import GenerateCitation
app = Flask(__name__)
CORS(app)

@app.route('/generate_citation', methods=['POST'])
def generate_citation():
    try:
        data = request.json
        input_text = data['text']
        citation_style = data['style']

        # Initialize a list to collect messages
        messages = []

        # Call GenerateCitation and collect messages
        final_response, step_messages = GenerateCitation(input_text, citation_style)
        messages.extend(step_messages)

        return jsonify(citation=final_response, steps=messages)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
