import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import random
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cuppa_joe')
BANNER="""


░█████╗░██╗░░░██╗██████╗░██████╗░░█████╗░  ░░░░░██╗░█████╗░███████╗
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔══██╗  ░░░░░██║██╔══██╗██╔════╝
██║░░╚═╝██║░░░██║██████╔╝██████╔╝███████║  ░░░░░██║██║░░██║█████╗░░
██║░░██╗██║░░░██║██╔═══╝░██╔═══╝░██╔══██║  ██╗░░██║██║░░██║██╔══╝░░
╚█████╔╝╚██████╔╝██║░░░░░██║░░░░░██║░░██║  ╚█████╔╝╚█████╔╝███████╗
░╚════╝░░╚═════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░░╚═╝  ░╚════╝░░╚════╝░╚══════╝

"""
COFFEE = """

_________________¶¶__¶¶___¶¶
__________________¶¶__¶¶__¶¶
___________________¶¶__¶¶__¶¶
___________________¶¶__¶¶__¶¶
__________________¶¶__¶¶__¶¶
_________________¶¶__¶¶__¶¶
________________¶¶__¶¶__¶¶
________________¶¶__¶¶__¶¶
_________________¶¶__¶¶__¶¶
___________________________
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶
____¶¶______________________________¶¶¶¶¶¶____¶¶¶
____¶¶¶_____________________________¶¶¶¶_______¶¶¶
____¶¶¶_____¶_______¶_¶_¶___¶_¶_____¶¶¶_________¶¶
____¶¶¶________¶_¶_¶_______¶_¶______¶¶¶_________¶¶
_____¶¶¶______¶_____¶_¶_______¶_¶__¶¶¶¶________¶¶¶
_____¶¶¶___________¶_¶___¶_________¶¶¶¶________¶¶
______¶¶¶_________¶___¶___¶_¶_____¶¶¶¶¶¶_____¶¶¶
_______¶¶¶_______________________¶¶¶__¶¶¶¶¶¶¶¶¶
________¶¶¶_____________________¶¶¶_______¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶_______________________________¶¶¶¶
____¶¶¶¶¶¶¶_____________________¶¶¶¶¶¶¶
_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶

"""


print(BANNER)
print(COFFEE)
print("****Welcome to Cuppa Joe****\n")
waitress = ['Becky', 'Tisha', 'Cathy', 'Sarah', 'Helen']
print("Hi, My name is " + random.choice(waitress) + ".\n")
print("We have a large selection of drinks available from our menu.\n")

coffee_items = {"Latte": {"Small": 2.50, "Medium": 2.75, "Large": 3.00},
                "Flat White": {"Small": 2.50, "Medium": 2.75, "Large": 3.00},
                "Americano": {"Small": 2.50, "Medium": 2.75, "Large": 3.00},
                "Cappucino": {"Small": 2.50, "Medium": 2.75, "Large": 3.00},
                "Mocha": {"Small": 2.50, "Medium": 2.75, "Large": 3.00}}
extra_items = {"Soya Milk": .50, "Cream": .75,
               "Chocolate": 1.00, "Oat Milk": .50}
total = []
order_items = []


# Add Coffee to the Order
def add_coffee():
    global product
    while True:
        item = [['Latte'], ['Flat White'], ['Americano'],
                ['Cappucino'], ['Mocha']]
        headers = ["Name"]
        print(tabulate(item, headers, tablefmt="rounded_outline"))
        product = input("\nWhat coffee would you like? \n")
        if product in coffee_items:
            break
        else:
            print()
            print("ERROR: PLEASE ENTER OPTION AS SHOWN!\n")


# Add Quantity to the Order
def get_quantity():
    global quantity
    while True:
        quantity = input(f"\nHow many would {product} you like? \n")
        try:
            quantity = int(quantity)
            break
        except ValueError:
            print("\nERROR: PLEASE ENTER A NUMBER!")
            print()


# Add Something extra to the Coffee Order
def add_extra():
    global extra
    extra = [["Soya Milk"], ["Cream"], ["Chocolate"], ["Oat Milk"]]
    headers = ["Extra"]
    print(tabulate(extra, headers, tablefmt="rounded_outline"))
    while True:
        extra = input(f"\nWould you like anything extra with your {product}? \n").capitalize()
        if extra in extra_items:
            break
        else:
            print("ERROR: PLEASE ENTER OPTION AS SHOWN!")
            print()
    total.append(extra_items[extra] * quantity)


# Add Size of Coffee to the Order
def add_size():
    global size
    amount = [["Small"], ["Meduim"], ["Large"]]
    headers = ["Size"]
    print(tabulate(amount, headers, tablefmt="rounded_outline"))
    while True:
        size = input("\nWhat size would you like? \n").capitalize()
        if size in coffee_items:
            print("ERROR: PLEASE ENTER OPTION AS SHOWN!")
            print()
        else:
             break             
    print(f"\nYou have ordered:\n {quantity} - {size} {product} with {extra}.\n")
    total.append(coffee_items[product][size] * quantity)


# Order Number Generated
def order_num():
    print(f"Order number is {random.randint(1,500)}\n")


# Display items and input order
def get_order_items():
    add_coffee()
    get_quantity()
    add_extra()
    add_size()

    order_items.append(f"Quantity: {quantity}\nSize: {size}\nProduct: {product}\nExtra: {extra}\n")


# Main Function that calls all functions
def main():
    while True:
        more = input("Do you want to add to the order? Y/N \n")
        if more == "Y":
            get_order_items()
        else:
            break

    print("\nYou order:\n")
    for order in order_items:
        print(order)

    order_num()

    print(f"The total price is:\n €{sum(total)}\n")

SystemExit()


main()
