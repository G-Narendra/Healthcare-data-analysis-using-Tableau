import pandas as pd

# Load the datasets
train_df = pd.read_csv('train_clean.csv')
test_df = pd.read_csv('test_clean.csv')

# Inspect the data
print("Train DataFrame Head:")
print(train_df.head())
print("\nTrain DataFrame Info:")
print(train_df.info())

print("\nTest DataFrame Head:")
print(test_df.head())
print("\nTest DataFrame Info:")
print(test_df.info())

# Data Cleaning
# Remove rows with NaN values in both datasets
train_df = train_df.dropna()
test_df = test_df.dropna()

# Convert columns to appropriate data types if needed
# Assuming columns like 'Admission Date' and 'Discharge Date' exist
if 'Admission Date' in train_df.columns and 'Discharge Date' in train_df.columns:
    train_df['Admission Date'] = pd.to_datetime(train_df['Admission Date'])
    train_df['Discharge Date'] = pd.to_datetime(train_df['Discharge Date'])
if 'Admission Date' in test_df.columns and 'Discharge Date' in test_df.columns:
    test_df['Admission Date'] = pd.to_datetime(test_df['Admission Date'])
    test_df['Discharge Date'] = pd.to_datetime(test_df['Discharge Date'])

# Calculate the length of stay if the columns exist
if 'Admission Date' in train_df.columns and 'Discharge Date' in train_df.columns:
    train_df['Length of Stay'] = (train_df['Discharge Date'] - train_df['Admission Date']).dt.days
if 'Admission Date' in test_df.columns and 'Discharge Date' in test_df.columns:
    test_df['Length of Stay'] = (test_df['Discharge Date'] - test_df['Admission Date']).dt.days

# Save the cleaned data
train_df.to_csv('cleaned_train_healthcare_data.csv', index=False)
test_df.to_csv('cleaned_test_healthcare_data.csv', index=False)

print("Data cleaning and preparation complete. Cleaned data saved to 'cleaned_train_healthcare_data.csv' and 'cleaned_test_healthcare_data.csv'.")
