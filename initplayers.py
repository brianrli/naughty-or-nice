from app import db
from app.models import Player

# initial test
db.drop_all()
db.create_all()
db.session.add(Player('Brian','brian.li@yale.edu',False,"You are a blessing on this earth."))
db.session.add(Player('Ben','benjamin.bartolome@yale.edu',True))
db.session.add(Player('Kevin','kevin.garcia@yale.edu',True,'Sucks to suck.'))
db.session.add(Player('Aimee','aimee.sawyer@yale.edu'))
db.session.commit()