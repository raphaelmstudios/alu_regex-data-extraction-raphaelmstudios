import re

print("***Program started!***")

# Read the input file
with open('sample_input.txt', 'r') as file:
    text = file.read()

print("=====ORIGINAL TEXT=====")
print(text)
print()

# Extracting email addresses using regex
email_pattern = r'\w+@\w+\.\w+'
emails = re.findall(email_pattern, text)

print("=====EMAILS EXTRACTED=====")
print(emails)
print()

#Extracting phone numbeers
#US/International phone pattern
us_phone_pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'

#Rwandan phone pattern
rw_phone_pattern = r'(?:\+250|00250|0)?[\s]?7[2-9][\s]?\d[\s]?\d{3}[\s]?\d{3}'

us_phones = re.findall(us_phone_pattern, text)
rw_phones = re.findall(rw_phone_pattern, text)
all_phones = us_phones + rw_phones

print("=====PHONE NUMBERS EXTRACTED=====")
for phone in all_phones:
    if isinstance(phone, tuple):
        phone = ''.join(phone)
    print(f" -{phone}")
print()

print("***Program ended!***")