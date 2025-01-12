"""
api URL:  http://127.0.0.1:5000/api/create_user
body:
    {
        "firstname" :"obied",
        "password" : "haddad",
        "phonenum" : "0509021620"
    }

response:
    {
        'message': 'User created successfully',
        'username': "obied",
        'phonenum': "0509021620"
    }

Other response:
    {
        "error": "User with this phone number already exists"
    }
OR:
    {
        "error": "User with this username already exists"
    }
OR:
    {
        "error": "Phone number is required"
    }
OR:
    {
        "error": "Password are required"
    }
OR:
    {
        "error": "Username is required"
    }

api URL:  http://127.0.0.1:5000/api/user_verfication
body:
    {
        "username" :"obied",
        "password" : "haddad",
    }

response:
    {
        "message": "User Verified",
        "preferences": "wifi-0, parking-1",
        "user_type": null,
        "userid": "2026a8ac-7d4d-41a2-855d-4095c13cc180"
    }

Other response:
    {
        "error": "Invalid username or password"
    }


api URL:  http://127.0.0.1:5000/api/get_user_by_name
body:
{
 "user_info": "ebrahem"
}

response:
{
    "phonenum": "0509871234",
    "username": "ebrahem"
}

api_url: http://127.0.0.1:5000/api/get_fields_by_sport_type
body:
    {
    "sport_type": "tennis"
    }
response:
    [
        {
            "average_rating": 0,
            "conf_interval": "14:00-16:00, 50, 16:00-18:00, 45, 19:00-20:00, 60, 22:00-00:00, 30",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "37.23.55",
            "location": "adi",
            "longitude": "-122.0373",
            "manager_id": "6d3c4dc5-0951-41b1-afc7-139cc019e1a1",
            "name": "adi club",
            "sport_type": "tennis",
            "uid": "cf98fbe7-bf6c-4136-a7e3-b41dc7506571",
            "utilities": {
                "Bathroom": 1,
                "Free parking": 0,
                "Lights": 0,
                "Pool": 0,
                "Sport equipment": 1
            }
        },
        {
            "average_rating": "5.0000000000000000",
            "conf_interval": "14:00-15:00,50 15:00-16:00,60 08:00-09:00,5",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "17.53.85",
            "location": "shefa-amr",
            "longitude": "-191.1373",
            "manager_id": "6d3c4dc5-0951-41b1-afc7-139cc019e1a1",
            "name": "Marcana Shefa",
            "sport_type": "tennis",
            "uid": "94154805-8c01-4653-8592-feb960805ea8",
            "utilities": {
                "Bathroom": 1,
                "Free parking": 1,
                "Lights": 1,
                "Pool": 1,
                "Sport equipment": 1
            }
        },
        {
            "average_rating": "4.5000000000000000",
            "conf_interval": "14:00-15:00,50 15:00-16:00,60 08:00-09:00,5",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "17.53.85",
            "location": "shefa-amr",
            "longitude": "-191.1373",
            "manager_id": "fc328116-cc1a-4c53-81f1-9db545c40d78",
            "name": "Marcana Shefa",
            "sport_type": "tennis",
            "uid": "4acbfc5b-062b-4e44-b807-f83c6e28bead",
            "utilities": {
                "Bathroom": 1,
                "Free parking": 1,
                "Lights": 1,
                "Pool": 1,
                "Sport equipment": 1
            }
        }
    ]

other response:
    {
        "message": "No fields found for the given sport type"
    }
OR:
    {
        "error": "Sport type parameter is required"
    }

api_url: http://127.0.0.1:5000/api/get_fields_by_manager_id
body:
    [
        {
            "average_rating": 0,
            "conf_interval": "14:00-16:00, 50, 16:00-18:00, 45, 19:00-20:00, 60, 22:00-00:00, 30",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "37.23.55",
            "location": "adi",
            "longitude": "-122.0373",
            "manager_id": "6d3c4dc5-0951-41b1-afc7-139cc019e1a1",
            "name": "adi club",
            "sport_type": "tennis",
            "uid": "cf98fbe7-bf6c-4136-a7e3-b41dc7506571",
            "utilities": {
                "Bathroom": 1,
                "Free parking": 0,
                "Lights": 0,
                "Pool": 0,
                "Sport equipment": 1
            }
        },
        {
            "average_rating": "2.6666666666666667",
            "conf_interval": "14:00-16:00, 50, 16:00-18:00, 45, 19:00-20:00, 60, 22:00-00:00, 30",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "37.23.55",
            "location": "adi",
            "longitude": "-122.0373",
            "manager_id": "6d3c4dc5-0951-41b1-afc7-139cc019e1a1",
            "name": "adi club",
            "sport_type": "Football",
            "uid": "df116407-9f58-448b-a541-1f66974b48f3",
            "utilities": {
                "Bathroom": 1,
                "Free parking": 0,
                "Lights": 0,
                "Pool": 0,
                "Sport equipment": 1
            }
        },
        {
            "average_rating": "5.0000000000000000",
            "conf_interval": "14:00-15:00,50 15:00-16:00,60 08:00-09:00,5",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "17.53.85",
            "location": "shefa-amr",
            "longitude": "-191.1373",
            "manager_id": "6d3c4dc5-0951-41b1-afc7-139cc019e1a1",
            "name": "Marcana Shefa",
            "sport_type": "tennis",
            "uid": "94154805-8c01-4653-8592-feb960805ea8",
            "utilities": {
                "Bathroom": 1,
                "Free parking": 1,
                "Lights": 1,
                "Pool": 1,
                "Sport equipment": 1
            }
        }
    ]

other respone:
    {
        "message": "No fields found for the given Manager ID"
    }
OR:
    {
        "error": "Manager ID must be a valid UUID"
    }
OR:
    {
        "error": "Manager ID parameter is required"
    }

api_url: http://127.0.0.1:5000/api/get_best_fields
    body:
    {
    "sport_type": "Football",
    "longitude": "35.180806",
    "latitude": "32.798167",
    "permission": "true",
    "user_id": "d2ae0c5d-4c81-49e3-acf7-a929be06a616"
    }
Other body:
    {
    "sport_type": "Football",
    "longitude": "0",
    "latitude": "0",
    "permission": "false",
    "user_id": "d2ae0c5d-4c81-49e3-acf7-a929be06a616"
    }

response:
    [
        {
            "average_rating": "3.6666666666666667",
            "conf_interval": "14:00-16:00,50 19:00-20:00,60 22:00-00:00,30",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "32.8036",
            "location": "Shefa-amr",
            "longitude": "35.1733",
            "manager_id": "fc328116-cc1a-4c53-81f1-9db545c40d78",
            "name": "Shefaamr",
            "sport_type": "Football",
            "total_score": 109.71377902104277,
            "uid": "ce97b7f9-b3a1-4294-bfb6-54ac61e2d354",
            "utilities": {
                "Bathroom": 1,
                "Free parking": 1,
                "Lights": 0,
                "Pool": 0,
                "Sport equipment": 1
            }
        },
        {
            "average_rating": "2.3333333333333333",
            "conf_interval": "14:00-16:00,50 16:00-18:00,60 20:00-22:00,60",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "32.8553",
            "location": "Tamara",
            "longitude": "35.1859",
            "manager_id": "2026a8ac-7d4d-41a2-855d-4095c13cc180",
            "name": "Tamra",
            "sport_type": "Football",
            "total_score": 18.3454608900502,
            "uid": "c1c8ab70-8725-4c77-8d33-16bd40a9425c",
            "utilities": {
                "Bathroom": 0,
                "Free parking": 0,
                "Lights": 0,
                "Pool": 0,
                "Sport equipment": 0
            }
        },
        {
            "average_rating": "4.0000000000000000",
            "conf_interval": "14:00-16:00,50 16:00-18:00,60 18:00-20:00,30",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "32.794044",
            "location": "Haifa",
            "longitude": "34.989571",
            "manager_id": "679b0918-c4cb-49aa-8849-3d84f1e84298",
            "name": "Haifa",
            "sport_type": "Football",
            "total_score": 6.917073964650308,
            "uid": "26d1ea4e-4d20-4d0b-ba6a-78944649b90a",
            "utilities": {
                "Bathroom": 1,
                "Free parking": 1,
                "Lights": 1,
                "Pool": 1,
                "Sport equipment": 1
            }
        }
    ]

Other response:
    {
        "error": "User ID must be valid UUIDs"
    }
OR:
    {
        "error": "User ID and Sport Type are required"
    }

api_url: http://127.0.0.1:5000/api/get_filtered_fields
body:
    {
        "date": "21.09.2023",
        "start_time": "14:00",
        "end_time": "22:00",
        "location": "Haifa",
        "sport_type": "Football",
        "user_id": "a7578c2b-d2e0-4738-b09a-5eb8df1dd207",
        "user_latitude": "32.794044",
        "user_longitude": "34.989571"
    }
response:
    [
        {
            "average_rating": "5.0000000000000000",
            "conf_interval": "14:00-16:00,50 19:00-20:00,60",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "32.8036",
            "location": "Shefa-amr",
            "longitude": "35.1733",
            "manager_id": "fc328116-cc1a-4c53-81f1-9db545c40d78",
            "name": "Shefaamr",
            "sport_type": "tennis",
            "total_score": 7.2947844735270895,
            "uid": "d4734484-a896-44d9-bd87-4d2ad5412551",
            "utilities": {
                "Bathroom": 1,
                "Free parking": 1,
                "Lights": 0,
                "Pool": 0,
                "Sport equipment": 1
            }
        },
        {
            "average_rating": 0,
            "conf_interval": "14:00-16:00,50 16:00-18:00,60 20:00-22:00,60",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "32.8553",
            "location": "Tamara",
            "longitude": "35.1859",
            "manager_id": "2026a8ac-7d4d-41a2-855d-4095c13cc180",
            "name": "Tamra",
            "sport_type": "tennis",
            "total_score": 5.362317325672179,
            "uid": "fe82f1ea-6d7a-4ac1-b0fc-90d5e8cea511",
            "utilities": {
                "Bathroom": 0,
                "Free parking": 0,
                "Lights": 0,
                "Pool": 0,
                "Sport equipment": 0
            }
        },
        {
            "average_rating": "5.0000000000000000",
            "conf_interval": "14:00-16:00,50",
            "imageURL": "lib/images/samir_stadium.jpg",
            "latitude": "32.794044",
            "location": "Haifa",
            "longitude": "34.989571",
            "manager_id": "679b0918-c4cb-49aa-8849-3d84f1e84298",
            "name": "Haifa",
            "sport_type": "tennis",
            "total_score": 2.8877343400756312,
            "uid": "a0d4728e-fae6-4557-a3d4-ee1d7ce8a17a",
            "utilities": {
                "Bathroom": 1,
                "Free parking": 1,
                "Lights": 1,
                "Pool": 1,
                "Sport equipment": 1
            }
        }
    ]

other response:
    {
        "message": "No fields found matching the criteria"
    }
OR:
    []
OR:
    {
        "error": "User ID must be a valid UUID"
    }
OR:
    {
        "error": "User ID and User Longitude and User Latitude are required"
    }

api_url:http://127.0.0.1:5000/api/add_favorite
body:
    {
    "user_id":"c22424d8-909a-45a1-809a-6e06bbdc0aa8",
    "field_id":"0c64c061-2dc2-4e83-9b49-39794eff16b8"
    }
response:
    {
        "message": "Field added to favorites successfully"
    }

Other response:
    {
        "error": "User ID must be a valid UUID"
    }
OR:
    {
        "error": "Field ID must be a valid UUID"
    }
OR:
    {
        "error": "This field is already in your favorites"
    }
OR:
    {
    "error": "Field does not exist"
    }
OR:
    {
    "error": "User does not exist"
    }

api_url:http://127.0.0.1:5000/api/remove_favorite
body:
    {
    "user_id":"c22424d8-909a-45a1-809a-6e06bbdc0aa8",
    "field_id":"0c64c061-2dc2-4e83-9b49-39794eff16b8"
    }

response:
    {
        "message": "Field removed from favorites successfully"
    }

Other response:
    {
        "error": "This field is not in your favorites"
    }
OR:
    {
        "error": "User ID must be a valid UUID"
    }
OR:
    {
        "error": "Field ID must be a valid UUID"
    }
OR:
    {
        "error": "This field is already in your favorites"
    }



api_url:http://127.0.0.1:5000/api/get_user_favorites
body:
    {
    "user_id":"d8856094-79d0-44fd-9819-01f6f1a7b982"
    }
response:
    [
        {
            "imageURL": "http://10.0.0.12/api/images/samir_stadium.jpg",
            "latitude": "37.23.55",
            "location": "adi",
            "longitude": "-122.0373",
            "name": "adi club",
            "price": 50.0,
            "sport_type": "tennis",
            "uid": "0c64c061-2dc2-4e83-9b49-39794eff16b8"
        },
        {
            "imageURL": "http://10.0.0.12/api/images/samir_stadium.jpg",
            "latitude": "37.23.55",
            "location": "haifa",
            "longitude": "-122.0373",
            "name": "marcana",
            "price": 50.0,
            "sport_type": "football",
            "uid": "171bc20e-7964-4045-90e8-cb3429455a05"
        }
    ]

Other response:
    {
        "message": "No favorite fields found for this user."
    }
OR:
    {
        "error": User ID must be a valid UUID"
    }

api_url: http://127.0.0.1:5000/api/create_reservation
body:
    {
    "field_id": "25096a7b-4566-4f34-b45e-920e3d67cde9",
    "date": "20.09.2023",
    "interval_time": "15:00-17:00",
    "status": "pending",
    "du_date": "20.09.2023",
    "du_time": "18:00",
    "user_uuid": "c22424d8-909a-45a1-809a-6e06bbdc0aa8",
    "price": "50",
    "field_name": "samer",
    "location": "shefa-amr",
        "imageURL": "http://10.0.0.12/api/images/samir_stadium.jpg"
    }
response:
    {
        "message": "Reservation created successfully"
    }

api_url:http://127.0.0.1:5000/api/get_reservation
body:
    {
        "uuid": "d8856094-79d0-44fd-9819-01f6f1a7b982"
    }
response:
    [
        {
            "date": "20/09/2023",
            "du_date": "20/09/2023",
            "du_time": "18:00",
            "field_id": "171bc20e-7964-4045-90e8-cb3429455a05",
            "imageURL": "http://10.0.0.12/api/images/samir_stadium.jpg",
            "interval_time": "15:00-17:00",
            "location": "haifa",
            "name": "marcana",
            "price": 50,
            "status": "pending",
            "uid": "c21dd6af-3b40-40d0-9348-afeaf77de7a7",
            "user_uuid": "d8856094-79d0-44fd-9819-01f6f1a7b982"
        },
        {
            "date": "20/09/2023",
            "du_date": "20/09/2023",
            "du_time": "18:00",
            "field_id": "25096a7b-4566-4f34-b45e-920e3d67cde9",
            "imageURL": "http://10.0.0.12/api/images/samir_stadium.jpg",
            "interval_time": "15:00-17:00",
            "location": "haifa",
            "name": "marcana",
            "price": 50,
            "status": "pending",
            "uid": "0963245a-7856-4c09-b798-58288a026598",
            "user_uuid": "d8856094-79d0-44fd-9819-01f6f1a7b982"
        },
        {
            "date": "20/09/2023",
            "du_date": "20/09/2023",
            "du_time": "18:00",
            "field_id": "25096a7b-4566-4f34-b45e-920e3d67cde9",
            "imageURL": "http://10.0.0.12/api/images/samir_stadium.jpg",
            "interval_time": "15:00-17:00",
            "location": "shefa-amr",
            "name": "samer",
            "price": 50,
            "status": "pending",
            "uid": "ecb1512e-f714-4c35-abb4-26e26c465218",
            "user_uuid": "d8856094-79d0-44fd-9819-01f6f1a7b982"
        }
    ]

Other response:
    {
        "error": "User ID must be a valid UUID"
    }
OR:
    {
        "error": "User does not exist"
    }
OR:
    {
        "message": "No reservations found for the given user ID"
    }

api_url: http://127.0.0.1:5000/api/update_reservation_status
body:
    {
    "reservation_uuid": "c21dd6af-3b40-40d0-9348-afeaf77de7a7",
    "status": "Accepted"
    }
response:
    {
        "message": "Reservation status updated to 'canceled'"
    }

Other response:
    {
        "message": "Reservation not found or status update failed"
    }

api_url:http://127.0.0.1:5000/api/get_reservations_by_manager
body:
    {
        "manager_id": "6d3c4dc5-0951-41b1-afc7-139cc019e1a1"
    }
response:
    [
        {
            "date": "20/09/2023",
            "du_date": "20/09/2023",
            "du_time": "18:00",
            "field_id": "cf98fbe7-bf6c-4136-a7e3-b41dc7506571",
            "imageURL": "http://10.0.0.12/api/images/samir_stadium.jpg",
            "interval_time": "14:00-15:00",
            "location": "haifa",
            "name": "marcana",
            "price": 50,
            "status": "pending",
            "uid": "a9f0b2b4-0855-4bd8-b23f-ebca3257e2bf",
            "user_uuid": "fc328116-cc1a-4c53-81f1-9db545c40d78"
        },
        {
            "date": "28/09/2023",
            "du_date": "20/09/2023",
            "du_time": "18:00",
            "field_id": "cf98fbe7-bf6c-4136-a7e3-b41dc7506571",
            "imageURL": "http://10.0.0.12/api/images/samir_stadium.jpg",
            "interval_time": "14:00-15:00",
            "location": "haifa",
            "name": "marcana",
            "price": 50,
            "status": "pending",
            "uid": "56318498-4673-41b2-a1b4-6ddc831df8ff",
            "user_uuid": "fc328116-cc1a-4c53-81f1-9db545c40d78"
        }
    ]

Other esponse:
    {
        "error": "Manager ID parameter is required"
    }
OR:
    {
        "error": "Manager ID must be a valid UUID"
    }
OR:
    {
        "message": "No reservations found for the given manager ID"
    }


api_url: http://localhost:5000/api/create_field
body:
    {
        "name": "haifa-club",
        "location": "shefa-amr",
        "latitude": "17.53.85",
        "longitude": "-191.1373",
        "sport_type": "tennis",
        "conf_interval": "14:00-16:00,50 19:00-20:00,60 22:00-00:00,30",
        "imageURL": "lib/images/samir_stadium.jpg",
        "manager_id": "1dfe2197-3082-4564-bfed-6d0af5767562",
        "utilities": {
            "Pool": 0,
            "Lights": 0,
            "Bathroom": 1,
            "Sport equipment": 1,
            "Free parking": 0
        }
    }
response:
    {
        "Field_id": "ba07e482-c476-4a0a-ab53-18b588f74fd3"
    }

Other response:
    {
        "error": "Field with the same name, location, and sport type already exists"
    }
OR:
    {
        "error": "Manager ID must be a valid UUID"
    }

api URL: http://127.0.0.1:5000/api/update_conf_interval
body:
    {
        "field_id": "some-field-uuid",
        "conf_interval": "14:00-15:00,50 15:00-16:00,60 08:00-09:00,5"
    }

response:
    {
        "average_rating": "4.5000000000000000",
        "conf_interval": "14:00-15:00,50 15:00-16:00,60 08:00-09:00,25",
        "imageURL": "lib/images/samir_stadium.jpg",
        "latitude": "17.53.85",
        "location": "shefa-amr",
        "longitude": "-191.1373",
        "manager_id": "fc328116-cc1a-4c53-81f1-9db545c40d78",
        "name": "Marcana Shefa",
        "sport_type": "tennis",
        "uid": "4acbfc5b-062b-4e44-b807-f83c6e28bead",
        "utilities": {
            "Bathroom": 1,
            "Free parking": 1,
            "Lights": 1,
            "Pool": 1,
            "Sport equipment": 1
        }
    }

Other response:
    {
        "message": "Field not found"
    }
OR:
    {
        "error": "Field ID is required"
    }
OR:
    {
        "error": "Field ID must be a valid UUID"
    }


api URL: http://127.0.0.1:5000/api/update_field_details
body:
    {
        "field_id": "94154805-8c01-4653-8592-feb960805ea8",
        "name": "Marcana Shefa",
        "utilities": {
            "Pool": 1,
            "Lights": 1,
            "Bathroom": 1,
            "Sport equipment": 1,
            "Free parking": 1
        }
    }

response:
    {
        "average_rating": "4.5000000000000000",
        "conf_interval": "14:00-15:00,50 15:00-16:00,60 08:00-09:00,25",
        "imageURL": "lib/images/samir_stadium.jpg",
        "latitude": "17.53.85",
        "location": "shefa-amr",
        "longitude": "-191.1373",
        "manager_id": "fc328116-cc1a-4c53-81f1-9db545c40d78",
        "name": "Marcana Shefa",
        "sport_type": "tennis",
        "uid": "4acbfc5b-062b-4e44-b807-f83c6e28bead",
        "utilities": {
            "Bathroom": 1,
            "Free parking": 1,
            "Lights": 1,
            "Pool": 1,
            "Sport equipment": 1
        }
    }

response:
    {
        "message": "Field not found"
    }

Other response:
    {
        "error": "Field ID must be a valid UUID"
    }
OR:
    {
        "error": "Field ID is required"
    }



api URL: http://127.0.0.1:5000/api/delete_field
body:
    {
        "field_id": "valid-field-uuid",
        "manager_id": "valid-manager-uuid"
    }

response:
    {
        "message": "Field deleted successfully"
    }

Other response:
    {
        "message": "Field ID and Manager ID are required"
    }
OR:
    {
        "message": "Field ID and Manager ID must be valid UUIDs"
    }
OR:
    {
        "message": "Field does not belong to this manager"
    }

api URL:  http://127.0.0.1:5000/api/create_payment
body:
    {
        "carHolderID":"858888955",
        "cardNumber":"45698712365",
        "digitCode":"558",
        "month": "15",
        "name": "obied",
        "year": "2026",
        "userid": "fc328116-cc1a-4c53-81f1-9db545c40d78"
    }

response:
    {
        "message": "Payment created successfully"
    }

Other response:
    {
        "error": "A payment with this card number already exists"
    }
OR:
    {
        "error": "carHolderID is required"
    }
OR:
    {
        "error": "cardNumber is required"
    }
OR:
    {
        "error": "digitCode is required"
    }
OR:
    {
        "error": "month is required"
    }
OR:
    {
        "error": "year is required"
    }
OR:
    {
        "error": "name is required"
    }
OR:
    {
        "error": "User ID must be a valid UUID"
    }

       
api URL:  http://127.0.0.1:5000/api/get_payment_by_id
body:
    {
        "userid":"ab40d55f-0b04-46a0-9225-02beca70ecfd"
    }

    [
        {
            "cardNumber": "4325678914326545",
            "name": "obied"
        },
        {
            "cardNumber": "4123789654328877",
            "name": "obied"
        }
    ]

Other response:
    {
        "message": "No payments found for this user"
    }
OR:
    {
        "error": "User ID must be a valid UUID"
    }

api URL:http://127.0.0.1:5000/api/delete_payment
body:
    {
        "user_id": "fc328116-cc1a-4c53-81f1-9db545c40d78",
        "cardNumber":"412378976632845"
    }
response:
    {
        "message": "Payment deleted successfully"
    }
Other response:
    {
        "error": "Card not found"
    }
OR:
    {
        "error": "Card Number is required"
    }
OR:
    {
        "error": "User ID must be a valid UUID"
    }


api URL: http://127.0.0.1:5000/api/add_rating
body:
    {
        "field_id": "0d4d41a4-105c-48ad-80a2-5c5e0e8f3f7f",
        "user_id": "ab40d55f-0b04-46a0-9225-02beca70ecfd",
        "rating": 4.5
    }
response:
    {
        "message": "Rating created successfully"
    }
OR:
    {
        "message": "Rating updated successfully"
    }

Other response:
    {
        "error": "User does not exist."
    }
OR:
    {
        "error": "Field does not exist."
    }
OR:
    {
        "error": "Field ID must be a valid UUID"
    }
OR:
    {
        "error": "User ID must be a valid UUID"
    }


api URL: http://127.0.0.1:5000/api/update_preferences
body:
    {
        "username": "obied4",
        "preference": "wifi-0, parking-1"
    }

response:
    {
        "message": "Preferences updated successfully"
    }

Other response:
    {
        "error": "User ID must be a valid UUID"
    }
OR:
    {
        "message": "User not found"
    }
OR:
    {
        "error": "User ID and preference are required"
    }

api URL: http://127.0.0.1:5000/api/get_reservation_count_per_month_report
body:
    {
        "year": "2023",
        "manager_id": "6d3c4dc5-0951-41b1-afc7-139cc019e1a1"

    }

response:
    {
        "Marcana Shefa": {
            "2023": {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0,
                "10": 0,
                "11": 0,
                "12": 0
            }
        },
        "adi club": {
            "2023": {
                "1": 1,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 4,
                "10": 1,
                "11": 0,
                "12": 0
            }
        }
    }

Other response:
    {
        "error": "Manager ID must be a valid UUID"
    }
OR:
    {
        "error": "Year and Manager ID are required"
    }


api URL: http://127.0.0.1:5000/api/get_hourly_reservations_report
body:
    {
        "date": "9.2023",
        "manager_id": "2026a8ac-7d4d-41a2-855d-4095c13cc180"

    }

respoonse:
    {
        "09.2023": {
            "08:00-09:00": [
                {
                    "count": 0,
                    "field_name": "Marcana Shefa"
                }
            ],
            "14:00-15:00": [
                {
                    "count": 0,
                    "field_name": "Marcana Shefa"
                }
            ],
            "14:00-16:00": [
                {
                    "count": 4,
                    "field_name": "adi club"
                },
                {
                    "count": 2,
                    "field_name": "tel-aviv"
                }
            ],
            "15:00-16:00": [
                {
                    "count": 0,
                    "field_name": "Marcana Shefa"
                }
            ],
            "16:00-18:00": [
                {
                    "count": 2,
                    "field_name": "adi club"
                },
                {
                    "count": 1,
                    "field_name": "tel-aviv"
                }
            ],
            "19:00-20:00": [
                {
                    "count": 0,
                    "field_name": "adi club"
                },
                {
                    "count": 0,
                    "field_name": "tel-aviv"
                }
            ],
            "22:00-00:00": [
                {
                    "count": 0,
                    "field_name": "adi club"
                },
                {
                    "count": 0,
                    "field_name": "tel-aviv"
                }
            ]
        }
    }

Other respone:
    {
        "message": "No fields found for the given Manager ID"
    }
OR:
    {
        "error": "Manager ID must be a valid UUID"
    }
OR:
    {
        "error": "Manager ID and date are required"
    }
        

"""