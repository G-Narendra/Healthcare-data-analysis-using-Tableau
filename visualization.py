import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load cleaned data
train_df = pd.read_csv('cleaned_train_healthcare_data.csv')

# Display the first few rows and column info
print(train_df.head())
print(train_df.info())

# 1. Histogram for Patient Age Distribution
if 'patient_age' in train_df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(train_df['patient_age'], bins=20, kde=False, color='blue')
    plt.title('Patient Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Number of Patients')
    plt.show()
else:
    print("The column 'patient_age' does not exist in the dataframe.")

# 2. Histogram for Household Income Distribution
if 'income_household_median' in train_df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(train_df['income_household_median'], bins=20, kde=True, color='green')
    plt.title('Household Income Distribution')
    plt.xlabel('Median Household Income')
    plt.ylabel('Number of Households')
    plt.show()
else:
    print("The column 'income_household_median' does not exist in the dataframe.")

# 3. Bar Chart for Education Levels
education_columns = [
    'education_less_highschool', 'education_highschool', 'education_some_college',
    'education_bachelors', 'education_graduate', 'education_stem_degree'
]

# Check if all education columns exist
if all(col in train_df.columns for col in education_columns):
    education_data = train_df[education_columns].sum().reset_index()
    education_data.columns = ['Education Level', 'Count']
    
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Count', y='Education Level', data=education_data, palette='viridis')
    plt.title('Education Levels in the Dataset')
    plt.xlabel('Count')
    plt.ylabel('Education Level')
    plt.show()
else:
    print("One or more of the education columns do not exist in the dataframe.")

# 4. Heatmap for Correlation Analysis
# Select only numeric columns for correlation
numeric_columns = train_df.select_dtypes(include=[float, int]).columns

plt.figure(figsize=(14, 10))
correlation_matrix = train_df[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
