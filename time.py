from datetime import date, timedelta
vdate = (date.today() + timedelta(days=60)).isoformat()
print(vdate)

import select
import warnings
import weakref