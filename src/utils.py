import os
import sys
import pandas as pd
import numpy as np
import dill
from sklearn.metrics import r2_score

def save_object(file_path, obj):

    try: 
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except:
        pass


def evaluate_model(X_train, X_test, y_train, y_test, models):

    print("In Utils")

    try: 

        report = {}

        for i in range(len(list(models))):
            model = list (models.values())[i]

            print(model)
            model.fit(X_train, y_train) #Training the model after fitting data

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(y_test)

            train_model_score = r2_score(y_train, y_train_pred)


            test_model_score = r2_score(X_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

            # print(report)


        return report


    except:
        pass