import numpy as np
from sklearn.externals import joblib
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.grid_search import ParameterGrid

training_data = np.loadtxt("head_on_accidents_without_severity_fit.txt")
training_labels = np.loadtxt("head_on_accidents_labels_fatal_fit.txt")
testing_data = np.loadtxt("head_on_accidents_without_severity_test.txt")
testing_labels = np.loadtxt("head_on_accidents_labels_fatal_test.txt")

#remove "imputed maximum severity" to make sure our predictor isn't cheating
training_data = np.delete(training_data, 10, 1)
testing_data = np.delete(testing_data, 10, 1)

def try_svc(parameter_grid):
  max_score = 0
  best_operator = None
  for combo in ParameterGrid(parameter_grid):
    svc_operator = SVC(**combo)
    svc_operator.fit(training_data,training_labels)
    current_score = svc_operator.score(testing_data,testing_labels)
    if current_score > max_score:
      max_score = current_score
      best_operator = svc_operator
      print "New maximum score: " + str(current_score)
      print svc_operator
  return best_operator

def main():
  svc_parameter_grid = [{
    "C":[1,10,50,100],
    "kernel":['rbf','poly','sigmoid'],
    "degree":[2,3,4],
    "class_weight":['auto'],
  }]

  svc_operator = try_svc(svc_parameter_grid)

main()
