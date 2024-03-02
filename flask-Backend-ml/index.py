from flask import Flask, request, jsonify
from flask_cors import CORS 
import pickle
from sklearn.ensemble import RandomForestClassifier
from google.generativeai import configure, GenerativeModel

app = Flask(__name__)
CORS(app)

# Load the trained model
with open('mlmodel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Configure Google Generative AI
configure(api_key='AIzaSyCvuuQm4eJ4GIAIHHxaWl-FozyfYDqEnBA')
generative_model = GenerativeModel('gemini-pro')

# Endpoint for recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get input data from the POST request
        input_data = request.json

        # Ensure the input data has the expected number of features
        if len(input_data) != 7:
            return jsonify({'error': 'Invalid input. Please provide 7 values.'}), 400

        # Convert input data to a NumPy array
        input_array = [float(value) for value in input_data.values()]

        # Make prediction using the loaded model
        prediction = model.predict([input_array])

        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# New endpoint for Plantinfo with modified prompt
@app.route('/Plantinfo', methods=['POST'])
def plant_info():
    try:
        # Get input data from the POST request
        plantname = request.json.get('plantname', 'Sunflower')  # Default to 'Sunflower' if not provided
        language= request.json.get('language','english')
        # plantname="rice"
        # Modified prompt for generative model
        generative_prompt = f"Provide advice on grooming a {plantname} plant and recommend fertilizers. (write in hindi {language} , do not want any ** /n in my text give only plain text give it in boolet points)"

        # Use the generative model to generate content
        generative_response = generative_model.generate_content(generative_prompt)
        generated_text = generative_response.text

        return jsonify({'output': generated_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
