import pandas as pd

def csv_pandas():
    csv_path = "src/csv/vgsales.csv"

    df = pd.read_csv(csv_path)
    print(df.head(25))
