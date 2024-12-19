from flask import Flask, jsonify, request
import google.generativeai as genai
import os

API_KEY = os.getenv('API_KEY')

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

PRE_PROMPT = "Please review this essay with the context that it is a 8th grade ELA project. Review this prompt while keeping in mind the goal is the find the things the student can improve on and NOT to give the student the answers directly. Give all the responses in a couple bullet points of any issues in the essay and how to improve them. if you do not find issues then do not write any bullet points. The essay is after this colon: "


# if no input 
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "no input found"})



@app.route('/review', methods=['POST'])
def review_essay():
    essay = PRE_PROMPT
    essay.append(request.json.get('essay'))
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(essay)
    return jsonify({"result": response})


if __name__ == '__main__':
    app.run(debug=True)

