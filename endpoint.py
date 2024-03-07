import traceback

import summariser
import question_answering
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

@app.route('/get_skills_required', methods=['POST'])
def get_skills_required():
    try:
        # Get parameters from the request
        data = request.get_json()
        parameters = data

        # Call your function
        answer = question_answering.answer_question_from_context(parameters, "What skills are required?")

        # Return the result as JSON
        return jsonify({'answer': answer})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

@app.route('/get_job_details', methods=['POST'])
def get_job_details():
    try:
        # Get parameters from the request
        data = request.get_json()
        parameters = data

        # Call your function
        answer = question_answering.answer_question_from_context(parameters, "What are the job details?")

        # Return the result as JSON
        return jsonify({'answer': answer})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

@app.route('/get_candidate_skills', methods=['POST'])
def get_candidate_skills():
    try:
        # Get parameters from the request
        data = request.get_json()
        parameters = data

        # Call your function
        answer = question_answering.answer_question_from_context(parameters, "What skills do they have?")

        # Return the result as JSON
        return jsonify({'answer': answer})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

@app.route('/get_suggested_job', methods=['POST'])
def get_suggested_job():
    try:
        # Get parameters from the request
        data = request.get_json()
        parameters = data

        # Call your function
        answer = question_answering.answer_question_from_context(parameters, "What should they work as?")

        # Return the result as JSON
        return jsonify({'answer': answer})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    print("begin answering")
    question_answering.answer_question_from_context("Test job", "What is the job?")
    print("Answered")
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        pass
    except BaseException as e:
        print(traceback.format_exc())
        pass

