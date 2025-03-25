
    # Prompt the user for an amount in euros and the exchange rate
    euros = float(input("Enter an amount in euros: "))
    exchange_rate = float(input("Enter the exchange rate: "))

    # Calculate the equivalent amount in pounds, taking into account the commission
    pounds = euros * exchange_rate
    commission = pounds * 0.02
    total = pounds + commission
    print(f"The equivalent amount in pounds is {total}")