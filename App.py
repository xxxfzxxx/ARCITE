from flask import Flask, request, jsonify
from GenerateCitation import GenerateCitation
app = Flask(__name__)

@app.route('/generate_citation', methods=['POST'])
def generate_citation():
    try:
        data = request.json
        input_text = data['text']
        citation_style = data['style']
        result = GenerateCitation(input_text, citation_style)
        return jsonify(citation=result)
    except Exception as e:  # Catch any exceptions that occur during the process
        return jsonify(error=str(e)), 500  # Return a server error

if __name__ == '__main__':
    app.run(debug=True)