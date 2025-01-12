from flask import jsonify
from svc.dao.ratings_dao import RatingsDAO
from svc.dao.fields_dao import FieldDAO
from svc.dao.user_dao import UserDAO


class RatingsService:
    def __init__(self):
        self.ratings_dao = RatingsDAO()
        self.field_dao = FieldDAO()
        self.user_dao = UserDAO()

    def create_rating(self, data):
        user_id = data.get('user_id')
        field_id = data.get('field_id')
        rating_value = data.get('rating')

        if not user_id or not field_id or rating_value is None:
            return {"error": "User ID, Field ID, and Rating Value are required."}, 400

        # Check if user exists
        user = self.user_dao.get_user_by_id(user_id)
        if not user:
            return {"error": "User does not exist."}, 404

        # Check if field exists
        field = self.field_dao.get_field_by_id(field_id)
        if not field:
            return {"error": "Field does not exist."}, 404

        response = self.ratings_dao.create_rating(user_id, field_id, rating_value)
        return response

