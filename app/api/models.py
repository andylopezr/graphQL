from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    #recommended = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Date)
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            #"recommended": self.recommended,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }