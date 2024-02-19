from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SurveyResults.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class SurveyResponse(db.Model):
    __tablename__ = 'survey_response'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(20))
    age = db.Column(db.String(20))
    occupation = db.Column(db.String(50))
    technology = db.Column(db.String(255))
    remoteWorkExperience = db.Column(db.String(255))
    challenges = db.Column(db.String(255))
    healthServices = db.Column(db.String(255))
    healthExperience = db.Column(db.String(255))
    socialConnection = db.Column(db.String(255))
    mentalHealth = db.Column(db.String(255))
    futureTech = db.Column(db.String(255))
    techAdvancements = db.Column(db.String(255))
    
# Create the database tables
with app.app_context():
    db.create_all()
  
