# Python Flask app from previous responsefrom flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Allows frontend communication

# Securely stored
openai.api_key = 'YOUR_OPENAI_API_KEY'

GPT_SYSTEM_PROMPT = """YOUR ENTIRE GPT CONFIGURATION PROMPT FROM EARLIER HERE"""

@app.route('/generate-analysis', methods=['POST'])
def generate_analysis():
    data = request.json

    brand = data.get('brand', 'None')
    indication = data['indication']
    geography = data.get('geography', 'U.S.')
    competitive_focus = data.get('competitive_focus', 'General')

    user_prompt = f"""
    Brand Name: {brand}
    Indication: {indication}
    Geography: {geography}
    Specific Competitive Focus: {competitive_focus}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": GPT_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.5,
        max_tokens=1200
    )

    analysis = response.choices[0].message.content
    return jsonify({"analysis": analysis})

if __name__ == '__main__':
    app.run(debug=True)
