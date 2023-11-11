import numpy as np
import pandas as pd
import time

# Setting up the number of simulated users and core customer attribute variables (usage time and prior BI experience)
n = 200000
prior_bi_experience_values = [0, 1, 2]
prior_bi_experience_prob = [0.03, 0.05, 0.92]
prior_bi_experience = np.random.choice(prior_bi_experience_values, n, p=prior_bi_experience_prob)
usage_hours = np.random.uniform(0, 500, n)

# Simulating the number of publishes per user
publishes_naive = np.random.normal(10, 1, n)

# Zero out observations with associated publications
publications = []
usage_list = list(usage_hours)
publish_naive_list = list(publishes_naive)
for i in range(n):
    if usage_list[i] < 20:
        publications.append(0)
    else:
        publications.append(publish_naive_list[i])

# Simulating the number of AI modules used
ai_1yr_exp = np.random.normal(5, 1, n)
a2_more_exp = np.random.normal(15, 1, n)

# Selecting the appropriate distribution based on years of experience
ai = []
exp_list = list(prior_bi_experience)
for i in range(n):
    if exp_list[i] == 0:
        ai.append(0)
    elif exp_list[i] == 1:
        ai.append(ai_1yr_exp[i])
    else:
        ai.append(a2_more_exp[i])

# attributes
at3 = np.random.choice([0, 1, 2, 3], n, p=[0.3, 0.4, 0.1, 0.2])
at4 = np.random.normal(4, 1, n)
at5 = np.random.uniform(0, 10, n)
at6 = np.random.exponential(scale=2, size=n)  # Customer support response time

# You will need to add any attributes here
d = {
    "prior_exp": prior_bi_experience,
    "usage_hours": usage_hours,
    "publishes": publications,
    "ai": ai,
    "at3": at3,
    "at4": at4,
    "at5": at5,
    "Issue_response_time": at6
}

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
df['utility'] = utility(df['publishes'], df['ai'], df['at3'], df['at4'], df['at5'], df['Issue_response_time'])
df['conversion'] = np.where(df['utility'] > 29, 1, 0)

end_time_utility_calculation = time.time()
elapsed_time_utility_calculation = end_time_utility_calculation - start_time_utility_calculation

print(f"Time taken to calculate utility: {elapsed_time_utility_calculation} seconds")

# Save DataFrame to JSON
df.to_json("sim_data.json")
