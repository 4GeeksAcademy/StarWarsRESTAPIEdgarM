from flask import Flask, jsonify, request
from models import db, User, People, Planet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Or the URI of your choice
db.init_app(app)

@app.route('/people', methods=['GET'])
def get_people():
    all_people = People.query.all()
    return jsonify([p.name for p in all_people])

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get_or_404(people_id)
    return jsonify(person.name)

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
        'favorite_people': [p.name for p in user.favorites_people],
        'favorite_planets': [p.name for p in user.favorites_planets],
    })

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    user = User.query.get_or_404(request.args.get('user_id'))  # Assuming user_id is passed as a query param
    person = People.query.get_or_404(people_id)
    if person not in user.favorites_people:
        user.favorites_people.append(person)
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

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def remove_favorite_people(people_id):
    user = User.query.get_or_404(request.args.get('user_id'))  # Assuming user_id is passed as a query param
    person = People.query.get_or_404(people_id)
    if person in user.favorites_people:
        user.favorites_people.remove(person)
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
