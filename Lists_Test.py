"""
Lists and Iterating
"""

spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low_spendings = 0
normal_spendings = 0
high_spendings = 0

for month in spendings:
    if month < 1000:
        low_spendings += 1
    elif month <= 2500:
        normal_spendings += 1
    else:
        high_spendings += 1
print("Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.".format(low_spendings, normal_spendings, high_spendings))
