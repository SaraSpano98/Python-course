# <D/T/DT> = D/T/DT.fromisoformat(<str>)      # Object from ISO string. Raises ValueError.
# <DT>     = DT.strptime(<str>, '<format>')   # Datetime from custom string. See Format.
# <D/DTn>  = D/DT.fromordinal(<int>)          # D/DT from days since the Gregorian NYE 1.
# <DTn>    = DT.fromtimestamp(<float>)        # Local naive DT from seconds since the Epoch.
# <DTa>    = DT.fromtimestamp(<float>, <tz>)  # Aware datetime from seconds since the Epoch.

# ISO strings come in following forms: 'YYYY-MM-DD', 'HH:MM:SS.mmmuuu[±HH:MM]', 
# or both separated by an arbitrary character. All parts following the hours are optional.
# Python uses the Unix Epoch: '1970-01-01 00:00 UTC', '1970-01-01 01:00 CET', ...

# Decode
# <str>    = <D/T/DT>.isoformat(sep='T')      # Also `timespec='auto/hours/minutes/seconds/…'`.
# <str>    = <D/T/DT>.strftime('<format>')    # Custom string representation of the object.
# <int>    = <D/DT>.toordinal()               # Days since Gregorian NYE 1, ignoring time and tz.
# <float>  = <DTn>.timestamp()                # Seconds since the Epoch, from local naive DT.
# <float>  = <DTa>.timestamp()                # Seconds since the Epoch, from aware datetime.

# Format
# >>> dt = datetime.strptime('2025-08-14 23:39:00.00 +0200', '%Y-%m-%d %H:%M:%S.%f %z')
# >>> dt.strftime("%dth of %B '%y (%a), %I:%M %p %Z")
# "14th of August '25 (Thu), 11:39 PM UTC+02:00"
# '%z' accepts '±HH[:]MM' and returns '±HHMM' or empty string if object is naive.
# '%Z' accepts 'UTC/GMT' and local timezone's code and returns timezone's name, 
# 'UTC[±HH:MM]' if timezone is nameless, or an empty string if object is naive.