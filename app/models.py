from app import db


class Item(db.Model):
    __name__ = "item"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    qty = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    owned = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Item {self.name}, {self.qty}, {self.price}>'


class User(db.Model):
    __name__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Float(), nullable=False, default=1000.00)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}, {self.email}, {self.password}>'