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

#This code will convert key columns to the correct numeric types ( price to float, quantity to int )
#This is because these columns will be used in calculations later on, and need to be in the correct format
def clean_column_values(df:pd.DataFrame) -> pd.DataFrame:
    """Convert 'price' to float and 'quantity' to int."""
    df_modified = df.copy() #create a copy of the dataframe to avoid modifying the original
    df_modified['price'] = pd.to_numeric(df_modified['price'], errors='coerce') #convert price to float, set errors to NaN
    df_modified['quantity'] = pd.to_numeric(df_modified['quantity'], errors='coerce').astype('Int64') #convert quantity to int, set errors to NaN
    return df_modified #returns the modified dataframe


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

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())