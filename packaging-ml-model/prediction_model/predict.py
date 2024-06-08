import pandas as pd
import numpy as np
from prediction_model.config import config
from prediction_model.processing.data_handling import load_pipeline,load_datasets

classification_pipeline = load_pipeline(config.MODEL_NAME)

# def generate_prediction(input_data):
#     data = pd.DataFrame(input_data)
#     prediction = classification_pipeline.predict(data[config.FEATURES])
#     output = np.where(prediction==1,'Y','N')
#     result = {"predictions":output}

#     return result

def generate_prediction():
    test_data=load_datasets(config.TEST_FILE)
    prediction = classification_pipeline.predict(test_data[config.FEATURES])
    output = np.where(prediction==1,'Y','N')
    # result = {"predictions":output}

    return output

if __name__=='__main__':
    generate_prediction()