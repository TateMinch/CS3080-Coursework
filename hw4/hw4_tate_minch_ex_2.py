import pyperclip as py
import re

text = py.paste()
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9._]+\.[A-Z|a-z]{2,}', text)
phoneNumbers = re.findall(r'[0-9]{3}-[0-9]{3}-[0-9]{4}',text)
print('Emails: ')
print(emails)
print('Phone Numbers: ')
print(phoneNumbers)
