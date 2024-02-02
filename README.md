# Working Days Calculator

This Python script calculates the number of working days (business days) in each month of the current year for Turkey. It takes into account the official holidays in Turkey and excludes weekends (Saturdays and Sundays) from the count. The script uses the `workalendar` library to retrieve the list of holidays for the specified year.

## Prerequisites

Before running the script, make sure you have `poetry` installed. You can install it using pip:

```bash
pip install poetry
```

## Usage

1. Import the required libraries with `poetry install` and define the `count_working_days` function, which calculates the working days between two dates, excluding holidays and weekends.

2. Retrieve today's date and the current year.

3. Initialize the Turkey calendar using `workalendar`.

4. Get the list of official holidays for the current year and format them as strings in the 'YYYY-MM-DD' format.

5. Iterate through each month of the year, calculating the number of working days for that month using the `count_working_days` function. Adjustments are made for January to account for the fact that the 2nd of January is not observed as a holiday in Turkey.

6. Run the code with `poetry run python3 working_days_tr.py`. Print the number of working days for each month and the total number of working days for the current year.

## Output

The script will output the number of working days for each month and the total working days for the current year. This information can be useful for various business and scheduling purposes.

## Note

- This script assumes that weekends are Saturdays and Sundays. You can modify the `count_working_days` function to consider different weekend days if needed.

- Ensure that the official holidays in Turkey are correctly defined in the `workalendar` library for accurate results.

- The script is tailored for the year in which it is executed. If you want to calculate working days for a different year, simply update the `ThisYear` variable with the desired year.

Feel free to adapt and customize this script for your specific needs or integrate it into other projects where you need to calculate working days.
