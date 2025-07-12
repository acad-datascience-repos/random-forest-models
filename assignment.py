from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_random_forest_on_wine():
  """
  Trains a RandomForestClassifier on the Wine dataset and returns its accuracy.

  Returns:
    The accuracy of the model on the test set.
  """
  # Task 1: Load the Wine dataset
  wine = None
  X, y = (None, None)
  # Your code here

  # Task 2: Split the data
  X_train, X_test, y_train, y_test = (None, None, None, None)
  # Your code here

  # Task 3: Create and train the model
  model = None
  # Your code here

  # Task 4: Make predictions and calculate accuracy
  predictions = None
  accuracy = None
  # Your code here

  return accuracy
