# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    if not isinstance(values, list):
        return 0.0

    total = 0
    count = 0

    for v in values:
        if v is not None:
            try:
                total += float(v)
                count += 1
            except (ValueError, TypeError):
                continue

    if count == 0:
        return 0.0

    return total / count
