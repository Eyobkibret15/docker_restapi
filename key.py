
from django.template import loader
from django.db.models import Avg, F
from django.datetime


today = datetime.now().date()
tomorrow = today + timedelta(1)
today_start = datetime.combine(today, time())
today_end = datetime.combine(tomorrow, time())

print(today_start)
print(today_end)

