from datetime import datetime
from user_journal import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    journals = db.relationship('Journal', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.name}','{self.username}')"


class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publish_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    journal_entry = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Journal('{str(self.publish_time)}','{self.journal_entry[:50]}')"
