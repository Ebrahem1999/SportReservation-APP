import json
import uuid
from flask import request, Blueprint, jsonify,send_file
from svc.services.user_service import UserService
from svc.services.fields_service import FieldService
from svc.services.reservation_service import ReservationService,generate_android_deep_link,generate_ios_deep_link
from svc.services.sms_auth_service import generate_auth_code, send_sms,generate_phone_num,sms_queue,check_code,auth_code_queue
from svc.services.payments_service import PaymentsService
from svc.services.ratings_service import RatingsService
import os
from google.auth.transport import requests
from google.oauth2 import id_token
#API EXAMPLES ARE INSIDE THE FILE API_EXAMPLES, PLEASE IF YOU ADD ANY NEW ENDPOINT TO ADD IT TO THIS FILE.

api_bp = Blueprint('api', __name__)

def is_valid_uuid(uuid_to_test, version=4):
    try:
        uuid_obj = uuid.UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test

@api_bp.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    user_service = UserService()
    response = user_service.create_user(data=data)
    return response

@api_bp.route('/update_preference', methods=['PUT'])
def update_preference():
    user_name = request.json.get('username')
    preference = request.json.get('preference')
    
    if not user_name or not preference:
        return jsonify({'error': 'User Name and preference are required'}), 400
    user_service = UserService()
    response, status_code = user_service.update_preference(user_name, preference)
    return response, status_code

@api_bp.route('/user_verfication', methods=['POST'])
def user_verification():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user_service = UserService()
    response = user_service.user_verification(username=username, password=password)
    return response

@api_bp.route('/get_user_by_name', methods=['GET'])
def get_user_by_name():
    data = request.json
    data = data.get('user_info')
    user_service = UserService()
    users = user_service.get_user_by_name(user_name=data)
    ##for users in user_service.fetcher_db(user_info=users):
    return jsonify(user_service.fetcher_db_user_info(user_info=users))

@api_bp.route('/create_field', methods=['POST'])
def create_field():
    data = request.json
    data['utilities'] = json.dumps(data['utilities']) 
    manager_id = data['manager_id']
    if not is_valid_uuid(manager_id):
        return jsonify({'error': 'Manager ID must be a valid UUID'}), 400
    field_service = FieldService()
    response = field_service.create_field(data=data)
    return response

@api_bp.route('/update_conf_interval', methods=['PUT'])
def update_conf_interval():
    field_id = request.json.get('field_id')
    conf_interval = request.json.get('conf_interval')
    if not field_id or not conf_interval:
        return jsonify({'error': 'Field ID and conf_interval are required'}), 400
    if not is_valid_uuid(field_id):
        return jsonify({'error': 'Field ID must be a valid UUID'}), 400
    
    field_service = FieldService()
    field, status_code = field_service.update_conf_interval(field_id, conf_interval)
    return jsonify(field), status_code

@api_bp.route('/update_field_details', methods=['PUT'])
def update_field_details():
    field_id = request.json.get('field_id')
    name = request.json.get('name')
    utilities = json.dumps(request.json.get('utilities'))  # Ensure utilities is a JSON string
    
    if not field_id:
        return jsonify({'error': 'Field ID is required'}), 400
    
    if not is_valid_uuid(field_id):
        return jsonify({'error': 'Field ID must be a valid UUID'}), 400
    
    field_service = FieldService()
    field, status_code = field_service.update_field_details(field_id, name, utilities)
    return jsonify(field), status_code

@api_bp.route('/delete_field', methods=['DELETE'])
def delete_field():
    field_id = request.json.get('field_id')
    manager_id = request.json.get('manager_id')
    
    if not field_id or not manager_id:
        return jsonify({'error': 'Field ID and Manager ID are required'}), 400

    if not is_valid_uuid(field_id) or not is_valid_uuid(manager_id):
        return jsonify({'error': 'Field ID and Manager ID must be valid UUIDs'}), 400
    
    field_service = FieldService()
    response, status_code = field_service.delete_field(field_id, manager_id)
    return jsonify(response), status_code

@api_bp.route('/get_best_fields', methods=['POST'])
def get_best_fields():
    user_id = request.json.get('user_id')
    sport_type = request.json.get('sport_type')
    
    if not user_id or not sport_type:
        return jsonify({'error': 'Field ID and Manager ID are required'}), 400

    if not is_valid_uuid(user_id):
        return jsonify({'error': 'User ID must be valid UUIDs'}), 400
    
    data = request.json
    field_service = FieldService()
    response, status_code = field_service.get_best_fields(data=data)
    return jsonify(response), status_code

@api_bp.route('/get_fields_by_sport_type', methods=['POST'])
def get_fields_by_sport_type():
    sport_type = request.json.get('sport_type')
    if not sport_type:
        return jsonify({'error': 'Sport type parameter is required'}), 400
    
    field_service = FieldService()
    fields, status_code = field_service.get_fields_by_sport_type(sport_type)
    return jsonify(fields), status_code

@api_bp.route('/get_fields_by_manager_id', methods=['POST'])
def get_fields_by_manager_id():
    manager_id = request.json.get('manager_id')
    if not manager_id:
        return jsonify({'error': 'Manager ID parameter is required'}), 400
    if not is_valid_uuid(manager_id):
        return jsonify({'error': 'Manager ID must be a valid UUID'}), 400
    
    field_service = FieldService()
    fields, status_code = field_service.get_fields_by_manager_id(manager_id)
    return jsonify(fields), status_code

@api_bp.route('/get_filtered_fields', methods=['POST'])
def get_filtered_fields():
    user_id = request.json.get('user_id')
    user_longitude = request.json.get('user_longitude')
    user_latitude = request.json.get('user_latitude')
    
    if not user_id or not user_latitude or not user_longitude :
        return jsonify({'error': 'User ID and User Longitude and User Latitude are required'}), 400

    if not is_valid_uuid(user_id):
        return jsonify({'error': 'User ID must be valid UUIDs'}), 400
    data = request.json
    field_service = FieldService()
    response = field_service.get_filtered_fields(data=data)
    return response

@api_bp.route('/get_field_by_id', methods=['POST'])
def get_football_field_by_id():
    data = request.json
    field_service = FieldService()
    response = field_service.get_available_time_slots(data=data)
    print(response)
    return response

@api_bp.route('/add_favorite', methods=['POST'])
def add_favorite():
    data = request.json
    user_id = data.get('user_id')
    field_id = data.get('field_id')
    if not is_valid_uuid(user_id):
        return jsonify({'error': 'User ID must be a valid UUID'}), 400
    if not is_valid_uuid(field_id):
        return jsonify({'error': 'Field ID must be a valid UUID'}), 400

    user_service = UserService()
    response = user_service.add_favorite(data)
    return response

@api_bp.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    user_id = request.json.get('user_id')
    field_id = request.json.get('field_id')
    if not is_valid_uuid(user_id):
        return jsonify({'error': 'User ID must be a valid UUID'}), 400
    if not is_valid_uuid(field_id):
        return jsonify({'error': 'Field ID must be a valid UUID'}), 400

    user_service = UserService()
    response = user_service.remove_favorite(user_id, field_id)
    return response

@api_bp.route('/get_user_favorites', methods=['POST'])
def get_user_favorites():
    user_id = request.json.get('user_id')
    if not is_valid_uuid(user_id):
        return jsonify({'error': 'User ID must be a valid UUID'}), 400

    user_service = UserService()
    favorite_fields, status_code = user_service.get_user_favorite_fields(user_id)
    return jsonify(favorite_fields), status_code

@api_bp.route('/create_reservation', methods=['POST'])
def create_reservation():
    data = request.json
    reservation_service = ReservationService()
    response = reservation_service.create_reservation(data=data)
    return response

@api_bp.route('/get_reservation', methods=['POST'])
def get_reservation():
    user_id = request.json.get('uuid')
    if not is_valid_uuid(user_id):
        return jsonify({'error': 'User ID must be a valid UUID'}), 400
    
    reservation_service = ReservationService()
    response, status_code = reservation_service.get_reservation(user_id)
    return jsonify(response), status_code

@api_bp.route('/update_reservation_status', methods=['PUT'])
def update_reservation_status():
    reservation_uuid = request.json.get('reservation_uuid')
    status = request.json.get('status')

    if not reservation_uuid:
        return jsonify({"error": "Reservation UUID is required"}), 400
    if not is_valid_uuid(reservation_uuid):
        return jsonify({'error': 'Reservation UUID must be a valid UUID'}), 400
    
    if not status:
        return jsonify({"error": "Status is required"}), 400

    reservation_service = ReservationService()
    success = reservation_service.update_reservation_status(reservation_uuid, status)

    if success:
        return jsonify({"message": "Reservation status updated successfully"}), 200
    else:
        return jsonify({"error": "Reservation not found or status update failed"}), 404
    
@api_bp.route('/get_reservations_by_manager', methods=['POST'])
def get_reservations_by_manager():
    manager_id = request.json.get('manager_id')
    if not manager_id:
        return jsonify({'error': 'Manager ID parameter is required'}), 400
    if not is_valid_uuid(manager_id):
        return jsonify({'error': 'Manager ID must be a valid UUID'}), 400
    
    reservation_service = ReservationService()
    reservations, status_code = reservation_service.get_reservations_by_manager(manager_id)
    return jsonify(reservations), status_code

@api_bp.route('/get_reservation_count_per_month_report', methods=['POST'])
def get_reservation_report():
    data = request.json
    year = data.get('year')
    manager_id = data.get('manager_id')
    
    if not year or not manager_id:
        return jsonify({'error': 'Year and Manager ID are required'}), 400

    if not is_valid_uuid(manager_id):
        return jsonify({'error': 'Manager ID must be a valid UUID'}), 400
    
    field_service = FieldService()
    response, status_code = field_service.get_reservation_report(manager_id,year)
    return jsonify(response), status_code

@api_bp.route('/get_hourly_reservations_report', methods=['POST'])
def get_hourly_reservations_report():
    data = request.json
    manager_id = data.get('manager_id')
    date = data.get('date')

    if not manager_id or not date:
        return jsonify({'error': 'Manager ID and date are required'}), 400

    if not is_valid_uuid(manager_id):
        return jsonify({'error': 'Manager ID must be a valid UUID'}), 400

    field_service = FieldService()
    response, status_code = field_service.get_hourly_reservations_report(manager_id, date)
    return jsonify(response), status_code

@api_bp.route('/get_football_stadiums', methods=['GET'])
def get_football_stadiums():
    data = {
        "1": {
            "id": "1",
            "name": "safi stadium",
            "width": 50,
            "length": 70,
            "location": "Shefa-Amr",
            "imageURL": "http://10.0.0.12:5000/api/images/stadium.jpg",
            "latitude": "37.3763",
            "longitude": "-122.0373",
            "type":"football"
        },
        "2": {
            "id": "2",
            "name": "samir stadium",
            "width": 50,
            "length": 70,
            "location": "Kiryat-Ata",
            "imageURL": "http://10.0.0.12/api/images/samir_stadium.jpg",
            "latitude": "37.3763",
            "longitude": "-122.0373",
             "type":"football"
        }
    }
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@api_bp.route('/create_payment', methods=['POST'])
def create_payment():
    data = request.json
    user_id = data.get('userid')
    if not is_valid_uuid(user_id):
        return jsonify({'error': 'User ID must be a valid UUID'}), 400
    payments_service = PaymentsService()
    response, status_code = payments_service.create_payments(data=data)
    return jsonify(response), status_code

@api_bp.route('/get_payment_by_id', methods=['POST'])
def get_payment_by_id():
    user_id = request.json.get('userid')
    if not is_valid_uuid(user_id):
        return jsonify({'error': 'User ID must be a valid UUID'}), 400
    payments_service = PaymentsService()
    response, status_code = payments_service.get_payment(user_id)
    return jsonify(response), status_code

@api_bp.route('/delete_payment', methods=['DELETE'])
def delete_payment():
    user_id = request.json.get('user_id')
    data = request.json
    if not is_valid_uuid(user_id):
        return jsonify({'error': 'User ID must be a valid UUID'}), 400
    payments_service = PaymentsService()
    response, status_code = payments_service.delete_payment(data)
    return jsonify(response), status_code

@api_bp.route('/add_rating', methods=['POST'])
def create_rating():
    data = request.json
    field_id = data["field_id"]
    if not is_valid_uuid(field_id):
        return jsonify({"error": "Field ID must be a valid UUID"}), 400
    user_id = data["user_id"]
    if not is_valid_uuid(user_id):
        return jsonify({"error": "User ID must be a valid UUID"}), 400
    ratings_service = RatingsService()
    response, status_code = ratings_service.create_rating(data)
    return jsonify(response), status_code

@api_bp.route('/send-auth-code/<phone_number>', methods=['GET'])
def send_auth_code(phone_number):
    try:
        #data = request.get_json()
        #phone_number = data.get('phone_number')
        if not phone_number:
            return jsonify({'error': 'Phone number is required'}), 400
        auth_code = generate_auth_code()
        # Customize the message as needed
        message = auth_code
        # Add the task to the queue
        sms_queue.put((phone_number, message))
        # Process the queue sequentially
        while not sms_queue.empty():
            phone, msg = sms_queue.get()
            send_sms(phone, msg)
            sms_queue.task_done()
        response = jsonify({'message': 'Authentication code sent successfully'})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/confirm-auth-code/<phonenum>/<authcode>', methods=['GET'])
def check_auth_code(phonenum,authcode):
    try:
        auth_code_queue.put((phonenum, authcode))
        # Process the queue sequentially
        while not auth_code_queue.empty():
            phone, auth = auth_code_queue.get()
            result = check_code(phone, auth)
            auth_code_queue.task_done()

        response = jsonify({'message': result})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    except Exception as e:
     return jsonify({'error': str(e)}), 500

@api_bp.route('/images/<image_name>', methods=['GET'])
def get_image(image_name):
    try:
        response = send_file(f'images/{image_name}', mimetype='image/jpeg')
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except FileNotFoundError:
        return "Image not found", 404

    return

@api_bp.route('/generate_deeplink', methods=['POST'])
def generate_deeplink():
    try:
        data = request.json
        reservation_id = data.get('reservation_id')
        if reservation_id is not None:
            android_deep_link = generate_android_deep_link(reservation_id)
            ios_deep_link = generate_ios_deep_link(reservation_id)
            return jsonify({
                'android_deep_link': android_deep_link,
                'ios_deep_link': ios_deep_link
            }), 200
        else:
            return jsonify({'message': 'Invalid data'}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@api_bp.route('/auth/google_sign_in', methods=['POST'])
def google_sign_in():
    token = request.json.get('idToken')
    if not token:
        return jsonify({'error': 'Missing token'}), 400

    try:
        id_info = id_token.verify_oauth2_token(token, requests.Request(), os.getenv('630533245227-f7rj997qs8075alurbhbg3c79vaci4p1.apps.googleusercontent.com'))

        # If the token is valid, get user information
        user_id = id_info['sub']
        email = id_info['email']
        name = id_info.get('name')
        
        # Here you can create the user in your database or update the existing user

        return jsonify({'message': 'Sign-in successful'}), 200
    except ValueError:
        # Invalid token
        return jsonify({'error': 'Invalid token'}), 400    
