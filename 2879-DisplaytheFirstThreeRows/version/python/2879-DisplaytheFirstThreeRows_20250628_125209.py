# Last updated: 6/28/2025, 12:52:09 PM
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)