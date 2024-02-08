import datetime
from workalendar.europe import Turkey


def count_working_days(start_date, end_date, formatted_holidays):
    current_date = start_date
    working_days = 0

    while current_date <= end_date:
        formatted_current_date = current_date.strftime("%Y-%m-%d")
        if (
            current_date.weekday() < 5
            and formatted_current_date not in formatted_holidays
        ):
            working_days += 1
        current_date += datetime.timedelta(days=1)

    return working_days


today = datetime.date.today()
ThisYear = today.year

cal = Turkey()

# Get the list of holidays
holidays = cal.holidays(ThisYear)
formatted_holidays = [date.strftime("%Y-%m-%d") for date, _ in holidays]

# Calculate and print the number of working days for each month
total_working_days = 0
subtracted_holiday = False  # We need to exclude the 2nd of January as a holiday since it is not observed in Turkey, contrary to the information in the holiday calendar library

for month in range(1, 13):
    start_date = datetime.date(ThisYear, month, 1)
    last_day = (
        31
        if month in [1, 3, 5, 7, 8, 10, 12]
        else (
            30
            if month != 2
            else (
                29
                if ThisYear % 4 == 0 and (ThisYear % 100 != 0 or ThisYear % 400 == 0)
                else 28
            )
        )
    )
    end_date = datetime.date(ThisYear, month, last_day)

    working_days_in_month = count_working_days(start_date, end_date, formatted_holidays)

    if month == 1 and not subtracted_holiday:
        # Subtract one holiday from January
        working_days_in_month += 1
        subtracted_holiday = True

    total_working_days += working_days_in_month

    month_name = start_date.strftime("%B")

    # print the number of working days for each and every month
    print(f"{month_name}: {working_days_in_month}")

# Print the total number of working days for current year
print(f"Total working days: {total_working_days}")
