from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as genai
import os

API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

app = Flask(__name__)
CORS(app)

app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

PRE_PROMPT = "Please review this essay with the understanding that it is an 8th-grade English Language Arts (ELA) project. The goal is to identify areas where the student can improve, without directly providing the answers. Focus on constructive feedback and suggestions for improvement, keeping your response concise. Limit the feedback to a few short sentences, and aim for under 300 words if possible. If you do not find any issues or areas for improvement, do not provide any feedback. The essay follows this colon:"


# if no input 
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "no input found"})



@app.route('/review', methods=['POST'])
def review_essay():
    essay_input = request.json.get('essay')
    essay = PRE_PROMPT + essay_input
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(essay)
    return jsonify({"result": response.text}),200


if __name__ == '__main__':
    app.run(debug=True)

