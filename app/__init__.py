from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configurations de base
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite de 16 Mo pour les fichiers

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app