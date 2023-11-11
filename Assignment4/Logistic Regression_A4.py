import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import time

# Setting up number of simulated users and core customer attribute variables (usage time and prior BI experience)
n = 200000
prior_bi_experience_values = [0, 1, 2]
prior_bi_experience_prob = [0.03, 0.05, 0.92]
prior_bi_experience = np.random.choice(prior_bi_experience_values, n, p=prior_bi_experience_prob)
usage_hours = np.random.uniform(0, 500, n)

# First assume all users exceed 20 usage hours
publishes_naive = np.random.normal(10, 1, n)

# Zero out observations with associated publications
publications = np.where(usage_hours < 20, 0, publishes_naive)

# Simulating the number of AI modules used
ai_1yr_exp = np.random.normal(5, 1, n)
a2_more_exp = np.random.normal(15, 1, n)

# Selecting the appropriate distribution based on years of experience
ai = np.where(prior_bi_experience == 0, 0, np.where(prior_bi_experience == 1, ai_1yr_exp, a2_more_exp))

# Simulating additional attributes
at3 = np.random.choice([0, 1, 2, 3], n, p=[0.3, 0.4, 0.1, 0.2])
at4 = np.random.normal(4, 1, n)
at5 = np.random.uniform(0, 10, n)
at6 = np.random.exponential(scale=2, size=n)  # Customer support response time

# Creating the DataFrame
d = {
    "prior_exp": prior_bi_experience,
    "usage_hours": usage_hours,
    "publishes": publications,
    "ai": ai,
    "at3": at3,
    "at4": at4,
    "at5": at5,
    "issue_response_time": at6
}
df = pd.DataFrame(d)

# Creating the utility function
def utility(a1, a2, a3, a4, a5, a6):
    return a1 + a2 + 0.5 * a3 + 0.5 * a4 + 0.25 * a5 + a6
# Calculating utility and conversion
df['utility'] = utility(df['publishes'], df['ai'], df['at3'], df['at4'], df['at5'], df['issue_response_time'])
df['conversion'] = np.where(df['utility'] > 29, 1, 0)

# Feature matrix and target variable
X = df[['usage_hours', 'publishes', 'ai', 'at3', 'at4', 'at5', 'issue_response_time']]
y = df['conversion']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a logistic regression model
model = LogisticRegression()

# Fitting the model on the training data
model.fit(X_train, y_train)

# Predicting on the test data
y_pred = model.predict(X_test)


# Measure the time it takes to create the DataFrame
start_time_df_creation = time.time()

# Creating the DataFrame
df = pd.DataFrame(d)

end_time_df_creation = time.time()
elapsed_time_df_creation = end_time_df_creation - start_time_df_creation

print(f"Time taken to create DataFrame: {elapsed_time_df_creation} seconds")

# attributes
def utility(a1, a2, a3, a4, a5, a6):
    return a1 + a2 + 0.5 * a3 + 0.5 * a4 + 0.25 * a5 + a6

# Measure the time it takes to calculate utility
start_time_utility_calculation = time.time()

# Calculating utility
df['utility'] = utility(df['publishes'], df['ai'], df['at3'], df['at4'], df['at5'], df['issue_response_time'])
df['conversion'] = np.where(df['utility'] > 29, 1, 0)

end_time_utility_calculation = time.time()
elapsed_time_utility_calculation = end_time_utility_calculation - start_time_utility_calculation

print(f"Time taken to calculate utility: {elapsed_time_utility_calculation} seconds")

# Save DataFrame to JSON
df.to_json("sim_data.json")

