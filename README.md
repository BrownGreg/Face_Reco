# Facial Recognition API

Ce projet est une API de reconnaissance faciale développée en Python avec Flask. Il permet de télécharger des images et de reconnaître des visages à partir de celles-ci. L'application inclut également une interface utilisateur simple en HTML.

## Structure du projet

```
facial-recognition-api
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── templates
│   └── index.html
├── static
│   └── styles.css
├── Dockerfile
├── requirements.txt
└── README.md
```

## Installation

1. Clonez le dépôt :
   ```
   git clone <URL_DU_DEPOT>
   cd facial-recognition-api
   ```

2. Créez un environnement virtuel et activez-le :
   ```
   python -m venv venv
   source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
   ```

3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

1. Démarrez l'application :
   ```
   python app/main.py
   ```

2. Accédez à l'interface utilisateur via votre navigateur à l'adresse `http://127.0.0.1:5000`.

3. Téléchargez une image au format JPG ou PNG pour reconnaître un visage.

## Fonctionnalités

- Téléchargement d'images pour la reconnaissance faciale.
- Gestion des utilisateurs et des visages dans une base de données.
- Interface utilisateur simple et intuitive.

## Docker

Pour exécuter l'application dans un conteneur Docker, utilisez les commandes suivantes :

1. Construisez l'image Docker :
   ```
   docker build -t facial-recognition-api .
   ```

2. Exécutez le conteneur :
   ```
   docker run -p 5000:5000 facial-recognition-api
   ```

## Auteurs

- Grégory HERY
- Othmane SENNIA
- Pierre Marcel MISSIHOUN

## License

Ce projet est sous licence MIT.
