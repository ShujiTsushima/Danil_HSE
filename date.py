from datetime import datetime, timedelta
def date_range(start_date, end_date):
  if start_date > end_date:
    return " "
  else:
    start_date_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    current_dt = start_date_datetime
    days = []
    while current_dt <= end_date_datetime:
      days.append(current_dt.strftime('%Y-%m-%d'))
      current_dt += timedelta(days=1)
    return days

print(date_range('2022-01-01', '2022-01-03'))
print(date_range('2022-01-03', '2022-01-01'))