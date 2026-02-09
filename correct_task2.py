# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
import re

def count_valid_emails(emails):
    email_regex_pattern = r'^[\w.+-]+@([\w-]+\.)+[\w-]{2,20}$'
    count = 0

    for email in emails:
        try:
            if re.match(email_regex_pattern, email):
                count += 1
        except (TypeError):
            continue

    return count
