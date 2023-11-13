import json

data = {"payment": {}}

data["new_customer"] = (
    True if input("Are you a new customer? (y/n) ").lower() == "y" else False
)
data["gender"] = (
    "male" if input("Are you male or female? ").lower() == "male" else "female"
)
data["first_name"] = input("Please enter your first name: ")
data["surname"] = input("Please enter your surname: ")

data["payment"]["card_number"] = input("Please enter your card number: ")
data["payment"]["expiry_date"] = {}
data["payment"]["expiry_date"]["month"] = input(
    "Please enter your card's expiry month: "
)
data["payment"]["expiry_date"]["year"] = input("Please enter your card's expiry year: ")
data["payment"]["cvv"] = input("Please enter your card's CVV: ")

print(json.dumps(data, indent=4))
