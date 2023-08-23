import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Solution 1
    # preferred since .loc and .str benefit from vectorization (on entire df), 
    # while .apply() is sequential
    employees['bonus']=0
    employees.loc[
        (employees['employee_id'] %2) &
        (~employees['name'].str.startswith('M')), 
        'bonus'
    ] = employees['salary']

    return employees[['employee_id','bonus']].sort_values(by='employee_id')

    # Solution 2
    # employees['bonus']= employees.apply(
    #     lambda row: 
    #     row['salary'] if (row['employee_id']%2 and not row['name'].startswith('M')) else 0, 
    #     axis=1
    # )

    # return employees[['employee_id','bonus']].sort_values(by='employee_id')
