from svc.dao.fields_dao import FieldDAO
from models.fields import Field
from svc.dao.user_dao import UserDAO
from svc.dao.favorites_dao import FavoritesDAO
from flask import jsonify
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import check_password_hash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class UserService():
    def __init__(self):
        self.user_dao = UserDAO()
        self.favorites_dao = FavoritesDAO()
        self.fields_dao = FieldDAO()
        self.fields = Field()

    def get_user_by_name(self,user_name):
        response = self.user_dao.get_user_by_name(user_name)
        return response
    
    def update_preference(self, user_name, preference):
        # Check if the user exists
        user = self.user_dao.get_user_by_name(user_name)
        if not user:
            return {'message': 'User not found'}, 404

        # Update the preference
        message = self.user_dao.update_preference(user_name, preference)
        return {'message': message}, 200
    
    def get_user_by_id(self, user_id):
        return self.user_dao.get_user_by_id(user_id)


    # Verify user credentials during login
    def user_verification(self, username, password):
        user = self.user_dao.get_user_by_username(username)
        if user and check_password_hash(user.password, password):
           return jsonify({
                'message': 'User Verified',
                'userid': user.uid,
                'user_type': user.user_type,
                'preferences': user.preference
            }), 200

        return jsonify({'error': 'Invalid username or password'}), 401  # HTTP 401 Unauthorized

        # You can add methods to set and verify the password
    def set_password(self, password):
        self.password_hash = Bcrypt().generate_password_hash(password).decode('utf-8')

    def create_user(self, data):
        if not data['username']:
            return jsonify({'error': 'Username is required'}), 400

        if 'password' not in data:  
            return jsonify({'error': 'Password are required'}), 400
        
        if not data['phonenum']:
            return jsonify({'error': 'Phone number is required'}), 400

        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        try:
            data['password'] = hashed_password


            user = self.user_dao.create_user(data=data)
            return jsonify({
                'message': 'User created successfully',
                'username': user.username,
                'phonenum': user.phonenum,
            }), 201

        except IntegrityError as e:
            # Log the exception message for debugging
            print("IntegrityError:", str(e))

            # Check if the exception is due to a unique constraint violation
            if "UniqueViolation" in str(e):
                if "users_username_key" in str(e):
                    return jsonify({'error': 'User with this username already exists'}), 409  # HTTP 409 Conflict
                elif "users_phonenum_key" in str(e):
                    return jsonify({'error': 'User with this phone number already exists'}), 409  # HTTP 409 Conflict

    # If we reach this point, return a generic error response
        return jsonify({'error': 'An unexpected error occurred'}), 500  # HTTP 500 Internal Server Error

    def fetcher_db_user_info(self, user_info):
        user_data_list = []
    
        try:
            if user_info:
                for user in user_info:
                    user_data = {
                        "username": user.username,
                        "password": user.password,
                        "phonenum": user.phonenum
                    }
                    user_data_list.append(user_data)
            else:
                # Return a specific response when user_info is missing
                return [{"message": "User info is missing"}]

        except Exception as e:
            # Handle any other exceptions that may occur
            return [{"error": str(e)}]

        return user_data_list
    
    def add_favorite(self, data):
        user_id = data['user_id']
        field_id = data['field_id']
        if not user_id or not field_id:
            return jsonify({'error': 'User ID and Field ID are required'}), 400

        # Check if the user exists
        user = self.user_dao.get_user_by_id(user_id)
        if not user:
            return jsonify({'error': 'User does not exist'}), 404

        # Check if the field exists
        field = self.fields_dao.get_field_by_id(field_id)
        if not field:
            return jsonify({'error': 'Field does not exist'}), 404

        # Check if the field is already in the user's favorites
        existing_favorite = self.favorites_dao.get_favorite_by_user_and_field(user_id, field_id)
        if existing_favorite:
            return jsonify({'error': 'This field is already in your favorites'}), 400

        # Create a new favorite record
        response = self.favorites_dao.create_favorite(user_id, field_id)
        return response
    
    # Method to remove a field from the user's favorites
    def remove_favorite(self, user_id, field_id):
        if not user_id or not field_id:
            return jsonify({'error': 'User ID and Field ID are required'}), 400

        # Check if the field is in the user's favorites
        existing_favorite = self.favorites_dao.get_favorite_by_user_and_field(user_id, field_id)
        if not existing_favorite:
            return jsonify({'error': 'This field is not in your favorites'}), 400

        # Delete the favorite record
        response = self.favorites_dao.delete_favorite(existing_favorite)
        return response
    
    def get_user_favorite_fields(self,user_id):
        if not user_id:
            return {"error": "user_id is required."}, 400
        
        favorite_fields = self.favorites_dao.get_favorite_fields_by_user(user_id)

        if not favorite_fields:
            return {"message": "No favorite fields found for this user."}, 404

        favorite_fields_details = []
        for favorite in favorite_fields:
            field_id = favorite.field_id
            field = self.fields_dao.get_single_field_by_id(field_id)
            print(f"field_id: {field_id}, field: {field}")
            if field:
                field_info = {
                    "uid": field.uid,
                    "name": field.name,
                    "location": field.location,
                    "latitude": field.latitude,
                    "longitude": field.longitude,
                    "sport_type": field.sport_type,
                    "imageURL": field.imageURL,
                    "manager_id" : field.manager_id,
                    "utilities" : field.utilities
                }
                favorite_fields_details.append(field_info)

        return favorite_fields_details, 200

