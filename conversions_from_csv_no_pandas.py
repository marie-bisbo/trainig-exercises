import csv


def conversions_from_csv(filepath: str):
    with open(filepath, newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        try:
            return sum([int(row["Conversions"]) for row in csv_reader])
        except KeyError:
            return "No column conversions in the csv file"


print(conversions_from_csv("data.csv"))
