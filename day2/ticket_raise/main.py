import ticket

name = input("Enter customer name: ")

phone = input("Enter phone number: ")
phone = phone[:2] + "******" + phone[-2:]

msg = input("Enter ticket message: ")

# extract ticket ID
ticket_id = msg.split(":")[1].split(".")[0]

# detect issue
if "login" in msg:
    issue = "Login Issue"
elif "payment" in msg:
    issue = "Payment Issue"
else:
    issue = "General Issue"

charges = int(input("Enter number of service charges: "))

print("\nOutput:\n")

details = ticket.create_ticket(
    Name=name,
    Phone=phone,
    Ticket_ID=ticket_id,
    Issue=issue,
    charges=charges
)

print(details)


# Sample Input
# Enter customer name: Sameera
# Enter phone number: 9876543210
# Enter ticket message: ticket:TK123.login_issue
# Enter number of service charges: 2
# Charge 1: 500
# Charge 2: 300

# Sample Output
# Name: Sameera
# Phone: 98******10
# Ticket_ID: TK123
# Issue: Login Issue
# Total Charges: 800