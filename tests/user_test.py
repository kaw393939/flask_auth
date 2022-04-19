from app import db
from app.db.models import User, Song
from faker import Faker

def test_adding_user(application):
    Faker.seed(4321)
    fake = Faker()
    for _ in range(10):
        print(fake.email())

    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        #showing how to add a record
        #create a record
        user = User('keith@webizly.com', 'testtest')
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='keith@webizly.com').first()
        #asserting that the user retrieved is correct
        assert user.email == 'keith@webizly.com'
        #this is how you get a related record ready for insert
        user.songs= [Song("test")]
        db.session.commit()
        assert db.session.query(Song).count() == 1
        song1 = Song.query.filter_by(title='test').first()
        assert song1.title == "test"
        #changing the title of the song
        song1.title = "spam"
        #saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(title='spam').first()
        assert song2.title == "spam"
        #checking cascade delete
        #db.session.delete(user)
        #assert db.session.query(User).count() == 0
        #assert db.session.query(Song).count() == 0




