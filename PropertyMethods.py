result_isdecimal = "123".isdecimal()                   # Checks for [0-9]. Also [०-९] and [٠-٩].
result_isdigit = "123".isdigit()                       # Checks for [²³¹…] and isdecimal().
result_isnumeric = "123".isnumeric()                   # Checks for [¼½¾…], [零〇一…] and isdigit().
result_isalnum = "abc123".isalnum()                    # Checks for [a-zA-Z…] and isnumeric().
result_isprintable = "Hello!".isprintable()            # Checks for [ !#$%…] and isalnum().
result_isspace = " \t\n".isspace()                     # Checks for [ \t\n\r\f\v\x1c-\x1f\x85\xa0…].