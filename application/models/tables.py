from application import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


class Hotel(db.Model):
    __tablename__ = "hoteis"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    reservado = db.Column(db.Boolean)

    def get_reservado(self):
        return str(self.reservado)

    def __init__(self, id, name, reservado):
        self.id = id
        self.name = name
        self.reservado = reservado

    def __repr__(self):
        return "%r" % self.reservado


class Reserva(db.Model):
    __tablename__ = "reserva"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))

    user = db.relationship('User', foreign_keys=user_id)
    hotel = db.relationship('Hotel', foreign_keys=hotel_id)

    def __init__(self, user_id, hotel_id):
        self.user_id = user_id
        self.hotel_id = hotel_id
