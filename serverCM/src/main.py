import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


DATABASE_URI = "mysql://backend:password@cookmaster-backend_db-1:3306/cookmaster"
TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = TRACK_MODIFICATIONS
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Web App with Python Flask!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
