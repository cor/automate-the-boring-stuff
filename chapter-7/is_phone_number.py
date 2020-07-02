import re

phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phone_number_regex.search('My phone number is 415-555-4242')

print(f'Phone number found: {mo.group()}')

area_code, main_number = mo.groups()

print(f'Area: {area_code}, Main number: {main_number}')

