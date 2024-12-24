import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import plot_importance
import numpy as np 
import sklearn
import xgboost as xgb 
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import ElasticNet
from sklearn.svm import SVR
from pathlib import Path
from utilities import opendata,modelado_regression_lineal
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import seaborn as sns
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor

class ModelRegressorCapexValidations:
    
    def __init__(self, path_data):
        
        self.path_data = path_data
        self.dataset = self.load_dataset()
        
        
    def load_dataset(self):
        
        df = pd.read_csv(self.path_data)
        df = df[["min_year_stage_date","curationlevel","source","capacity_type","latitude", "longitude", "value","capex"]]
        Q1 = df['capex'].quantile(0.25)
        Q3 = df['capex'].quantile(0.75)
        IQR = Q3 - Q1
        df['is_outlier'] = ((df['capex'] > Q3 + 1.5 * IQR) | (df['capex'] < Q1 - 1.5 * IQR)).astype(int)
        df.reset_index(drop=True, inplace=True)
        df = pd.get_dummies(df,columns=["capacity_type"])
        df = pd.get_dummies(df,columns=["source"])
        df = pd.get_dummies(df,columns=["curationlevel"])
        df = df.dropna()
        return df
    
    def training_model_validation(self):
        
        # Dividir los datos
        y = self.dataset['capex']
        X_with_new_dummy = self.dataset.drop(["capex"], axis=1)
        X_train_new_dummy, X_val_new_dummy, y_train, y_val = train_test_split(X_with_new_dummy,
                                                                              y,
                                                                            test_size=0.2, 
                                                                            random_state=2)
        # Modelos
        models = {
            "XGBRegressor": XGBRegressor(n_estimators=1000, learning_rate=0.1, max_depth=5, random_state=1),
            "AdaBoostRegressor": AdaBoostRegressor(n_estimators=100, learning_rate=0.1, random_state=1),
            "GradientBoostingRegressor": GradientBoostingRegressor(n_estimators=800, learning_rate=0.1, max_depth=5, random_state=1),
            "RandomForestRegressor": RandomForestRegressor(n_estimators=800, max_depth=5, random_state=1),
            "ExtraTreesRegressor":ExtraTreesRegressor(n_estimators=200, max_depth=12, random_state=1)
        }

        # Entrenar y evaluar
        results = {}
        for name, model in models.items():
            # Entrenar el modelo
            model.fit(X_train_new_dummy, y_train)
            
            # Predecir
            y_pred = model.predict(X_val_new_dummy)
            
            # Calcular MAE
            mae = mean_absolute_error(y_val, y_pred)
            results[name] = mae
            print(f"MAE for {name}: {mae}")

        # Resultados
        print("\nResumen de MAE:")
        for model_name, mae in results.items():
            print(f"{model_name}: {mae}")
        