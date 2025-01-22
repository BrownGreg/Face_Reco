from flask import Flask
from flask import request, jsonify, render_template
import cv2
import numpy as np
import os
from utils import recognize_face

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier téléchargé.'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Aucun fichier sélectionné.'}), 400

    if not (file.filename.endswith('.jpg') or file.filename.endswith('.png')):
        return jsonify({'error': 'Format de fichier non valide. Veuillez télécharger une image JPG ou PNG.'}), 400

    # Lire l'image
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Reconnaître le visage
    result = recognize_face(img)

    if result is None:
        return jsonify({'message': 'Personne non reconnue.'}), 404

    return jsonify({'message': f'Personne reconnue: {result}'}), 200

if __name__ == '__main__':
    app.run(debug=True)