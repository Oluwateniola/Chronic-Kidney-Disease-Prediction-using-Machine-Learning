import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from api.model.utils import Data
import pickle
import json


# load the model
fullModel = pickle.load( open( "api/model/kd_model.pkl", "rb" ) )



# respond to endpoint
def predict_response(dict_file):
    # convert data to dataframe
    df = pd.DataFrame.from_dict([dict_file])

    # slice out the values of the dataframe only
    array = df.values
    array_data = array[:,0:24]
    result = fullModel.predict(array_data)

    return {
            'message': "Success",
            'prediction': result[0]
            }


