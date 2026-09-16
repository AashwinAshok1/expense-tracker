from db import add_expense, create_table, delete_expense, get_expenses


def show_expenses():
	"""Display all saved expenses."""
	expenses = get_expenses()

	if not expenses:
		print("\nNo expenses found.")
		return

	print("\nExpenses:")
	print("-" * 60)
	for expense_id, amount, category, note, date in expenses:
		print(
			f"{expense_id}. ${amount:.2f} | {category} | "
			f"{note} | {date}"
		)
	print("-" * 60)


def add_new_expense():
	"""Ask the user for expense details and save the expense."""
	while True:
		try:
			amount = float(input("Amount: "))
			break
		except ValueError:
			print("Please enter a valid number for the amount.")

	category = input("Category: ")
	note = input("Note: ")
	date = input("Date (YYYY-MM-DD): ")

	add_expense(amount, category, note, date)
	print("Expense saved.")


def delete_existing_expense():
	"""Show expenses and delete the one selected by the user."""
	expenses = get_expenses()

	if not expenses:
		print("\nNo expenses found.")
		return

	show_expenses()

	try:
		expense_id = int(input("Enter the ID of the expense to delete: "))
	except ValueError:
		print("Please enter a valid expense ID.")
		return

	delete_expense(expense_id)
	print(f"Expense {expense_id} deleted.")


def main():
	"""Run the expense tracker menu."""
	create_table()

	while True:
		print("\nExpense Tracker")
		print("1. Add Expense")
		print("2. View Expenses")
		print("3. Delete Expense")
		print("4. Exit")

		choice = input("Choose an option: ")

		if choice == "1":
			add_new_expense()
		elif choice == "2":
			show_expenses()
		elif choice == "3":
			delete_existing_expense()
		elif choice == "4":
			print("Goodbye!")
			break
		else:
			print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
	main()
