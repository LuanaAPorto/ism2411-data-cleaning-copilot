#Sales Data Cleaning Program

#This project contains Pythons crips designed to load and clean raw sales data. The data cleaning process uses pandas library, and includes steps to standardize column names, handle data types, manage missing values and more.

#Project Structure

#ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv
│   └── processed/
│       └── sales_data_clean.csv        # created by your script
├── src/
│   └── data_cleaning.py                # your main script
├── README.md                           # short project description
└── reflection.md                       # your written explanation

#Installation and usage

#You need Python 3.x installed and pandas library
#Make sure your raw sales data filme is named correctely and located in the data/raw/ directory
#Run Python3 src/data_cleaning.py on your terminal

#Cleaning functions purpose

#load_data = loads CSV file into a pandas Dataframe
#clean_column_names = Converts column names to lowercase, strips leading whitespace, and replaces with underscores
#clean_string_columns = removes leading and trailing whitespaces from all string type columns
#clean_column_values = converts the price column to float and the quantity column to integer
#handle_missing_value = fills missing values with the median price and zeros
#remove_invalid_rows = removes rows with negative prices and quantities



