import joblib, json
import numpy as np
import pandas as pd


def model_import():
    try:                    
        cancer_json = open("config.json", "r")                   
        cancer_path = cancer_json.read()
        cancer_json = json.loads(cancer_path)                                          
        cancer_path = cancer_json["Models"]["Diabetes"]
        cancer_model = joblib.load(cancer_path)
        return cancer_model
    except Exception as w:                                                            
        return w

def diabetes_prediction(form):                                                                   
    try:
        model = model_import()   
        to_predict_dict = form.to_dict()
        feature_df = pd.DataFrame([to_predict_dict])
        feature_df.drop(['id','name', 'sex'], axis=1,  inplace=True)
        features = np.asarray(feature_df)
        result = model.predict(features.reshape(1, -1))
        if result[0] == 1:
            return "<h1>You may have/get Diabetes </h1>"
        elif result[0] == 0:
            return "<h1>You don't have/get Diabetes </h1>"
    except Exception as e:
        return f"{e}"                                      

