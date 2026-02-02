import re

# Security scan function to check for dangerous patterns
def is_input_safe(text):
    dangerous_patterns = [
        r"<script",           # JavaScript injection
        r"javascript:",       # Malicious URL protocol
        r"'\s*OR\s*'",       # SQL injection: ' OR '
        r";\s*DROP\s+TABLE", # SQL injection: ; DROP TABLE
        r"\.\./",            # Path traversal: ../
        r"rm\s+-rf",         # Delete command
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            print(f"ERROR! Found '{pattern}'")
            return False
    return True

# Email validation function
def validate_email(email):
    if len(email) > 254:
        print(f"Rejected email (too long): {email[:30]}...")
        return False
    
    if email.count('@') != 1:
        print(f"Rejected email (invalid format): {email}")
        return False
    
    dangerous_chars = ['<', '>', '"', "'", ';', '\\']
    for char in dangerous_chars:
        if char in email:
            print(f"Rejected email (dangerous character): {email}")
            return False
        
    return True

#Phone validation function
def validate_phone(phone):
    digits_only = re.sub(r'\D', '', phone)
    if len(digits_only) < 7 or len(digits_only) > 15:
        print(f"Rejected phone number (invalid length): {phone}")
        return False
    
    return True

#URL validation function
def validate_url(url):
    if len(url) > 2048:
        print(f"Rejected URL (too long): {url[:50]}...")
        return False
    
    if not url.startswith(('http://', 'https://')):
        print(f"Rejected URL (invalid protocol): {url}")
        return False
    
    dangerous_protocols = ['javascript:', 'data:', 'vbscript:', 'file:']
    for protocol in dangerous_protocols:
        if protocol in url.lower():
            print(f"Rejected URL (dangerous protocol): {url}")
            return False
        
    return True

#currency validation function
def validate_currency(amount):
    number_only = re.sub(r'[^\d.]', '', amount)
    try: 
        value = float(number_only)
        if value > 100000000:
            print(f"Rejected currency amount (unrealistic value): {amount}")
            return False
        
        return True
        
    except ValueError:
        print(f"Rejected currency amount (invalid format): {amount}")
        return False
    
#Output masking function
def mask_sensitive_data(data, data_type):
 
#Masking Emails
    if data_type == "email":
        parts = data.split('@')
        
        if len(parts) == 2:
            username = parts[0]
            domain = parts[1]

            if len(username) > 2:
                masked_username = username[0] + '*' * (len(username) - 2) + username[-1]
                return f"{masked_username}@{domain}"
            else:
                return f"{username[0]}*@{domain}"
    
        return data
    
 #Masking phone numbers      
    elif data_type == "phone":
        digits = re.sub(r'\D', '', data)
        
        if len(digits) >= 4:
            return '*' * (len(digits) - 4) + digits[-4:]       
        return data
    
    return data

#redirection to sample_output.txt

print("==================PROGRAM STARTED!==================")

# Read the input file
with open('sample_input.txt', 'r') as file:
    text = file.read()

print("=====ORIGINAL TEXT=====")
print(text)
print()

print("=====SECURITY SCAN=====")
if not is_input_safe(text):
    print("❌Input text failed the security scan. Exiting program.")
    exit()
else:
    print("✅Input text passed the security scan. Proceeding with data extraction.......")

# EXTRACTING EMAIL ADDRESSES
email_pattern = email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
emails_raw = re.findall(email_pattern, text)

emails = []
for email in emails_raw:
    if validate_email(email):
        emails.append(email)
        
print("=====EMAILS EXTRACTED=====")
if emails:
    for email in emails:
        masked = mask_sensitive_data(email, "email")
        print(f" -{masked}(masked for privacy)")
else:
    print(" No valid emails found.")
print()

#EXTRACTING PHONE NUMBERS
#US/International phone pattern
us_phone_pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'

#Rwandan phone pattern
rw_phone_pattern = r'(?:\+250|00250|0)?[\s]?7[2-9][\s]?\d[\s]?\d{3}[\s]?\d{3}'

us_phones_raw = re.findall(us_phone_pattern, text)
rw_phones_raw = re.findall(rw_phone_pattern, text)
all_phones_raw = us_phones_raw + rw_phones_raw

all_phones = []
for phone in all_phones_raw:
    if validate_phone(phone):
        all_phones.append(phone)
        
print("=====PHONE NUMBERS EXTRACTED=====")
if all_phones:
    for phone in all_phones:
        masked = mask_sensitive_data(phone, "phone")
        print(f" -{masked}(masked for privacy)")
else:
    print(" No valid phone numbers found.")
print()

#EXTRACTING WEBSITE URLS
url_pattern = r'https?://[\w-]+(?:\.[\w-]+)*\.\w{2,}(?:/[\w\-._~:/?#[\]@!$&\'()*+,;=]*)?'
urls_raw = re.findall(url_pattern, text)

urls = []
for url in urls_raw:
    if validate_url(url):
        urls.append(url)
print("=====WEBSITE URLS EXTRACTED=====")
if urls:
    for url in urls:
        print(f" -{url}")
else:
    print(" No URLs found.")
print()

#EXTRACTING CURRENCY AMOUNTS
# Symbol-based currencies such as ($, £, €, ¥)
symbol_currency_pattern = r'[$£€¥]\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

# Code-based currencies such as (RWF, KES) which usually come before or after the amount
code_currency_pattern = r'(?:RWF|FRw|KSh|KES)\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s(?:RWF|FRw|KSh|KES)'

symbol_currencies_raw = re.findall(symbol_currency_pattern, text)
code_currencies_raw = re.findall(code_currency_pattern, text)
all_currencies_raw = symbol_currencies_raw + code_currencies_raw

all_currencies = []
for currency in all_currencies_raw:
    if validate_currency(currency):
        all_currencies.append(currency)

print("=====CURRENCY AMOUNTS EXTRACTED=====")

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

#saving the result to output file
print("\nSaving results to sample_output.txt...")

try:
    with open('sample_output.txt', 'w', encoding='utf-8') as f:
        f.write("======================================================================\n")
        f.write("           DATA EXTRACTION & VALIDATION RESULTS\n")
        f.write("======================================================================\n\n")
        
        # Emails
        f.write("------------------------------- EXTRACTED EMAILS -------------------------------\n")
        if emails:
            for email in emails:
                masked = mask_sensitive_data(email, "email")
                f.write(masked + " (masked for privacy)\n")
        else:
            f.write("No emails found.\n")
        f.write("\n")
        
        # Phone Numbers
        f.write("---------------------------- EXTRACTED PHONE NUMBERS ----------------------------\n")
        if all_phones:
            for phone in all_phones:
                masked = mask_sensitive_data(phone, "phone")
                f.write(masked + " (masked for privacy)\n")
        else:
            f.write("No phone numbers found.\n")
        f.write("\n")
        
        # URLs
        f.write("------------------------------- EXTRACTED URLs ---------------------------------\n")
        if urls:
            for url in urls:
                f.write(url + "\n")
        else:
            f.write("No URLs found.\n")
        f.write("\n")
        
        # Currency
        f.write("---------------------------- EXTRACTED CURRENCY AMOUNTS -------------------------\n")
        if all_currencies:
            for currency in all_currencies:
                f.write(currency + "\n")
        else:
            f.write("No currency amounts found.\n")
        f.write("\n")
        
        # Time
        f.write("------------------------------- EXTRACTED TIME VALUES ---------------------------\n")
        if all_times:
            for time in all_times:
                f.write(time + "\n")
        else:
            f.write("No time values found.\n")
        f.write("\n")
        
        # Hashtags
        f.write("------------------------------- EXTRACTED HASHTAGS ------------------------------\n")
        if hashtags:
            for hashtag in hashtags:
                f.write(hashtag + "\n")
        else:
            f.write("No hashtags found.\n")
        f.write("\n")
        
        # End
        f.write("======================================================================\n")
        f.write("                           END OF REPORT\n")
        f.write("======================================================================\n")
    
    print("✅ Results successfully saved to sample_output.txt")
    
except Exception as e:
    print(f"❌ Error saving output file: {e}")
    
print("====================PROGRAM ENDED!======================")