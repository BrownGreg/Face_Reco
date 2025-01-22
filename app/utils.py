from PIL import Image
import face_recognition
import numpy as np

def load_image(image_path):
    image = Image.open(image_path)
    return np.array(image)

def recognize_face(known_face_encodings, known_face_names, face_image):
    face_encodings = face_recognition.face_encodings(face_image)

    if not face_encodings:
        return None

    face_encoding = face_encodings[0]
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    if True in matches:
        first_match_index = matches.index(True)
        return known_face_names[first_match_index]
    
    return None

def validate_image_format(image):
    valid_formats = ['jpg', 'jpeg', 'png']
    return image.split('.')[-1].lower() in valid_formats