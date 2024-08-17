from svc.dao.reservation_dao import ReservationDAO
from svc.dao.user_dao import UserDAO
class ReservationService():

    def __init__(self):
        self.reservation_dao = ReservationDAO()
        self.user_dao = UserDAO()


    def create_reservation(self, data):
        response = self.reservation_dao.create_reservation(data=data)
        return response
    
    def get_reservation(self, user_id):  
        # Check if the user exists
        user = self.user_dao.get_user_by_id(user_id)
        if not user:
            return {"error": "User does not exist"}, 404
        
        reservations = self.reservation_dao.get_reservations_by_user_uuid(user_id)
        if not reservations:
            return {"message": "No reservations found for the given user ID"}, 200

        all_reservations = []
        for reservation in reservations:
            all_reservations.append(reservation.asdict_reservation())
        return all_reservations, 200
    
    def update_reservation_status(self, uuid,Upstatus):
        reservation = self.reservation_dao.get_reservation_by_reservation_uuid(uuid)
        if not reservation:
            return False  # Reservation not found

        reservation_dao = ReservationDAO()
        success = reservation_dao.update_reservation_status(uuid, status=Upstatus)
        return success
    
    def get_reservations_by_manager(self, manager_id):
        reservations = self.reservation_dao.get_reservations_by_manager_id(manager_id)
        if not reservations:
            return {"message": "No reservations found for the given manager ID"}, 200
        all_reservations = []
        for reservation in reservations:
            all_reservations.append(reservation.asdict_reservation())
        return all_reservations, 200
    
    

    


def generate_android_deep_link(reservation_id):
    # Define your Android app's package name
    android_package_name = "com.example.piere_app"  # Replace with your Android package name

    # Define your website URL and deep link path
    website_url = "https://127.0.0.1:5000"
    deep_link_path = f"/deeplink/{reservation_id}"

    # Create the Android deep link
    android_deep_link = f"android-app://{android_package_name}{deep_link_path}"

    return android_deep_link


def generate_ios_deep_link(reservation_id):
    # Define your iOS app's bundle identifier
    ios_bundle_identifier = "com.example.myapp"  # Replace with your iOS bundle identifierx

    # Define your website URL and deep link path
    website_url = "https://your-app-url.com"
    deep_link_path = f"/deeplink/{reservation_id}"

    # Create the iOS deep link (Universal Link)
    ios_deep_link = f"https://{ios_bundle_identifier}.app links.your-app-url.com{deep_link_path}"

    return ios_deep_link


