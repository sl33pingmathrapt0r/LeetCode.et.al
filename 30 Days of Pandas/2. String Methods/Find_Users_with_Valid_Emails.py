import pandas as pd
import re   #  regex module

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    df= users[users['mail'].str.match(r"^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$")]
    return df
