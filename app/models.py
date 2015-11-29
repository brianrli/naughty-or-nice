from app import db

# model for students
class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    netid = db.Column(db.String(10))
    name = db.Column(db.String(25))
    email = db.Column(db.String(50))
    is_naughty = db.Column(db.Boolean(), nullable=False, default=False)
    message = db.Column(db.String(100))

    def __init__(self,name,email,is_naughty=False,message=None):
        self.name = name
        self.email = email
        self.is_naughty = is_naughty
        self.message = message

    def __repr__(self):
        return '#Netid: %s Name: %s Email: %s Naughty: %s' % (self.netid,self.name,self.email,self.is_naughty)