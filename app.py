from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
        __tablename__ = 'persons'
        id=db.Column(db.Integer,primary_key=True)
        name=db.Column(db.String(200), nullable=False)

        def __repr__(self):
                return f'<Person ID:{self.id}, NAME:{self.name}>'

db.create_all()

@app.route('/')
def index():
        person = Person.query.first()
        return 'Hellow '+person.name

if __name__ == "__main__":
        app.debug = True
        app.run()
