from flask import Blueprint, request, jsonify
from utils import recognize_face

routes = Blueprint('routes', __name__)

@routes.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier fourni.'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Nom de fichier vide.'}), 400

    if not (file.filename.endswith('.jpg') or file.filename.endswith('.png')):
        return jsonify({'error': 'Format de fichier non valide. Veuillez télécharger une image JPG ou PNG.'}), 400

    # Appel à la fonction de reconnaissance faciale
    result = recognize_face(file)

    if result is None:
        return jsonify({'message': 'Personne non reconnue.'}), 404

    return jsonify({'message': 'Personne reconnue.', 'name': result}), 200