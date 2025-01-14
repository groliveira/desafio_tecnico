from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/starwars"
mongo = PyMongo(app)

# Helper functions
def format_planet(planet):
    return {
        "id": str(planet["_id"]),
        "nome": planet["nome"],
        "clima": planet["clima"],
        "diametro": planet["diametro"],
        "populacao": planet["populacao"],
        "filmes": planet["filmes"],
        "data_criacao": planet["data_criacao"],
        "data_alteracao": planet["data_alteracao"],
    }

def format_film(film):
    return {
        "id": str(film["_id"]),
        "titulo": film["titulo"],
        "data_lancamento": film["data_lancamento"],
        "diretor": film["diretor"],
        "planetas": film["planetas"],
        "data_criacao": film["data_criacao"],
        "data_alteracao": film["data_alteracao"],
    }

# Rotas para Planetas
@app.route('/planetas', methods=['POST'])
def create_planet():
    data = request.get_json()
    planet = {
        "nome": data["nome"],
        "clima": data["clima"],
        "diametro": data["diametro"],
        "populacao": data["populacao"],
        "filmes": data.get("filmes", []),
        "data_criacao": datetime.utcnow(),
        "data_alteracao": datetime.utcnow()
    }
    result = mongo.db.planetas.insert_one(planet)
    return jsonify({"id": str(result.inserted_id)}), 201

@app.route('/planetas', methods=['GET'])
def get_planets():
    planets = mongo.db.planetas.find()
    return jsonify([format_planet(planet) for planet in planets]), 200

@app.route('/planetas/<planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = mongo.db.planetas.find_one({"_id": ObjectId(planet_id)})
    if planet:
        return jsonify(format_planet(planet)), 200
    return jsonify({"error": "Planeta não encontrado"}), 404

@app.route('/planetas/<planet_id>', methods=['PUT'])
def update_planet(planet_id):
    data = request.get_json()
    update_data = {
        "nome": data["nome"],
        "clima": data["clima"],
        "diametro": data["diametro"],
        "populacao": data["populacao"],
        "filmes": data.get("filmes", []),
        "data_alteracao": datetime.utcnow()
    }
    result = mongo.db.planetas.update_one({"_id": ObjectId(planet_id)}, {"$set": update_data})
    if result.matched_count:
        return jsonify({"message": "Planeta atualizado com sucesso"}), 200
    return jsonify({"error": "Planeta não encontrado"}), 404

@app.route('/planetas/<planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    result = mongo.db.planetas.delete_one({"_id": ObjectId(planet_id)})
    if result.deleted_count:
        return jsonify({"message": "Planeta deletado com sucesso"}), 200
    return jsonify({"error": "Planeta não encontrado"}), 404

# Rotas para Filmes
@app.route('/filmes', methods=['POST'])
def create_film():
    data = request.get_json()
    film = {
        "titulo": data["titulo"],
        "data_lancamento": data["data_lancamento"],
        "diretor": data["diretor"],
        "planetas": data.get("planetas", []),
        "data_criacao": datetime.utcnow(),
        "data_alteracao": datetime.utcnow()
    }
    result = mongo.db.filmes.insert_one(film)
    return jsonify({"id": str(result.inserted_id)}), 201

@app.route('/filmes', methods=['GET'])
def get_films():
    films = mongo.db.filmes.find()
    return jsonify([format_film(film) for film in films]), 200

@app.route('/filmes/<film_id>', methods=['GET'])
def get_film(film_id):
    film = mongo.db.filmes.find_one({"_id": ObjectId(film_id)})
    if film:
        return jsonify(format_film(film)), 200
    return jsonify({"error": "Filme não encontrado"}), 404

@app.route('/filmes/<film_id>', methods=['PUT'])
def update_film(film_id):
    data = request.get_json()
    update_data = {
        "titulo": data["titulo"],
        "data_lancamento": data["data_lancamento"],
        "diretor": data["diretor"],
        "planetas": data.get("planetas", []),
        "data_alteracao": datetime.utcnow()
    }
    result = mongo.db.filmes.update_one({"_id": ObjectId(film_id)}, {"$set": update_data})
    if result.matched_count:
        return jsonify({"message": "Filme atualizado com sucesso"}), 200
    return jsonify({"error": "Filme não encontrado"}), 404

@app.route('/filmes/<film_id>', methods=['DELETE'])
def delete_film(film_id):
    result = mongo.db.filmes.delete_one({"_id": ObjectId(film_id)})
    if result.deleted_count:
        return jsonify({"message": "Filme deletado com sucesso"}), 200
    return jsonify({"error": "Filme não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
