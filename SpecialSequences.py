'\d' == '[0-9]'                                   # Also [०-९…]. Matches a decimal character.
'\w' == '[a-zA-Z0-9_]'                            # Also [ª²³…]. Matches an alphanumeric or _.
'\s' == '[ \t\n\r\f\v]'                           # Also [\x1c-\x1f…]. Matches a whitespace.
# By default, decimal characters and alphanumerics from all alphabets are matched unless 'flags=re.ASCII' is used. 

# It restricts special sequence matches to the first 128 Unicode characters and also 
# prevents '\s' from accepting '\x1c', '\x1d', '\x1e' and '\x1f' (non-printable characters that divide text into files, 
# tables, rows and fields, respectively).

# Use a capital letter for negation (all non-ASCII characters will be matched when used in combination with ASCII flag).