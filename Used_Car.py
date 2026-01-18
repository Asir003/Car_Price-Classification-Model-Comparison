import os
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np


from sklearn.model_selection import train_test_split, GridSearchCV, learning_curve, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder, label_binarize
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc


import joblib
import matplotlib.pyplot as plt
import seaborn as sns


try:
    plt.style.use('seaborn-v0_8-darkgrid')
except OSError:
    try:
        plt.style.use('seaborn-darkgrid')
    except OSError:
        plt.style.use('ggplot')
sns.set_palette("husl")

class CarPricePredictor:

    def __init__(self, csv_file='Used Car Dataset.csv'):
       
        self.csv_file = csv_file
        self.df = None
       
    def load_data(self):

        print("=" * 60)
        print("Loading Dataset...")
        print("=" * 60)
        
        try:
            self.df = pd.read_csv(self.csv_file)
            print(f"  Dataset loaded successfully!")
            print(f"  - Shape: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
            print(f"  - Columns: {list(self.df.columns)}")
        except FileNotFoundError:
            print(f"✗ Error: File '{self.csv_file}' not found!")
            raise
        except Exception as e:
            print(f"✗ Error loading file: {str(e)}")
            raise

    def run_complete_pipeline(self):

        print("\n" + "=" * 60)
        print("CAR PRICE CLASSIFICATION - MACHINE LEARNING PIPELINE")
        print("=" * 60)

        self.load_data()

def main():
    
    # Initialize predictor
    predictor = CarPricePredictor(csv_file='Used Car Dataset.csv')
    
    # Run complete pipeline
    predictor.run_complete_pipeline()


if __name__ == "__main__":
    main()
