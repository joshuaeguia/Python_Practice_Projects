all_records = []
all_expenses = []

def add_expense():

    try:
        expense_description = input("Enter your expense description: ")
        category = input("Enter your expense category: ")
        amount = int(input("Enter your expense amount: "))

    except ValueError:
        print()
        print("Invalid input! Please add the correct amount!")

    except Exception as e:
        print(e)

    else:
        expense_record = {
        "Expense Description": expense_description,
        "Category": category,
        "Amount": amount
            }

        all_descriptions = expense_record.get("Expense Description")
        all_categories = expense_record.get("Category")
        all_amounts = expense_record.get("Amount")

        all_records.append(f"{all_descriptions} - {all_categories} - ₱{all_amounts}")
        all_expenses.append(all_amounts)

        print()
        print("Expense added successfully!")
        print()

    return add_expense


def expense_history():

    print("==== EXPENSE HISTORY ====")
    print()

    for i, record in enumerate(all_records, 1):
        print(f"{i}. {record}")


def total_expenses():

    print("==== TOTAL SPENDING ====")
    print()

    full_expenses = 0
    for expenses in all_expenses:
        full_expenses += int(expenses)
    print(f"Total expenses: ₱{full_expenses}")


def main():

    while True:
        print()
        print("==== PERSONAL EXPENSE TRACKER ====")
        print()
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. Exit")
        print()

        choice = input("Choose an option: ")
        print()

        if choice == "1":
            add_expense()
        elif choice == "2":
            expense_history()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Thank you for your time!")
            break
        else:
            print()
            print("Invalid option! Choose between 1 to 4")


main()