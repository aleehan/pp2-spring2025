import psycopg2
import csv

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Gomunotop7_",
    host="localhost"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone VARCHAR(50)
    )
""")
conn.commit()

def insert_data(first_name, last_name, phone):
    cur.execute("SELECT * FROM phonebook WHERE first_name = %s AND last_name = %s", (first_name, last_name))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    else:
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s AND last_name = %s", (phone, first_name, last_name))
    conn.commit()

def upload_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            insert_data(row[0], row[1], row[2])

def enter_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    insert_data(first_name, last_name, phone)

def update_data(id, first_name=None, phone=None):
    if first_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE id = %s", (first_name, id))
    if phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (phone, id))
    conn.commit()

def query_data_by_name_or_phone():
    print("1 - Search by first name")
    print("2 - Search by phone")
    print("3 - Show all contacts")
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter first name: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", ('%' + name + '%',)) # % for matching
    elif choice == '2':
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone ILIKE %s", ('%' + phone + '%',))
    elif choice == '3':
        cur.execute("SELECT * FROM phonebook")
    else:
        print("Invalid option.")
        return

    rows = cur.fetchall() #Extruct the data to the list containing of tuples
    if not rows:
        print("No data found.")
    for row in rows:
        print(row)

def insert_many_users():
    user_list = []
    n = int(input("How many users do you want to add? "))

    for i in range(n):
        print(f"\nUser {i + 1}:")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = input("Enter phone (10 digits): ")

        if len(phone) == 11 and phone.isdigit():
            user_list.append((first_name, last_name, phone))
        else:
            print("Incorrect phone number format. Must be 10 digits.")

    for user in user_list:
        insert_data(user[0], user[1], user[2])
        print(f"User {user[0]} {user[1]} added/updated.")


def delete_data(id):
    cur.execute("DELETE FROM phonebook WHERE id = %s", (id,))
    conn.commit()


def main():
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1 - Add entry from console")
        print("2 - Upload from CSV")
        print("3 - Update entry")
        print("4 - Search entries")
        print("5 - Delete entry")
        print("6 - Insert many users")
        print("7 - Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            enter_data()
        elif choice == '2':
            path = input("Enter CSV file path: ")
            upload_csv(path)
        elif choice == '3':
            id = input("Enter ID to update: ")
            new_name = input("Enter new first name (or press Enter to skip): ")
            new_phone = input("Enter new phone (or press Enter to skip): ")
            update_data(id, first_name=new_name if new_name else None, phone=new_phone if new_phone else None)
        elif choice == '4':
            query_data_by_name_or_phone()
        elif choice == '5':
            id = input("Enter ID to delete: ")
            delete_data(id)
        elif choice == '6':
            insert_many_users()
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()