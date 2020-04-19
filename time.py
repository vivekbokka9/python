from datetime import date, timedelta
today = date.today()
vdate = (date.today() + timedelta(days=60)).isoformat()
print("", vdate)

