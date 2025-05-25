# Format
# <str> = f'{<el_1>}, {<el_2>}'            # Curly brackets can also contain expressions.
# <str> = '{}, {}'.format(<el_1>, <el_2>)  # Or: '{0}, {a}'.format(<el_1>, a=<el_2>)
# <str> = '%s, %s' % (<el_1>, <el_2>)      # Redundant and inferior C-style formatting.

# Example
# import collections
# Person = collections.namedtuple('Person', 'name height')
# person = Person('Jean-Luc', 187)
# print(f'{person.name} is {person.height / 100} meters tall.')
# Output: 'Jean-Luc is 1.87 meters tall.'

# General Options
# {<el>:<10}                               # '<el>      '
# {<el>:^10}                               # '   <el>   '
# {<el>:>10}                               # '      <el>'
# {<el>:.<10}                              # '<el>......'
# {<el>:0}                                 # '<el>'
# Objects are rendered using 'format(<el>, "<options>")'.
# Options can be generated dynamically: f'{<el>:{<str/int>}[…]}'
# Adding '=' to the expression prepends it to the output: f'{1+1=}' returns '1+1=2'.
# Adding '!r' to the expression converts object to string by calling its repr() method.

# Strings
# {'abcde':10}                             # 'abcde     '
# {'abcde':10.3}                           # 'abc       '
# {'abcde':.3}                             # 'abc'
# {'abcde'!r:10}                           # "'abcde'   "

# Numbers
# {123456:10}                              # '    123456'
# {123456:10,}                             # '   123,456'
# {123456:10_}                             # '   123_456'
# {123456:+10}                             # '   +123456'
# {123456:=+10}                            # '+   123456'
# {123456: }                               # ' 123456'
# {-123456: }                              # '-123456'

# Floats
# {1.23456:10.3}                           # '      1.23'
# {1.23456:10.3f}                          # '     1.235'
# {1.23456:10.3e}                          # ' 1.235e+00'
# {1.23456:10.3%}                          # '  123.456%'

# Comparison of presentation types:
# +--------------+----------------+----------------+----------------+----------------+
# |              |    {<float>}   |   {<float>:f}  |   {<float>:e}  |   {<float>:%}  |
# +--------------+----------------+----------------+----------------+----------------+
# |  0.000056789 |   '5.6789e-05' |    '0.000057'  | '5.678900e-05' |    '0.005679%' |
# |  0.00056789  |   '0.00056789' |    '0.000568'  | '5.678900e-04' |    '0.056789%' |
# |  0.0056789   |   '0.0056789'  |    '0.005679'  | '5.678900e-03' |    '0.567890%' |
# |  0.056789    |   '0.056789'   |    '0.056789'  | '5.678900e-02' |    '5.678900%' |
# |  0.56789     |   '0.56789'    |    '0.567890'  | '5.678900e-01' |   '56.789000%' |
# |  5.6789      |   '5.6789'     |    '5.678900'  | '5.678900e+00' |  '567.890000%' |
# | 56.789       |  '56.789'      |   '56.789000'  | '5.678900e+01' | '5678.900000%' |
# +--------------+----------------+----------------+----------------+----------------+
# +--------------+----------------+----------------+----------------+----------------+
# |              |  {<float>:.2}  |  {<float>:.2f} |  {<float>:.2e} |  {<float>:.2%} |
# +--------------+----------------+----------------+----------------+----------------+
# |  0.000056789 |    '5.7e-05'   |      '0.00'    |   '5.68e-05'   |      '0.01%'   |
# |  0.00056789  |    '0.00057'   |      '0.00'    |   '5.68e-04'   |      '0.06%'   |
# |  0.0056789   |    '0.0057'    |      '0.01'    |   '5.68e-03'   |      '0.57%'   |
# |  0.056789    |    '0.057'     |      '0.06'    |   '5.68e-02'   |      '5.68%'   |
# |  0.56789     |    '0.57'      |      '0.57'    |   '5.68e-01'   |     '56.79%'   |
# |  5.6789      |    '5.7'       |      '5.68'    |   '5.68e+00'   |    '567.89%'   |
# | 56.789       |    '5.7e+01'   |     '56.79'    |   '5.68e+01'   |   '5678.90%'   |
# +--------------+----------------+----------------+----------------+----------------+
# '{<float>:g}' is '{<float>:.6}' with stripped zeros, exponent starting at '1e+06'.
# When both rounding up and rounding down are possible, the one that returns result with even last digit is chosen. That makes '{6.5:.0f}' a '6' and '{7.5:.0f}' an '8'.
# This rule only effects numbers that can be represented exactly by a float (.5, .25, …).

# Ints
# {90:c}                                   # 'Z'. Unicode character with value 90.
# {90:b}                                   # '1011010'. Binary representation of the int.
# {90:X}                                   # '5A'. Hexadecimal with upper-case letters.

# Numbers
# <int>      = int(<float/str/bool>)           # Or: math.trunc(<float>)
# <float>    = float(<int/str/bool>)           # Or: <int/float>e±<int>
# <complex>  = complex(real=0, imag=0)         # Or: <int/float> ± <int/float>j
# <Fraction> = fractions.Fraction(0, 1)        # Or: Fraction(numerator=0, denominator=1)
# <Decimal>  = decimal.Decimal(<str/int>)      # Or: Decimal((sign, digits, exponent))
# 'int(<str>)' and 'float(<str>)' raise ValueError on malformed strings.
# Decimal numbers are stored exactly, unlike most floats where '1.1 + 2.2 != 3.3'.
# Floats can be compared with: 'math.isclose(<float>, <float>)'.
# Precision of decimal operations is set with: 'decimal.getcontext().prec = <int>'.
# Bools can be used anywhere ints can, because bool is a subclass of int: 'True + 1 == 2'.

# Built-in Functions
# <num> = pow(<num>, <num>)                    # Or: <number> ** <number>
# <num> = abs(<num>)                           # <float> = abs(<complex>)
# <num> = round(<num> [, ±ndigits])            # Also math.floor/ceil(<number>).
# <num> = min(<collection>)                    # Also max(<num>, <num> [, ...]).
# <num> = sum(<collection>)                    # Also math.prod(<collection>).

# Math
# from math import pi, inf, nan, isnan         # `inf*0` and `nan+1` return nan.
# from math import sqrt, factorial             # `sqrt(-1)` raises ValueError.
# from math import sin, cos, tan               # Also: asin, degrees, radians.
# from math import log, log10, log2            # Log accepts base as second arg.

# Statistics
# from statistics import mean, median, mode    # Also: variance, stdev, quantiles.

# Random
# from random import random, randint, uniform  # Also: gauss, choice, shuffle, seed.
# <float> = random()                           # Returns a float inside [0, 1).
# <num>   = randint/uniform(a, b)              # Returns an int/float inside [a, b].
# <float> = gauss(mean, stdev)                 # Also triangular(low, high, mode).
# <el>    = choice(<sequence>)                 # Keeps it intact. Also sample(pop, k).
# shuffle(<list>)                              # Shuffles the list in place.

# Hexadecimal Numbers
# <int> = ±0x<hex>                             # Or: ±0b<bin>
# <int> = int('±<hex>', 16)                    # Or: int('±<bin>', 2)
# <int> = int('±0x<hex>', 0)                   # Or: int('±0b<bin>', 0)
# <str> = hex(<int>)                           # Returns '[-]0x<hex>'. Also bin().

# Bitwise Operators
# <int> = <int> & <int>                        # And (0b1100 & 0b1010 == 0b1000).
# <int> = <int> | <int>                        # Or  (0b1100 | 0b1010 == 0b1110).
# <int> = <int> ^ <int>                        # Xor (0b1100 ^ 0b1010 == 0b0110).
# <int> = <int> << n_bits                      # Left shift. Use >> for right.
# <int> = ~<int>                               # Not. Also -<int> - 1.