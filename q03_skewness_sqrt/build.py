# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

# Write your Solution Here:

def skewness_sqrt(df):

    df['GrLivArea'] = np.sqrt(df['GrLivArea'])
    df['SalePrice'] = np.sqrt(df['SalePrice'])
    areaskew=skew(df['GrLivArea'])
    saleskew=skew(df['SalePrice'])
    return areaskew, saleskew
