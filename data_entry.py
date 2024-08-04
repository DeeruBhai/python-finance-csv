from datetime import datetime
date_format="%d-%m-%y"
CATEGORIES={"I":"Income","E":"Expense"}
def get_date(prompt, allow_default=False):
    datestring = input(prompt)
    if allow_default and not datestring:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.today().strptime(datestring,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format,Enter valid date in dd-mm-yyyy format")
        return get_date(prompt,allow_default=False)

def get_amount():
    try:
        amount_value = float(input("Enter the amount:"))
        if amount_value <=0 :
            print("Amount must be non-zero and non-negative value.")
        return amount_value
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    try:
        category = input("Enter the category('I'for income or 'E' for expense):").upper()
        if not len(category)  :
            print("Invalid category.Enter a valid category('I'for income or 'E' for expense):")
            return get_category()
        if category in CATEGORIES:
            return CATEGORIES[category]


    except ValueError as e:
        print(e)
        return get_category()

def get_description():
  return input ("Enter a description (optional)")
