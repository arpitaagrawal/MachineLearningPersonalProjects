
## truth : the outcome column extracted from the training dataset
## pred : the predicted value retreived from the model for the dataset
def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """
    
    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred): 
        
        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"


# Base prediction, we are going to make a 0 prediction for every passenger
def base_predictions(data):

	predictions = []
	for _, passenger in data.iterrows():
		predictions.append(0)

	return predictions



def predictions_iter1(data):

	predictions = []
	for _, passenger in data.iterrows():
		if(passenger['Sex'] == "female"):
			predictions.append(1)
		else:
			predictions.append(0)

	return predictions


def predictions_iter2(data):

	predictions = []
	for _, passenger in data.iterrows():
		if(passenger['Sex'] == "female"):
			predictions.append(1)
		elif(passenger['Sex']== "male" and passenger['Age'] <= 10):
			predictions.append(1)
		else:
			predictions.append(0)

	return predictions

