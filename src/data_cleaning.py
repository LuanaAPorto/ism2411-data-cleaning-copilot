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

#This code will standardize column names (for example, lowercase and underscores).

def clean_column_names(df:pd.DataFrame) -> pd.DataFrame:
    """Standardize column names to lowercase with underscores."""
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df


