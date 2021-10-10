import logging

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from config import Config

# setup logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# instantiate the app
app = Flask(__name__)
app.config.from_object(Config)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})  # silence the deprecation warning

# Initialize DB
db = SQLAlchemy(app)


@dataclass
class Target(db.Model):
    __tablename__ = 'target'
    __table_args__ = {'schema': 'whodat'}

    id: int
    json_doc: dict
    created_at: str
    updated_at: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    json_doc = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/targets', methods=['GET'])
def get_targets():
    targets = Target.query.all()
    return jsonify(targets)


@app.route('/target/<id>', methods=['GET'])
def get_target(id):
    target = Target.query.get(id)
    return jsonify(target)


@app.route('/target/insert', methods=['POST'])
def insert_target():
    target = Target(json_doc=request.json)
    db.session.add(target)
    db.session.commit()
    return jsonify(target)


@app.route('/target/update/<id>', methods=['PUT'])
def update_target(id):
    target = Target.query.get(id)
    target.json_doc = request.json
    target.updated_at = db.func.now()
    db.session.commit()
    return jsonify(target)


@app.route('/target/delete/<id>', methods=['DELETE'])
def delete_target(id):
    target = Target.query.get(id)

    db.session.delete(target)
    db.session.commit()
    return jsonify(target)


if __name__ == '__main__':
    app.run()
