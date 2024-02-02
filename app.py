# Importing Libraries
from flask import Flask, render_template, request
from flask_cors import CORS
import os, secrets

# Prediction Functions
from supporting.heart import heart_prediction
from supporting.cancer import cancer_prediction
from supporting.diabetes import diabetes_prediction
from supporting.dengue import dengue_prediction
from supporting.alzheimer import alzheimer_prediction

# Configuration for Flask App
app = Flask(__name__)
CORS(app)
app._static_folder = "templates/static/"
app.secret_key = secrets.token_hex(16)

# Directory Path of current file 
source_path = os.path.dirname(__file__)
source_path = str(source_path)


# --------------------------------
# --------- Front-end ------------
# --------------------------------


# Index Page
@app.route('/')
def ui_main_page():
    return render_template('index.html')

# Heart Disease Prediction
@app.route('/heart_disease')
def ui_heart_disease():
    return render_template('heart.html')

# Breast Cancer Prediction
@app.route('/breast_cancer')
def ui_breast_cancer():
    return render_template('cancer.html')

# Diabetes
@app.route('/diabetes')
def ui_diabetes():
    return render_template('diabetes.html')

# Dengue
@app.route('/dengue')
def ui_dengue():
    return render_template('dengue.html')

# Alzheimer
@app.route('/alzheimer')
def ui_alzheimer():
    return render_template('alzheimer.html')
# --------------------------------



# --------------------------------
# --------- Back-end ------------
# --------------------------------

# Heart Disease Prediction
@app.route('/api/heart_disease', methods=['POST'])
def api_heart_disease():
    return heart_prediction(form=request.form)

# Breast Cancer Prediction
@app.route('/api/breast_cancer', methods=['POST'])
def api_breast_cancer():
    return cancer_prediction(form=request.form)

# Diabetes
@app.route('/api/diabetes', methods=['POST'])
def api_diabetes():
    return diabetes_prediction(form=request.form)

# Dengue
@app.route('/api/dengue', methods=['POST'])
def api_dengue():
    return dengue_prediction(form=request.form)

# Alzheimer
@app.route('/api/alzheimer', methods=['POST'])
def api_alzheimer():
    return alzheimer_prediction(form=request.form)


@app.route('/test')
def test():
    return "<h1> Test Approved from U-Health </h1>"
# --------------------------------

if __name__ == '__main__':
    app.run(debug=True)