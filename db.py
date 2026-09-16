import sqlite3


DATABASE_NAME = "expenses.db"


def connect_db():
	"""Connect to the SQLite database."""
	return sqlite3.connect(DATABASE_NAME)


def create_table():
	"""Create the expenses table if it does not already exist."""
	connection = connect_db()

	connection.execute(
		"""
		CREATE TABLE IF NOT EXISTS expenses (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			amount REAL,
			category TEXT,
			note TEXT,
			date TEXT
		)
		"""
	)
	connection.commit()
	connection.close()


def add_expense(amount, category, note, date):
	"""Insert one expense into the database."""
	connection = connect_db()

	connection.execute(
		"""
		INSERT INTO expenses (amount, category, note, date)
		VALUES (?, ?, ?, ?)
		""",
		(amount, category, note, date),
	)
	connection.commit()
	connection.close()


def delete_expense(id):
	"""Delete an expense by its id."""
	connection = connect_db()

	connection.execute("DELETE FROM expenses WHERE id = ?", (id,))
	connection.commit()
	connection.close()


def get_expenses():
	"""Return all expenses from the database."""
	connection = connect_db()

	cursor = connection.execute(
		"SELECT id, amount, category, note, date FROM expenses ORDER BY id"
	)
	expenses = cursor.fetchall()
	connection.close()

	return expenses
