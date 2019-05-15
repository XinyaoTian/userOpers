from app import db
from app.models import User

if __name__ == '__main__':

    u = User(
        username='Mike',
        password_hash='0a',
        email='Mike@example.com',
        phone_number='11311311113',
    )

    db.session.add(u)
    db.session.commit()

    users = User.query.all()
    print(users)
