#1
from datetime import datetime, timedelta
x = datetime.now()
d = x - timedelta(days=5)
print('Current day:', x)
print('Substracted day:', d)

'''
from datetime import datetime, timedelta
x = datetime.now()
d = x - timedelta(days=5)
print('Current day:', x.strftime('%d %B %Y'))
print('Substracted day:', d.strftime('%d %B %Y'))
'''

#2
from datetime import datetime, timedelta
x = datetime.now()
d = x - timedelta(days=1)
s = x + timedelta(days=1)
print('Yesterday', d)
print('Today:', x)
print('Tomorrow:', s)

#3
from datetime import datetime, timedelta
x = datetime.now()
print(x.strftime('%Y-%m-%d %H:%I:%S'))

#4
from datetime import datetime
day1 = datetime.now()
day2= datetime.strptime('15 Feb 2024, 10:00:00', "%d %b %Y, %H:%M:%S")
subst = (day1 - day2).total_seconds()
print("Today:", datetime.now())
print("Choosen date:", day2)
print("Difference in seconds:", subst)