from flask_sqlalchemy import SQLAlchemy

class Target(SQLAlchemy.Model):
    __tablename__ = 'target'
    # __table_args__ = {'schema': 'whodat'}
    __bind_key__ = 'other_schema'

    id = db.Column(db.Integer, primary_key=True)
    json_doc = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return '<Target %r>' % self.json_doc

    def __init__(self, json_doc):
        self.json_doc = json_doc
