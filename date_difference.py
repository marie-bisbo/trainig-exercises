from dateutil import parser, relativedelta


def date_difference(date_1: str, date_2: str) -> str:
    date_difference = relativedelta.relativedelta(
        parser.parse(date_2, dayfirst=True), parser.parse(date_1, dayfirst=True)
    )
    return f"{date_difference.years} years, {date_difference.months} months, {date_difference.days} days"


print(date_difference("01/01/2020", "13/02/2020"))
