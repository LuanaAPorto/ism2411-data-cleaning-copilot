#import pandas 
import pandas as pd

#Load sales_data_raw.csv from data/raw/

def load_data(file_path:str):
    """Load data from a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return pd.DataFrame

#Clean the data
#Github Copilot was used in all the code below

#This code will standardize column names, change all letters to lowercase,replace spaces with underscores and removes leading whitespace.
#This is to avoid issues when accessing colums later on

def clean_column_names(df:pd.DataFrame) -> pd.DataFrame:                
    """Standardize column names to lowercase with underscores."""
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_') #removes leading whitespace, converts to lowercase, replaces spaces with underscores
    return df #returns the modified dataframe


#This code will handle missing prices and quantities (dropping or/and filling strategies) — but be consistent). Handle NaN values in 'price' and 'quantity' columns
#This is because it can't do any calculations with missing values

def handle_missing_values(df:pd.DataFrame) -> pd.DataFrame:
    """Handle missing values in 'price' and 'quantity' columns."""
    df_modified = df.copy() #create a copy of the dataframe to avoid modifying the original
    df_modified['price'].fillna(df['price'].median(), inplace=True) #fill NaN in price with median
    df_modified['quantity'].fillna(0, inplace=True) #fill NaN in quantity with 0
    return df_modified #returns the modified dataframe

#This code will remove rows that have invalid data ( negative prices or quantities )
#This is because these values don't make sense, and were definetely entered incorrectly, so we shouldn't use them in our analysis

def remove_invalid_rows(df:pd.DataFrame) -> pd.DataFrame:
    """Remove rows with negative 'price' or 'quantity'."""
    df_modified = df[(df['price'] >= 0) & (df['quantity'] >= 0)] #filter out rows with negative price or quantity
    return df_modified #returns the modified dataframe


