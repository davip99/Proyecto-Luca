import pandas as pd


def csv_pandas():
    """
    Carga los jeugos desde pandas
    """
    csv_path = "src/csv/vgsales.csv"

    df = pd.read_csv(csv_path)
    print(df.head(25))
