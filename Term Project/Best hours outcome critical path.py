import pandas as pd
import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize, lpSum
#These are a highlevel view of the tasks needed to complete the anticancer drug discovery along with their time and cost estimates
expected_tasks = {
    'T2': {'duration': 19, 'cost': 19000},
    'T3': {'duration': 49, 'cost': 49000},
    'T4': {'duration': 1, 'cost': 1000},
    'T5': {'duration': 2, 'cost': 2000},
    'T6': {'duration': 20, 'cost': 20000},
    'T7': {'duration': 12, 'cost': 12000},
    'T8': {'duration': 1, 'cost': 1000},
    'T9': {'duration': 38, 'cost': 38000},
    'T10': {'duration': 62, 'cost': 62000},
    'T11': {'duration': 2, 'cost': 3000},
    'T12': {'duration': 90, 'cost': 90000},
    'T13': {'duration': 72, 'cost': 7200},
    'T14': {'duration': 120, 'cost': 12000},
    'T15': {'duration': 150, 'cost': 200000},
    'T16': {'duration': 120, 'cost':120000},
    'T17': {'duration': 240, 'cost': 240000}
}
#Tasks dependent on preceding tasks to be completed before beginning
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
# Print the results-Identifies tasks that start at time 0 (tasks that are at the beginning of the project) and then finds the maximum end time among these tasks
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
