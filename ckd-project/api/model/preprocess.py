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


# def convert_to_numeric(name_of_data, column):
#     '''Converting numerical columns with data type object to float'''
#     num_data = pd.to_numeric(name_of_data[column], errors = 'coerce')
#     return num_data

# def convert_to_str(the_data):
#     '''Converting numerical columns with data type float to string'''
#     data = the_data.astype(str)
#     return data

# def replace_values(name_of_data, column, dict_value):
#     '''To replace incorrect values.
#     dict_value {a:b} is a dictionary that has the old value as 'key a' and the correct value as value b.
#     Remember to import pandas before running your function'''
    
#     data = name_of_data[column].replace(to_replace = dict_value)
#     return data

# def convert_col(Data):
#     Data.albumin = convert_to_str(Data.albumin)
#     Data.sugar = convert_to_str(Data.sugar)
#     return Data



# def pipeline_transformer(num_features, cat_features):
#     """ - To transform numerical variables and categorical variables separately and then concatenate them.
#     - You will first create 2 separate lists of variable names for the numerical variables and categorical variables.
#     - num_features = list of numerical variable names
#     - cat_features = list of categorical variable names
#     """
#     num_pipe = Pipeline([('Scaler', StandardScaler())])
#     cat_pipe = Pipeline([('Encoder', OneHotEncoder())])
    
#     full_pipe = ColumnTransformer([('nums', num_pipe, num_features), ('cats', cat_pipe, cat_features)])
    
#     return full_pipe

# load the model
fullModel = pickle.load( open( "api/model/kd_model.pkl", "rb" ) )

# # convert json file to dataframe
# def json_df(js_data):
#     df = pd.read_json(data, lines=True)
#     return df

# # prediction
# def predictor(dataframe, model):
#     result = model.predict(dataframe)
#     return result


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


