import sklearn # type: ignore
import pickle
import pandas as pd # type: ignore


# import ml model
with open('model/model.pkl','rb') as f: # rb -> read binary
    model = pickle.load(f)


# In Ideal case Model version come  from MLflow.
MODEL_VERSION = '1.0.0'


# def predict_output(user_input : dict):
#     input_df = pd.DataFrame([user_input])
#     output = model.predict(input_df)[0]


#     return output


# Get  All class labels (high, medium, low) from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    # Predict the class
    predicted_class = model.predict(df)[0]

    # Get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)            

    # we will able to do that, it is bcoz we use random forest where we can get predict_proba function which gives probability of all the classes.
    
    # Create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }