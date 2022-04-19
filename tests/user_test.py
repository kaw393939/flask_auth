from app import db
from app.db.models import User, Song
from faker import Faker

def test_adding_user(application):
    with application.app_context():
        Faker.seed(4321)
        fake = Faker()
        for _ in range(10):
            print(fake.email())

        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        user = User('keith@webizly.com', 'testtest')
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
        user = User.query.filter_by(email='keith@webizly.com').first()
        assert user.email == 'keith@webizly.com'
        user.songs= [Song("test")]
        db.session.commit()
        assert db.session.query(Song).count() == 1
        song1 = Song.query.filter_by(title='test').first()
        assert song1.title == "test"
        song1.title = "spam"
        db.session.commit()
        song2 = Song.query.filter_by(title='spam').first()
        assert song1.title == "spam"
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0




