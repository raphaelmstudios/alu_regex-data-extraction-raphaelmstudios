import re

print("***Program started!***")

# Read the input file
with open('sample_input.txt', 'r') as file:
    text = file.read()

print("=====ORIGINAL TEXT=====")
print(text)
print()

# EXTRACTING EMAIL ADDRESSES

email_pattern = r'\w+@\w+\.\w+'
emails = re.findall(email_pattern, text)

print("=====EMAILS EXTRACTED=====")
print(emails)
print()

#EXTRACTING PHONE NUMBERS

#US/International phone pattern
us_phone_pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'

#Rwandan phone pattern
rw_phone_pattern = r'(?:\+250|00250|0)?[\s]?7[2-9][\s]?\d[\s]?\d{3}[\s]?\d{3}'

us_phones = re.findall(us_phone_pattern, text)
rw_phones = re.findall(rw_phone_pattern, text)
all_phones = us_phones + rw_phones

print("=====PHONE NUMBERS EXTRACTED=====")
for phone in all_phones:
#phone pattern might return tuples because of groups, so we join them
    if isinstance(phone, tuple):
        phone = ''.join(phone)
    print(f" -{phone}")
print()

#EXTRACTING WEBSITE URLS

url_pattern = r'https?://[\w-]+(?:\.[\w-]+)*\.\w{2,}(?:/[\w\-._~:/?#[\]@!$&\'()*+,;=]*)?'
urls = re.findall(url_pattern, text)

print("=====WEBSITE URLS EXTRACTED=====")
if urls:
    for url in urls:
    # url pattern might return tuples because it has groups, so we join them
        if isinstance(url, tuple):
            url = ''.join(url)
        print(f" -{url}")
else:
    print(" No URLs found.")
print()

#EXTRACTING CURRENCY AMOUNTS

# Symbol-based currencies such as ($, £, €, ¥)
symbol_currency_pattern = r'[$£€¥]\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

# Code-based currencies such as (RWF, KES) which usually come before or after the amount
code_currency_pattern = r'(?:RWF|FRw|KSh|KES)\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s(?:RWF|FRw|KSh|KES)'

symbol_currencies = re.findall(symbol_currency_pattern, text)
code_currencies = re.findall(code_currency_pattern, text)
print("=====CURRENCY AMOUNTS EXTRACTED=====")
all_currencies = symbol_currencies + code_currencies

if all_currencies:
    for currency in all_currencies:
        print(f" -{currency}")
else:
    print(" No currency amounts found.")
print()

#TIME EXTRACTION
#24-hour format
time_24h_pattern = r'(?:[01]\d|2[0-3]):[0-5]\d'

#12-hour format with AM/PM
time_12h_pattern = r'(?:1[0-2]|0?[1-9]):[0-5]\d\s?(?:AM|PM|am|pm)'

times_24h = re.findall(time_24h_pattern, text)
times_12h = re.findall(time_12h_pattern, text)

all_times = times_24h + times_12h

print("=====TIME EXTRACTED=====")
if all_times:
    for time in all_times:
        print(f" -{time}")
else:
    print(" No time formats found.")
print()

#HASHTAG EXTRACTION
hashtag_pattern = r'\B#[A-Za-z][A-Za-z0-9_]{0,138}'
hashtags = re.findall(hashtag_pattern, text)

print("=====HASHTAGS EXTRACTED=====")
if hashtags:
    for hashtag in hashtags:
        print(f" -{hashtag}")
else:
    print(" No hashtags found.")
print()

print("***Program ended!***")