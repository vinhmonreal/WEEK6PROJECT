from flask import request, jsonify
from . import bp
from app.models import User

# Verify User
@bp.route('/verifyuser',methods=['POST','GET'])
def verify_user():
  content = request.get_json()
  print(content)
  username= content['username']
  password= content['password']
  user = User.query.filter_by(username=username).first()
  
  if user and user.check_password(password):
      print(password)
      return jsonify({'token': user.token})
  return jsonify({'error': 'user not found'}), 404

# Register User
@bp.route('/registeruser',methods=['POST', 'GET'])
def register_user():
  content = request.get_json()
  username= content['username']
  email= content['email']
  password= content['password']
  user = User.query.filter_by(username=username).first()
  if user:
      return jsonify({'error': 'username already exists'}), 409
  user = User.query.filter_by(email=email).first()
  if user:
      return jsonify({'error': 'email already exists'}), 409
  user = User(username=username, email=email)
  user.hash_password(password)
  user.add_token()
  user.commit()
  return jsonify({'token': user.token}), 201