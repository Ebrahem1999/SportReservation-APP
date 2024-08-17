from svc.db import db
from sqlalchemy.dialects.postgresql import JSON


class Field(db.Model):
    __tablename__ = 'fields'

    uid = db.Column(db.UUID(as_uuid=True), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    latitude = db.Column(db.String(30)) 
    longitude = db.Column(db.String(30))  
    sport_type = db.Column(db.String(100))  
    conf_interval = db.Column(db.String, nullable=True)  
    imageURL = db.Column(db.String(100))
    manager_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('users.uid'), nullable=False)
    utilities = db.Column(JSON, nullable=True) 

    reservations = db.relationship('Reservations', back_populates='field')
    ratings = db.relationship('Ratings', back_populates='field')
    manager = db.relationship('User', back_populates='fields_managed')

    def asdict_with_relation(self):
        reservation_dicts = [reservation.asdict_reservation() for reservation in self.reservations]
        return {
            'uid': self.uid,
            'name': self.name,
            'location': self.location,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'conf_interval': self.conf_interval,
            'reservations': reservation_dicts,
            'utilities': self.utilities
        }
    
    def asdict(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'location': self.location,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'sport_type': self.sport_type,
            'imageURL': self.imageURL,
            'utilities': self.utilities,
            'conf_interval': self.conf_interval,
            'manager_id': self.manager_id

        }
    
    def asdict_conf_interval(self):
        return {
            'conf_interval': self.conf_interval
        }
    
    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            uid=dict_obj.get('uid'),
            name=dict_obj.get('name'),
            location=dict_obj.get('location'),
            latitude=dict_obj.get('latitude'),
            longitude=dict_obj.get('longitude'),
            sport_type=dict_obj.get('sport_type'),
            conf_interval=dict_obj.get('conf_interval'),
            imageURL=dict_obj.get('imageURL'),
            manager_id=dict_obj.get('manager_id'),
            utilities=dict_obj.get('utilities')
        )
