import summariser
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for your function
@app.route('/get_summary', methods=['POST'])
def get_summary():
    try:
        # Get parameters from the request
        data = request.get_json()
        parameters = data

        # Call your function
        summary = summariser.create_summary(parameters)

        # Return the result as JSON
        return jsonify({'summary': summary})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

@app.route('/get_embedding', methods=['POST'])
def get_embedding():
    try:
        # Get parameters from the request
        data = request.get_json()
        parameters = data

        # Call your function
        embedding = summariser.create_embedding(parameters)

        # Return the result as JSON
        return jsonify({'embedding': embedding})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

@app.route('/get_embeddings', methods=['POST'])
def get_embeddings():
    try:
        # Get parameters from the request
        data = request.get_json()
        parameters = data

        # Call your function
        embeddings = summariser.bulk_create_embeddings(parameters)

        # Return the result as JSON
        return jsonify({'embeddings': embeddings})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=5000)
