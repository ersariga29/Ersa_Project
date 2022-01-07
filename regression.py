#library
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
#dataset 
X= np.array([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]).reshape((-1, 1))
Y= np.array([18184,19128,15758,17540,18792,18994,19024,18823,19127,13382,14719,15377,12885,13977,13312])
#call model regression
model = LinearRegression().fit(X,Y)
#save model
filename = 'model.sav'
joblib.dump(model, filename)
#load model
loaded_model = joblib.load(filename)
#prediction model
loaded_model.predict(20)