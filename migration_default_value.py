from app import db
from app.models import User

users = User.query.all()

for user in users:
    user.is_active = True
    db.session.commit()
