from fastapi import FastAPI, HTTPException # type: ignore
from fastapi.responses import JSONResponse # type: ignore
from schema.user_input import User_Input
from schema.prediction_response import PredictionResponse
from model.predict import MODEL_VERSION, predict_output, model

app = FastAPI()

# This end point is Human Readable
@app.get('/')
def Home():
   return {'message':"Insurance Premium predictor API"}


# This end point is machine readable like aws, docker
@app.get('/health')
def health_check():
   return {'status':"OK",
           'version': MODEL_VERSION,
           'model_Loaded': model is not None}


@app.post('/predict', response_model = PredictionResponse)  #  response_model = PredictionResponse , when a predicted value comes then it validates on this model after that it give the output.
def predict_Input(data: User_Input):
   
   # This single row of data is send to the ml model.
   user_input = {
      'BMI': data.bmi,
      'age_group': data.age_group,
      'lifestyle_risk': data.lifestyle_risk,
      'city_tier': data.city_tier,
      'income_lpa': data.income_lpa,
      'occupation':data.occupation
   }

   try:
   # This try statement is used bcoz we import predict_output function from other file if it does not work or not import then it will give the required error
    prediction = predict_output(user_input)
    return JSONResponse(status_code=200, content= {'Response':prediction})
   
   except Exception as e:

      return JSONResponse(status_code = 500,content = str(e) )


    