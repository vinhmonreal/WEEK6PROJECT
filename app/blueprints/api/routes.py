from . import bp
from app.blueprints.api.helpers import token_required
from app.models import User, MarvelCharacter

from flask import jsonify, request, url_for, abort


@bp.get('/characters')
@token_required
def characters():
    characters = MarvelCharacter.query.all()
    return jsonify([character.to_dict() for character in characters])        

@bp.get('/user/<username>')
@token_required
def user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'user not found'}), 404
    return jsonify(user.to_dict())

@bp.route('/user/addcharacter', methods=['POST', 'GET'])
@token_required
def addcharacter():
    content = request.get_json()
    username= content['username']
    password= content['password']
    name = content['name']
    description = content['description']
    comics_appeared_in = content['comics_appeared_in']
    super_power = content['super_power']
    
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        owner_id = user.token
        character = MarvelCharacter(name=name, description=description, comics_appeared_in=comics_appeared_in, super_power=super_power, owner_id=owner_id)
        character.commit()
        return jsonify(character.to_dict()), 201
    else:
        return jsonify({'error': 'user not found or invalid password'}), 404