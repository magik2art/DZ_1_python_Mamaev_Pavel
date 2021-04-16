# -*- coding: utf8 -*-

duration = input("input second ")
time = ["second", "minut", "hour", "day", "month", "year"]
sec = 1
minut = sec * 60
hour = minut * 60
day = hour * 24
mounth = day * 30
year = mounth * 12

if duration > (year - 1):
    print duration / year, time[5], (duration % year) / mounth, time[4], (duration % mounth) / day, time[3], (duration % day) / hour, time[2], (duration % hour) / minut, time[1], (duration % minut), time[0]
elif duration > (mounth - 1):
    print duration / mounth, time[4], (duration % mounth) / day, time[3], (duration % day) / hour, time[2], (duration % hour) / minut, time[1], (duration % minut), time[0]
elif duration > (day - 1):
    print duration / day, time[3], (duration % day) / hour, time[2], (duration % hour) / minut, time[1], (duration % minut), time[0]
elif duration > (hour - 1):
    print duration / hour, time[2], (duration % hour) / minut, time[1], (duration % minut), time[0]
elif duration > (minut - 1):
    print (duration / (minut*sec)), time[1], (duration % minut), time[0]
else:
    print duration, time[0]
