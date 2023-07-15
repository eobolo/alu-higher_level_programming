#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    roman_sum = 0
    if type(roman_string) != str or roman_string is None:
        return roman_sum

    if len(roman_string) % 2 == 0:
        for i in range(0, len(roman_string), 2):
            if numerals.get(roman_string[i]) > \
                    numerals.get(roman_string[i + 1]):
                roman_sum += numerals.get(roman_string[i]) + \
                        numerals.get(roman_string[i + 1])
            elif numerals.get(roman_string[i]) < \
                    numerals.get(roman_string[i + 1]):
                roman_sum += numerals.get(roman_string[i + 1]) - \
                        numerals.get(roman_string[i])
            else:
                roman_sum += numerals.get(roman_string[i]) + \
                        numerals.get(roman_string[i + 1])
    else:
        for i in range(0, len(roman_string), 2):
            if i == 0 and len(roman_string) == 1:
                roman_sum += numerals.get(roman_string[i])
                return roman_sum
            elif i != len(roman_string) - 1 and \
                    numerals.get(roman_string[i + 1]) > \
                    numerals.get(roman_string[i]) and i > 0:
                roman_sum += numerals.get(roman_string[i + 1]) - \
                        numerals.get(roman_string[i]) - \
                        numerals.get(roman_string[i])
                roman_sum += numerals.get(roman_string[i + 2])
            elif i != len(roman_string) - 1 and \
                    numerals.get(roman_string[i + 1]) > \
                    numerals.get(roman_string[i]):
                roman_sum += numerals.get(roman_string[i + 1]) - \
                        numerals.get(roman_string[i])
                roman_sum += numerals.get(roman_string[i + 2])
            elif i == 0:
                roman_sum += numerals.get(roman_string[i])
                if numerals.get(roman_string[i + 1]) >= \
                        numerals.get(roman_string[i + 2]):
                    roman_sum += numerals.get(roman_string[i + 1]) + \
                            numerals.get(roman_string[i + 2])
                else:
                    roman_sum += numerals.get(roman_string[i + 2]) - \
                            numerals.get(roman_string[i + 1])
            elif i != 0 and i != len(roman_string) - 1:
                if numerals.get(roman_string[i + 1]) >= \
                        numerals.get(roman_string[i + 2]):
                    roman_sum += numerals.get(roman_string[i + 1]) + \
                            numerals.get(roman_string[i + 2])
                else:
                    roman_sum += numerals.get(roman_string[i + 2]) - \
                            numerals.get(roman_string[i + 1])
    return roman_sum
