from datetime import datetime

curr_year = datetime.now().year
year_limit = curr_year if datetime.now().month == 12 else curr_year - 1
YEARS = [str(year) for year in range(2015, year_limit + 1)]
YEARS.reverse()
