from server.app import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    rating = db.Column(db.Integer)  

    episode = db.relationship('Episode', backref='appearances')
    guest = db.relationship('Guest', backref='appearances')
