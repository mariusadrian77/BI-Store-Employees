import pandas as pd

# Load the provided files into pandas dataframes
employee_data_path = '/workspaces/AnalitiQs-Assignment/employee_data.xlsx'
stores_data_path = '/workspaces/AnalitiQs-Assignment/stores.xlsx'
stores_ltm_data_path = '/workspaces/AnalitiQs-Assignment/stores_ltm.xlsx'

# Reading the files
employee_data = pd.read_excel(employee_data_path, nrows=5)
stores_data = pd.read_excel(stores_data_path, nrows=5)
stores_ltm_data = pd.read_excel(stores_ltm_data_path, nrows=5)

# Displaying the first few rows of each dataframe to understand the structure
employee_data_preview = employee_data.head()
stores_data_preview = stores_data.head()
stores_ltm_data_preview = stores_ltm_data.head()

# print(employee_data.head(), '\n', stores_data.head(), '\n', stores_ltm_data.head())


# Check for duplicates and missing values in employee_data
employee_data_duplicates = employee_data.duplicated().sum()
employee_data_missing = employee_data.isnull().sum()

# Check for duplicates and missing values in stores_data
stores_data_duplicates = stores_data.duplicated().sum()
stores_data_missing = stores_data.isnull().sum()

# Check for duplicates and missing values in stores_ltm_data
stores_ltm_data_duplicates = stores_ltm_data.duplicated().sum()
stores_ltm_data_missing = stores_ltm_data.isnull().sum()

# Summarize results
print(employee_data_duplicates, '\n',
      employee_data_missing.sum(), '\n',
      stores_data_duplicates, '\n',
      stores_data_missing.sum(), '\n',
      stores_ltm_data_duplicates, '\n',
      stores_ltm_data_missing.sum()
)
