from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, User, Character, Planet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' 
CORS(app)
db.init_app(app)

@app.route('/character', methods=['GET'])
def get_character():
    all_character = Character.query.all()
    return jsonify([p.name for p in all_character])


@app.route('/planets', methods=['GET'])
def get_planets():
    all_planets = Planet.query.all()
    return jsonify([p.name for p in all_planets])

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    return jsonify(planet.name)

@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    return jsonify([u.username for u in all_users])

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    user = User.query.get_or_404(request.args.get('user_id'))  # Assuming user_id is passed as a query param
    return jsonify({
        'favorite_character': [p.name for p in user.favorites_character],
        'favorite_planets': [p.name for p in user.favorites_planets],
    })

@app.route('/favorite/character/<int:character_id>', methods=['POST'])
def add_favorite_character(character_id):
    user = User.query.get_or_404(request.args.get('user_id'))  # Assuming user_id is passed as a query param
    person = Character.query.get_or_404(character_id)
    if person not in user.favorites_character:
        user.favorites_character.append(person)
        db.session.commit()
    return jsonify({'message': 'Favorite added.'})

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user = User.query.get_or_404(request.args.get('user_id'))  # Assuming user_id is passed as a query param
    planet = Planet.query.get_or_404(planet_id)
    if planet not in user.favorites_planets:
        user.favorites_planets.append (planet_id)
        db.session.commit()
    return jsonify({'message': 'Favorite added.'})

@app.route('/favorite/character/<int:character_id>', methods=['DELETE'])
def remove_favorite_character(character_id):
    user = User.query.get_or_404(request.args.get('user_id'))  # Assuming user_id is passed as a query param
    person = Character.query.get_or_404(character_id)
    if person in user.favorites_character:
        user.favorites_character.remove(person)
        db.session.commit()
    return jsonify({'message': 'Favorite removed.'})

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def remove_favorite_planet(planet_id):
    user = User.query.get_or_404(request.args.get('user_id'))  # Assuming user_id is passed as a query param
    planet = Planet.query.get_or_404(planet_id)
    if planet in user.favorites_planets:
        user.favorites_planets.remove(planet)
        db.session.commit()
    return jsonify({'message': 'Favorite removed.'})

if __name__ == '__main__':
    app.run(debug=True)
