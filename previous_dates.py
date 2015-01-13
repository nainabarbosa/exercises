>>> dt = datetime.datetime(2015,1,13,12,30)
>>> days = 3

>>> for n in range(1, days+1):
...     #GET PREVIOUS DATES
...     previous = dt-datetime.timedelta(days=n)
...     print previous
...
2015-01-12 12:30:00
2015-01-11 12:30:00
2015-01-10 12:30:00
>>>
