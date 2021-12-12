from pydantic import BaseModel
from fastapi import Query

#defining the numerical and categorical columns seperately
num_feats = ['age','blood_pressure','specific_gravity','blood_glucose_random','blood_urea','serum_creatinine','sodium','potassium','haemoglobin','packed_cell_volume','white_blood_cell_count','red_blood_cell_count']
cat_feats = ['albumin','sugar','red_blood_cells','pus_cell','pus_cell_clumps','bacteria','hypertension','diabetes_mellitus','coronary_artery_disease','appetite','peda_edema','aanemia']

class Data(BaseModel):
    age: float = Query(...)
    blood_pressure: float = Query(...)
    specific_gravity: float = Query(...)
    albumin: int = Query(...)
    sugar: int = Query(...)
    red_blood_cells: str = Query(...)
    pus_cell: str  = Query(...)
    pus_cell_clumps: str  = Query(...)
    bacteria: str  = Query(...)
    blood_glucose_random: float = Query(...)
    blood_urea: float = Query(...)
    serum_creatinine: float = Query(...)
    sodium: float = Query(...)
    potassium: float = Query(...)
    haemoglobin: float = Query(...)
    packed_cell_volume: float = Query(...)
    white_blood_cell_count: float = Query(...)
    red_blood_cell_count: float = Query(...)
    hypertension: str  = Query(...)
    diabetes_mellitus: str  = Query(...)
    coronary_artery_disease: str  = Query(...)
    appetite: str  = Query(...)
    peda_edema: str  = Query(...)
    aanemia: str  = Query(...)