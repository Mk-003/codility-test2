from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def solution(A, D):
    balance = 0
    monthly_fee = 5
    monthly_card_payments = 0
    monthly_card_payments_cost = 0
    current_month = parse_date("2020-01-01")

    for amount, date_str in zip(A, D):
        date = parse_date(date_str)
        if date.month > current_month.month:
            # Calculate the monthly fee
            if monthly_card_payments >= 3 and monthly_card_payments_cost >= 100:
                balance -= monthly_fee
            monthly_card_payments = 0
            monthly_card_payments_cost = 0
            current_month = date

        # Update the balance
        balance += amount
        if amount < 0:
            monthly_card_payments += 1
            monthly_card_payments_cost += abs(amount)

    # Calculate the monthly fee
    if monthly_card_payments >= 3 and monthly_card_payments_cost >= 100:
        balance -= monthly_fee

    return balance - (5 * 12)