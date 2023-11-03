from datetime import date, datetime, timedelta

today  = date.today()
dt = datetime.now()
print(today)
print(dt)

formatted_date = today.strftime("%a, %d %B %Y ") # Thurs, 25 Nov 2018 10.53 pm
print(formatted_date)

ten_days_ago = today - timedelta(days=10)
print(ten_days_ago)

date_string = "2012-09-01"
date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
print(date_object)
# "2012- 09-01" How to convert a date string to date
# "1999-01-31" "2005-11-13" find how days are in between the two dates, how many weeks

date_format = "%Y-%m-%d"

date_string1 = "1999-01-31"
date_string2 = "2005-11-13"

date1 = datetime.strptime(date_string1, date_format)
date2 = datetime.strptime(date_string2, date_format)

# Calculate the difference in days
difference = abs((date2 - date1).days)

print(f"There are {difference} days between {date_string1} and {date_string2}.")