# Data Extraction & Secure Validation System

A data extraction system built on Python that uses regular expressions for data extraction and validation. It ensures the data is safe and well-formed.

---

## Overview

The project covers regex pattern matching, data input validation, and security considerations in processing data from an untrusted data source.

### Use Case

The data extraction tool ensures that the data it extracts is safe and well-formed.

---

## Features

- 6 Data types can be extracted from the data source. These data types are Emails, Phone Numbers, URLs, Currencies, Time, and Hashtags.
- The tool can support multiple regions. This means it can support US, Rwandan, and Kenyan phone number formats.
- The tool can support multiple currencies. This means it can support $, £, €, ¥, RWF, and KES currencies.
- Security scanning is performed on the data. This includes checking for Cross-Site Scripting (XSS), SQL injection, and path traversal attempts.
- The tool ensures data privacy. This means it can mask emails and phone numbers.
- The tool ensures data is well-formed. This means it can validate the data.
- The tool can output data in a structured format. This means it can output data to the console and a text file.
- The tool can handle messy data. This means it can handle real-world data in various formats.

---

## Data Types Supported

### 1. Email Addresses

**Examples:**

- user@example.com
- firstname.lastname@company.co.uk

**Validation:**

- Maximum 254 characters
- Exactly one @ symbol
- Rejects dangerous characters: `< > " ' ; \`

**Privacy:**

- Masked output (e.g., `j***e@company.co.uk`)

### 2. Phone Numbers

**Formats:**

- US/International
- Rwandan

**Examples:**

- (555) 123-4567 (US format)
- +250 78 234 5678 (Rwanda with country code)
- 0788901234 (Rwanda local)

**Validation:**

- 7-15 digits after removing formatting
- Supports various separators (spaces, dots, dashes)

**Privacy:**

- Last 4 digits shown

### 3. URLs

**Examples:**

- https://www.example.com
- https://portfolio.site.africa/projects

**Validation:**

- Must start with http:// or https://
- Max 2048 characters long
- Blocks dangerous protocols: javascript:, data:, vbscript:, file:

### 4. Currency Amounts

**Examples:**

- $1,299.00 (USD)
- RWF 65,000 (Rwandan Franc)
- KSh 5,500 (Kenyan Shilling)
- €2,500.00 (Euro)

**Validation:**

- Max value: 100,000,000
- Allows for thousands separators
- Allows for prefix and suffix notation

### 5. Time Values

**Formats:**

- 24-Hour
- 12-Hour

**Examples:**

- 14:30 (24-hour)
- 2:30 PM (12-hour)
- 08:00 (24-hour)

### 6. Hashtags

**Examples:**

- #TechConnectAfrica
- #Innovation2024
- #DigitalTransformation

**Features:**

- Must start with a letter
- May include letters, numbers, underscores
- Max 139 characters long (Twitter standard)

---

## Installation

### Setup

```bash
# Clone the repository
git clone https://github.com/RAPHAELMSTUDIOS/alu_regex-data-extraction-RAPHAELMSTUDIOS.git

# Navigate to project directory
cd alu_regex-data-extraction-RAPHAELMSTUDIOS

# Run the program
python3 data_extraction.py
```

---

## Usage

### Basic Usage

1. Enter your text in `sample_input.txt`
2. Execute the program:
   ```bash
   python3 data_extraction.py
   ```
3. View results in console and `sample_output.txt`

### Program Flow

```
1. Read sample_input.txt
2. Display original text
3. Run security scan
   ├─ Pass: Continue with extraction
   └─ Fail: Exit with error
4. Extract and validate each data type
5. Display masked results
6. Save to sample_output.txt
```

---

## Regex Patterns Explained

### Email Pattern Breakdown

```regex
\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b
```

- `\b` - Word boundary (prevents partial matches)
- `[A-Za-z0-9._%+-]+` - Username (letters, numbers, special chars)
- `@` - Literal @ symbol
- `[A-Za-z0-9.-]+` - Domain name
- `\.` - Literal dot
- `[A-Za-z]{2,}` - TLD (minimum 2 letters)

### Phone Pattern (Rwandan)

```regex
(?:\+250|00250|0)?[\s]?7[2-9][\s]?\d[\s]?\d{3}[\s]?\d{3}
```

- `(?:\+250|00250|0)?` - Optional country code (+250, 00250, or 0)
- `[\s]?` - Optional space
- `7[2-9]` - Rwanda mobile starts with 72-79
- `[\s]?\d` - Space + digit
- `[\s]?\d{3}` - Space + 3 digits
- `[\s]?\d{3}` - Space + 3 digits

### Currency Pattern (Symbol-based)

```regex
[$£€¥]\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?
```

- `[$£€¥]` - Currency symbol
- `\s?` - Optional space
- `\d{1,3}` - 1-3 digits
- `(?:,\d{3})*` - Thousands separator (repeating)
- `(?:\.\d{2})?` - Optional decimal (.00)

---

## Project Structure

```
alu_regex-data-extraction-RAPHAELMSTUDIOS/
│
├── data_extraction.py      # Main program
├── sample_input.txt        # Sample input data
├── sample_output.txt       # Generated output
├── README.md              # This file
└── LICENSE                # License information
```

---

## Sample Output

```
==================PROGRAM STARTED!==================

=====ORIGINAL TEXT=====
[Input text displayed here]

=====SECURITY SCAN=====
Input text passed the security scan. Proceeding with data extraction.......

=====EMAILS EXTRACTED=====
 -s***s@techconnect.africa (masked for privacy)
 -j******e@company.co.uk (masked for privacy)

=====PHONE NUMBERS EXTRACTED=====
 -******4567 (masked for privacy)
 -******5678 (masked for privacy)

=====WEBSITE URLS EXTRACTED=====
 -https://www.techconnect.africa
 -https://portfolio.techconnect.africa/projects

=====CURRENCY AMOUNTS EXTRACTED=====
 -$49.99
 -RWF 65,000
 -€2,500.00

=====TIME EXTRACTED=====
 -08:30
 -2:30 PM
 -17:00

=====HASHTAGS EXTRACTED=====
 -#TechConnectAfrica
 -#Innovation2024

Saving results to sample_output.txt...
Results successfully saved to sample_output.txt
====================PROGRAM ENDED!======================
```

---

## Author

**Raphael Mumo**

GitHub: [raphaelmstudios](https://github.com/raphaelmstudios)
