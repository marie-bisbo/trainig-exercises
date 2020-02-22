import pandas as pd


def conversions_from_csv(filepath: str):
    df = pd.read_csv(filepath)
    try:
        return sum(df.Conversions)
    except AttributeError:
        return "Unable to make computations. The dataframe does not have a conversions column."


print(conversions_from_csv("data.csv"))
