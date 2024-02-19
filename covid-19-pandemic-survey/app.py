from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Construct the path to the SQLite database file
database_filename = "SurveyResults.db"
current_directory = os.path.dirname(os.path.realpath(__file__))
database_path = os.path.join(current_directory, database_filename)

app = Flask(__name__, template_folder='templates')

# Configure SQLAlchemy to use the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

from models import SurveyResponse  

# Initialize database within app context
with app.app_context():
    try:
        db.create_all()
        app.logger.info("Database tables created successfully.")
    except Exception as e:
        app.logger.error("Error creating database tables: %s", e)
        
@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/thankyou.html')
def show_results():
     return render_template('thankyou.html')

@app.route('/results.html')
def results():
    return render_template('results.html')


@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    try:
        print("Received POST request to /submit_survey")
        
        # Parse JSON data from the request
        survey_data = request.get_json()
        print("Received survey data:", survey_data)

        # Extract data from JSON and create a new SurveyResponse object
        new_response = SurveyResponse(
            gender=survey_data.get('gender'),
            age=survey_data.get('age'),
            occupation=survey_data.get('occupation'),
            technology=survey_data.get('technology'),
            remoteWorkExperience=survey_data.get('remoteWorkExperience'),
            challenges=survey_data.get('challenges'),
            healthServices=survey_data.get('healthServices'),
            healthExperience=survey_data.get('healthExperience'),
            socialConnection=survey_data.get('socialConnection'),
            mentalHealth=survey_data.get('mentalHealth'),
            futureTech=survey_data.get('futureTech'),
            techAdvancements=survey_data.get('techAdvancements')
        )
        print("Created new SurveyResponse object:", new_response)

        # Add the new response to the database session and commit
        db.session.add(new_response)
        db.session.commit()

        # Return a success message
        return jsonify({"message": "Survey submitted successfully"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500



@app.route('/survey_results', methods=['GET'])
def survey_results():
    try:
        responses = SurveyResponse.query.all()
        response_data = [{
            'gender': response.gender,
            'age': response.age,
            'occupation': response.occupation,
            'technology': response.technology,
            'remoteWorkExperience': response.remoteWorkExperience,
            'challenges': response.challenges,
            'healthServices': response.healthServices,
            'healthExperience': response.healthExperience,
            'socialConnection': response.socialConnection,
            'mentalHealth': response.mentalHealth,
            'futureTech': response.futureTech,
            'techAdvancements': response.techAdvancements,
        } for response in responses]
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)