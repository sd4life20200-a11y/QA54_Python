import re

#####################################################################################################################

def is_positive_less_than_300(value):
    return bool(re.fullmatch(r'[1-9]|[1-9][0-9]|[12][0-9]{2}', value))

print(is_positive_less_than_300("17"))
print(is_positive_less_than_300("299"))
print(is_positive_less_than_300("300"))
print(is_positive_less_than_300("hello"))
print(is_positive_less_than_300("1.11111"))
print(is_positive_less_than_300("-3"))

#####################################################################################################################

def is_number_from_1_to_255(value):
    return bool(re.fullmatch(r'[1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]', value))

print(is_positive_less_than_300("17"))
print(is_positive_less_than_300("299"))
print(is_positive_less_than_300("300"))
print(is_positive_less_than_300("hello"))
print(is_positive_less_than_300("1.11111"))
print(is_positive_less_than_300("-3"))

#####################################################################################################################

def is_israel_mobile(phone):
    return bool(re.fullmatch(r'(05[0-9]|\+9725[0-9])(-?[0-9]){7}', phone))

print(is_israel_mobile("0541234567"))
print(is_israel_mobile("054-1234567"))
print(is_israel_mobile("0541234-567"))
print(is_israel_mobile("054--1234567"))
print(is_israel_mobile("+972054-123-4567"))
