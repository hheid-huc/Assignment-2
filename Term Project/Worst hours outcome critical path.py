import pandas as pd
import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize, lpSum

expected_tasks = {
    'T2': {'duration': 25, 'cost': 25000},
    'T3': {'duration': 60, 'cost': 60000},
    'T4': {'duration': 5, 'cost': 5000},
    'T5': {'duration': 10, 'cost': 10000},
    'T6': {'duration': 30, 'cost': 300000},
    'T7': {'duration': 20, 'cost': 20000},
    'T8': {'duration': 5, 'cost': 5000},
    'T9': {'duration': 50, 'cost': 50000},
    'T10': {'duration': 75, 'cost': 75000},
    'T11': {'duration': 6, 'cost': 6000},
    'T12': {'duration': 200, 'cost': 200000},
    'T13': {'duration': 90, 'cost': 90000},
    'T14': {'duration': 180, 'cost': 180000},
    'T15': {'duration': 220, 'cost': 220000},
    'T16': {'duration': 600, 'cost':600000},
    'T17': {'duration': 360, 'cost': 360000}
}
expected_tasks_list = list(expected_tasks.keys())
precedences = {'T2':[],
               'T3': [],
               'T4': ['T3'],
               'T5':['T2', 'T4'],
               'T6': ['T4'],
               'T7': ['T4'],
               'T8': [],
               'T9': ['T6', 'T7'],
               'T10':['T9'],
               'T11': ['T9'],
               'T12': [],
               'T13': ['T10'],
               'T14': ['T13'],
               'T15': ['T14'],
               'T16': ['T15'],
               'T17': ['T16']
               }


# create the LP problem
prob_exp2 = LpProblem("Critical_Path", LpMinimize)
start_times_expected = {task: LpVariable(f"start_{task}", 0, None) for task in expected_tasks_list}
end_times_expected = {task: LpVariable(f"end_{task}", 0, None) for task in expected_tasks_list}

for task in expected_tasks_list:
    prob_exp2 += end_times_expected[task] == start_times_expected[task] + expected_tasks[task]['duration'], f"{task}_duration"
    for predecessor in precedences[task]:
        prob_exp2 += start_times_expected[task] >= end_times_expected[predecessor],f"{task}_predecessor_{predecessor}"

prob_exp2 += lpSum([end_times_expected[task] for task in expected_tasks_list])

status = prob_exp2.solve()
# Print the results
print("Critical Path time for Expected Time Estimates:")
critical_path_tasks = [task for task in expected_tasks_list if value(start_times_expected[task]) == 0]
critical_path_end_time = max([value(end_times_expected[task]) for task in critical_path_tasks])

for task in critical_path_tasks:
    print(f"{task} is on the critical path and ends at {critical_path_end_time} hours in duration")

# Print solution
print("\nSolution variable values:")
for var in prob_exp2.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)