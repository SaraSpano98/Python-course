# Immutable sequence of characters.

# <str>  = <str>.strip()                       # Strips all whitespace characters from both ends.
# <str>  = <str>.strip('<chars>')              # Strips passed characters. Also lstrip/rstrip().
# <list> = <str>.split()                       # Splits on one or more whitespace characters.
# <list> = <str>.split(sep=None, maxsplit=-1)  # Splits on 'sep' str at most 'maxsplit' times.
# <list> = <str>.splitlines(keepends=False)    # On [\n\r\f\v\x1c-\x1e\x85\u2028\u2029] and \r\n.
# <str>  = <str>.join(<coll_of_strings>)       # Joins elements by using string as a separator.
# <bool> = <sub_str> in <str>                  # Checks if string contains the substring.
# <bool> = <str>.startswith(<sub_str>)         # Pass tuple of strings for multiple options.
# <int>  = <str>.find(<sub_str>)               # Returns start index of the first match or -1.
# <int>  = <str>.index(<sub_str>)              # Same, but raises ValueError if there's no match.
# <str>  = <str>.lower()                       # Changes the case. Also upper/capitalize/title().
# <str>  = <str>.replace(old, new [, count])   # Replaces 'old' with 'new' at most 'count' times.
# <str>  = <str>.translate(<table>)            # Use `str.maketrans(<dict>)` to generate table.
# <str>  = chr(<int>)                          # Converts int to Unicode character.
# <int>  = ord(<str>)                          # Converts Unicode character to int.

# Use 'unicodedata.normalize("NFC", <str>)' on strings like 'Motörhead' before comparing them to other strings, because 'ö' can be stored as one or two characters.
# 'NFC' converts such characters to a single character, while 'NFD' converts them to two.