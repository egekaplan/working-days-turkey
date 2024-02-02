import datetime
from workalendar.europe import Turkey
import pytest
from working_days_tr import count_working_days 

@pytest.fixture
def holidays():
    cal = Turkey()
    this_year = datetime.date.today().year
    holidays_list = cal.holidays(this_year)
    return [date.strftime('%Y-%m-%d') for date, _ in holidays_list]

def test_count_working_days_no_holidays():
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 1, 5)  # Assuming a 5-day work week
    holidays_list = []
    result = count_working_days(start_date, end_date, holidays_list)
    assert result == 5  

def test_count_working_days_with_holidays(holidays):
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 1, 10)
    result = count_working_days(start_date, end_date, holidays)
    assert result == 6  

