"""
Functions for regular expression matching.

import re
# <str>   = re.sub(r'<regex>', new, text, count=0)  # Substitutes all occurrences with 'new'.
# <list>  = re.findall(r'<regex>', text)            # Returns all occurrences as strings.
# <list>  = re.split(r'<regex>', text, maxsplit=0)  # Add brackets around regex to keep matches.
# <Match> = re.search(r'<regex>', text)             # First occurrence of the pattern or None.
# <Match> = re.match(r'<regex>', text)              # Searches only at the beginning of the text.
# <iter>  = re.finditer(r'<regex>', text)           # Returns all occurrences as Match objects.

Raw string literals do not interpret escape sequences, thus enabling us to use regex-specific escape sequences that cause SyntaxWarning in normal string literals (since 3.12).
Argument 'new' of re.sub() can be a function that accepts Match object and returns a str.
Argument 'flags=re.IGNORECASE' can be used with all functions.
Argument 'flags=re.MULTILINE' makes '^' and '$' match the start/end of each line.
Argument 'flags=re.DOTALL' makes '.' also accept the '\n'.
're.compile(<regex>)' returns a Pattern object with methods sub(), findall(), etc.
"""
