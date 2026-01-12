def calculate_total(quantity, price):
    return quantity * price

def format_currency(amount):
    return "${:,.2f}".format(amount)