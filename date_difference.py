from dateutil import parser, relativedelta
from dateutil.parser import ParserError


def date_difference(date_1: str, date_2: str) -> str:
    try:
        date_difference = relativedelta.relativedelta(
            parser.parse(date_2, dayfirst=True), parser.parse(date_1, dayfirst=True)
        )
        return f"{date_difference.years} years, {date_difference.months} months, {date_difference.days} days"
    except ParserError:
        return "Error computing the date difference. Please input a valid date format."


print(date_difference("1st Jan 2020", "2nd Feb 2019"))
