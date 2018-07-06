from datetime import *

now=datetime.today()
print(now)

t=time(5,45,30)
print (t)

print ("hour:\t",t.hour)
print ("minutes:",t.minute)
print ("seconds:",t.second)

d = date(2020,6,3)
print(d)


print ("day:\t",d.day)
print ("Month:\t",d.month)
print ("Year:",d.year)



"""OUTPUT:
2018-07-05 11:22:41.741626
05:45:30
hour:	 5
minutes: 45
seconds: 30
2020-06-03
day:	 3
Month:	 6
Year: 2020
"""
