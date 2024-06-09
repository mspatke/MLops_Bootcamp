import pytest
from pathlib import Path
import os
import sys

#adding the below path to avoid module not found error
PACKAGE_ROOT =  Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions

#output from predict is not null
#output from predict script is str data type
#the output is Y for an example data

#Fixtures --> functions before test funstion --> ensure single_predictions

@pytest.fixture
def single_predictions():
    test_dataset = load_dataset(config.TEST_FILE)
    

