# Write a function `conversionsFromCsv()` that can take a CSV file path as
#  * input and return the total number of conversions recorded in that csv.
#  * The csv files will be of the form:
#  *
#  * Cost,Conversions,Clicks,...
#  * 10,2,50,...
#  * ...
#  *
#  * The order of the headers may vary between CSVs. The function should throw an
#  * Exception if the input is invalid in some way.
#  */
import pandas as pd


def conversions_from_csv(filepath: str):
    df = pd.read_csv(filepath)
    try:
        return sum(df.Conversions)
    except AttributeError:
        return "Unable to make computations. The dataframe does not have a conversions column."


print(conversions_from_csv("data.csv"))
