# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

def calculate_average_order_value(orders):
    if not isinstance(orders, list):
        return 0.0

    total = 0
    count = 0

    for order in orders:
        try:    
            if ("status" in order and "amount" in order) and order["status"] != "cancelled":
                total += order["amount"]
                count += 1
        except (TypeError):
            continue

    if count == 0:
        return 0.0

    return total / count

print(calculate_average_order_value(5))