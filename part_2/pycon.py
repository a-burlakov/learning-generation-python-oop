import calendar
import datetime

input_list = [i.strip() for i in open(0)]

year = int(input_list[0])
month = int(input_list[1])

weeks = calendar.monthcalendar(year, month)
if weeks[0][3] == 0:
    thursday_day = weeks[4][3]
else:
    thursday_day = weeks[3][3]

date = datetime.date(year, month, thursday_day)
print(date.strftime("%d.%m.%Y"))
