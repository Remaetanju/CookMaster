from flask import Flask
from models.users import Student, db
# from flask_sqlalchemy import SQLAlchemy


TRACK_MODIFICATIONS = False
DATABASE_URI = "mysql+pymysql://back:backword@dbCMhost:3306/dbCM"

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = TRACK_MODIFICATIONS
db.init_app(app)


@app.route('/create')
def create():
    db.create_all()
    return 'create'


@app.route('/')
def list():
    return 'Web App with Python Flask!'


@app.route('/drop')
def drop():
    return 'drop'


@app.route('/john')
def john():
    student_john = Student(firstname='john', lastname='doe',
                           email='jd@example.com', age=23,
                           bio='Biology student')
    db.session.add(student_john)
    db.session.commit()
    return dict(mdr=student_john.id)


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=5000)
    app.run(host='0.0.0.0', port=5000)
