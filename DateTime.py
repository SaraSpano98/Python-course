# Provides 'date', 'time', 'datetime' and 'timedelta' classes. All are immutable and hashable.

# $ pip3 install python-dateutil
from datetime import date, time, datetime, timedelta, timezone
import zoneinfo
# import dateutil.tz  # Uncomment if python-dateutil is installed

# Example usages:
# d  = date(year, month, day)               # Only accepts valid dates from 1 to 9999 AD.
# t  = time(hour=0, minute=0, second=0)     # Also: microsecond=0, tzinfo=None, fold=0.
# dt = datetime(year, month, day, hour=0)   # Also: minute=0, second=0, microsecond=0, etc.
# td = timedelta(weeks=0, days=0, hours=0)  # Also: minutes=0, seconds=0, microseconds=0.

# Times and datetimes that have defined timezone are called aware and ones that don't, naive.
# If object is naive, it is presumed to be in the system's timezone!
# 'fold=1' means the second pass in case of time jumping back for one hour.
# Timedelta normalizes arguments to +/-days, seconds (< 86400) and microseconds (< 1M).
# Its str() method returns '[+/-D, ]H:MM:SS[.…]' and total_seconds() a float of all seconds.
# Use 'd.weekday()' or 'dt.weekday()' to get the day of the week as an integer, with Monday being 0.

# Now
# d_today = date.today()                    # Current local date
# dt_today = datetime.today()               # Current local naive datetime
# dt_now = datetime.now()                   # Current local naive datetime
# dt_aware = datetime.now(tzinfo)           # Aware datetime from current time in passed timezone

# To extract time use 'dt_today.time()', 'dt_aware.time()', or 'dt_aware.timetz()'.

# Timezone
# tz_utc = timezone.utc                     # London without daylight saving time (DST)
# tz_offset = timezone(timedelta(hours=1))  # Timezone with fixed offset from UTC
# tz_local = None  # Use dateutil.tz.tzlocal() if dateutil is installed
# tz_zoneinfo = zoneinfo.ZoneInfo('Continent/City_Name')  # IANA zone with dynamic offset

# dt_converted = dt_today.astimezone(tz_utc)  # Converts datetime to the passed or local fixed zone
# dt_replaced = dt_today.replace(tzinfo=tz_utc)  # Changes object's timezone without conversion

# Timezones returned by tzlocal(), ZoneInfo() and implicit local timezone of naive objects have offsets that vary through time due to DST and historical changes of the base offset.

# To get ZoneInfo() to work on Windows run '> pip3 install tzdata'