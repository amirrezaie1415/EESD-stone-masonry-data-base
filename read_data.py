import pandas as pd

def read_data():
    df = pd.read_excel('data/StoneMasonryDatabase.xls', index_col=None)
    return df

