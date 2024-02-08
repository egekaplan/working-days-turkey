import datetime
from workalendar.europe import Turkey
import pytest
from src.working_days_project.working_days_tr import count_working_days
from loguru import logger  # Import Loguru's logger


@pytest.fixture
def holidays():
    cal = Turkey()
    this_year = datetime.date.today().year
    holidays_list = cal.holidays(this_year)
    return [date.strftime("%Y-%m-%d") for date, _ in holidays_list]


def test_count_working_days_no_holidays():
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 1, 5)
    holidays_list = []
    result = count_working_days(start_date, end_date, holidays_list)
    assert result == 5


def test_count_working_days_with_holidays(holidays):
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 1, 10)
    result = count_working_days(start_date, end_date, holidays)
    assert result == 7  # Updated to reflect the adjustment in working_days_tr.py


# Configure Loguru logger
logger.add("tests.log", rotation="500 MB", level="INFO")

# Uncomment the lines below if you want to log information during the tests
# logger.info("Logging test information")
# logger.error("Logging test error")
# logger.warning("Logging test warning")
