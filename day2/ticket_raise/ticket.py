def create_ticket(**details):
    result = ""

    for key, value in details.items():
        if key != "charges":
            result += f"{key}: {value}\n"
        else:
            total = 0
            for i in range(value):
                amt = int(input(f"Charge {i+1}: "))
                total += amt
            result += f"Total Charges: {total}\n"

    return result