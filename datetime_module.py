import datetime
from datetime import date
bugun = (date.today)()
print(bugun)
dun = date(2023, 9, 13)
print(dun)
print(bugun - dun)
yarin = bugun + datetime.timedelta(days = 1)
print(yarin)
zaman_araligi = bugun - dun
print(zaman_araligi.days)
print(dun < bugun)
print(bugun.year)
print(bugun.month)
print(bugun.day)
print(bugun.__getattribute__('day'))
print(date.isocalendar(bugun))
print(date.weekday(bugun))
print(date.ctime(bugun))
from datetime import time
zaman = time(21,15,5)
print(zaman)
print(zaman.hour)
print(zaman.minute)
print(zaman.second)
dt = datetime.datetime(2020,10,21,11,5,3)
print(dt)
print(dt.hour)
print(dt.minute)
import time
print(time.time())
baslangic_zamani = time.time()
print("Baslama zamani:\t{}".format(baslangic_zamani))
time.sleep(5)
bitis_zamani = time.time()
print("Bitis zamani:\t{}".format(bitis_zamani))
print("Calisma suresi:\t{}".format(bitis_zamani - baslangic_zamani))








