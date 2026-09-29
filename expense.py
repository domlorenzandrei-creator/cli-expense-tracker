import json
import argparse
from datetime import date

FILE = 'expenses.json'

# Read and write the file
def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

#Appends and updates the list, lists it and also summarizes it.
def add(args):
    expenses = load()
    expenses.append({
        "date": str(date.today()),
        "amount": args.amount,
        "category": args.category,
    })
    save(expenses)
    print('Successfully added!')

def list_all(args):
    for e in load():
        print(e["date"], e["category"], e["amount"])

def summary(args):
    totals = {}
    for e in load():
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    for category, total in totals.items():
        print(category, total)

#Connects the terminal to the functions
parser = argparse.ArgumentParser()
sub = parser.add_subparsers(required=True)

#Teaches it the add command
p_add = sub.add_parser("add")
p_add.add_argument("amount", type=float)
p_add.add_argument("--category", default="misc")
p_add.set_defaults(func=add)

#Teaches it list and summary command
p_list = sub.add_parser("list")
p_list.set_defaults(func=list_all)

p_sum = sub.add_parser("summary")
p_sum.set_defaults(func=summary)

#Reads and runs it
args = parser.parse_args()
args.func(args)





