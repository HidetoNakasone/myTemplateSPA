from datetime import datetime
from flask import *
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


# Flask Config
app = Flask(__name__)
CORS(app)

# SQLAlchemy Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# DB Models
class Product(db.Model):
  __tablename__ = 'products'
  id = db.Column(db.Integer, primary_key=True,
                 nullable=False, autoincrement=True)
  name = db.Column(db.Text)
  price = db.Column(db.Integer)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(
      db.DateTime, default=datetime.now, onupdate=datetime.now)


# Schema
class ProductSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Product


@app.before_first_request
def init():
  db.create_all()


# Flask Routeing
@app.route('/api-test')
def index():
  all_products = Product.query.all()
  products_schema = ProductSchema(many=True)
  return products_schema.dump(all_products)


if __name__ == '__main__':
  app.debug = True
  app.run(port=5000)
