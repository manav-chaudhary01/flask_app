from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    items = db.relationship(
        "ItemModel",
        backref="store",
        cascade="all, delete"
    )


class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

    store_id = db.Column(
        db.String(32),
        db.ForeignKey("stores.id"),
        nullable=False
    )




# stores = {}
# items = {}


# pip install flask-sqlalchemy marshmallow


# items = {
#     "1" : {
#         "name" : "cold drink",
#         "price" : "40",
#         "store_id" : "abcd"
#     },
#     "2" : {
#         "name" : "chair",
#         "price" : "1000",
#         "store_id" : "efgh"
#     }
# }
