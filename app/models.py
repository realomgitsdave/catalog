from . import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), index=True, unique=True)
    description = db.Column(db.String(255), index=True)

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), index=True)
    description = db.Column(db.String(255), index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Item {}>'.format(self.name)