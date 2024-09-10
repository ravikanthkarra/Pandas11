import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # result = employees.merge(employee_uni, on = 'id', how = 'left')
    # return result[['unique_id', 'name']]
    return employees.merge(employee_uni, on = 'id', how = 'left')[['unique_id', 'name']]