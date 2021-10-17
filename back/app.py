import logging
import random
import time

from celery import Celery
from flask import Flask, jsonify, request, url_for
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
celery = Celery(app.name,
                broker=app.config['CELERY_BROKER_URL'],
                backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.update(app.config)


@celery.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}


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


@app.route('/longtask', methods=['POST'])
def longtask():
    task = long_task.apply_async()
    return jsonify({'status': url_for('taskstatus', task_id=task.id)}), \
           202, \
           { 'Content-Type': 'application/json'}


@app.route('/status/<task_id>', methods=['GET'])
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
