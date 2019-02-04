import pandas as pd
import numpy as np
import utils as ut
from IPython.display import display

input_file = "titanic_data.csv"


full_data = pd.read_csv(input_file)
outcomes = full_data['Survived']
display(full_data.head())

#base_prediction = ut.base_predictions(full_data)
print("Accuracy for base prediction is {}".format(ut.accuracy_score(outcomes, ut.base_predictions(full_data))))

#predictions_iter1 = ut.predictions_iter1(full_data)
print("Accuracy for female added  is {}".format(ut.accuracy_score(outcomes, ut.predictions_iter1(full_data))))

#predictions_iter2 = ut.predictions_iter2(full_data)
print("Accuracy for female + male less than 10 years old is {}".format(ut.accuracy_score(outcomes, ut.predictions_iter2(full_data))))
