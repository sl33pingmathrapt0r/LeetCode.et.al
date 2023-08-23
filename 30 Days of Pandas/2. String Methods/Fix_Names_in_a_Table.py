import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name']= users['name'].str.capitalize()   # capitalize affects only first char in string
    return users.sort_values(by=['user_id'])
