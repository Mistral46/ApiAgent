from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de MongoDB
MONGO_URI = os.getenv('MONGO_URI')
if not MONGO_URI:
    raise ValueError("MONGO_URI no está configurada en el archivo .env")

client = MongoClient(MONGO_URI)

# Función para obtener una base de datos específica
def get_database(db_name):
    return client[db_name]

@app.route('/')
def home():
    return "API Flask con MongoDB Atlas"

# Endpoints para la base de datos iso27001_db
@app.route('/iso27001_db/chats', methods=['GET'])
def get_chats():
    db = get_database('iso27001_db')
    collection = db['chats']
    records = list(collection.find({}, {'_id': 0}))  # No incluir el campo _id
    return jsonify(records)

@app.route('/iso27001_db/fs.chunks', methods=['GET'])
def get_fs_chunks():
    db = get_database('iso27001_db')
    collection = db['fs.chunks']
    records = list(collection.find({}, {'_id': 0}))  # No incluir el campo _id
    return jsonify(records)

@app.route('/iso27001_db/fs.files', methods=['GET'])
def get_fs_files():
    db = get_database('iso27001_db')
    collection = db['fs.files']
    records = list(collection.find({}, {'_id': 0}))  # No incluir el campo _id
    return jsonify(records)

# Endpoints para la base de datos sgsi_db
@app.route('/sgsi_db/respuestas', methods=['GET'])
def get_respuestas():
    db = get_database('sgsi_db')
    collection = db['respuestas']
    records = list(collection.find({}, {'_id': 0}))  # No incluir el campo _id
    return jsonify(records)

if __name__ == '__main__':
    print(f"Mongo URI: {MONGO_URI}")  # Verifica que la URI se está cargando correctamente
    app.run(debug=True)
