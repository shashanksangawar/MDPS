import joblib, json
import numpy as np
import pandas as pd


def model_import():
    try:                    
        heart_json = open("config.json", "r")                   
        heart_path = heart_json.read()
        heart_json = json.loads(heart_path)                                          
        heart_path = heart_json["Models"]["Heart"]
        heart_model = joblib.load(heart_path)
        return heart_model
    except Exception as w:                                                            
        return w

def heart_prediction(form):                                                                   
    try:
        model = model_import()
        print(model)
        to_predict_dict = form.to_dict()

        feature_df = pd.DataFrame([to_predict_dict])
        feature_df.drop(['id','name'], axis=1,  inplace=True)
        result = model.predict(feature_df)
        if result[0] == 1:
            return "<h1>You may have/get an Heart Disease </h1>"
        elif result[0] == 0:
            return "<h1>You don't have/get an Heart Disease </h1>"
    except Exception as e:
        return e                                      

