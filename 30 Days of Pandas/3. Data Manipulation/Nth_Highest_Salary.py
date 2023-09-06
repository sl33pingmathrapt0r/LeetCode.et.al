import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries= employee["salary"].drop_duplicates().sort_values(ascending=False)
    if len(salaries)<N: return pd.DataFrame({'getNthHighestSalary({i})'.format(i=N): [None]})
    return pd.DataFrame({'getNthHighestSalary({i})'.format(i=N): salaries.iloc[[N-1]]})
