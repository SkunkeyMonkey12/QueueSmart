# sets time for making tickets
from datetime import datetime
# Setting variables
staff_usernames = {"Simon": "pass123",
                   "Tony": "pass321",
                   "Paul": "QueuesmartSucks",
                   "Greg": "Password"}
staff_members = ["Simon", "Tony", "Paul", "Greg"]

created_time = datetime.now()

tickets = []

# Staff login is what the staff sees when they run it.


def staff_login():
    print("================================")
    print("      Welcome to QueueSmart     ")
    print("================================")
    print("1. Login")
    print("2. Exit")

    staff_choice = input("Enter choice from above: ")
    if staff_choice == "1":
        print("Enter username below: ")
        user_name = input("")
        print("Enter password below: ")
        password = input("")

        while user_name in staff_usernames and staff_usernames[user_name] == password:
            print("================================")
            print("      Welcome to QueueSmart     ")
            print("================================")
            print(f"Welcome {user_name}. ")
            print("1. Create ticket")
            print("2. Create appointments")
            print("3. View tickets and appointments")
            print("4. Exit")

            staff_choice2 = input("Enter choice from above: ")
            if staff_choice2 == "1":
                ticket = {}
                ticket["customer_name"] = input("Enter customer name: ")

                ticket["Category"] = input(
                    "Enter category of ticket (Housing / Benefits / Digital Support / Wellbeing/ Other): ").lower()
                ticket["Description"] = input("Enter description of ticket: ")
                ticket["Urgency Level"] = input(
                    "Enter level of urgency (Low / Medium / High / Critical): ").lower()
                ticket["Created Date"] = datetime.now().strftime(
                    "%d/%m/%y, %H:%M:%S")
                ticket["Status"] = input(
                    "Enter status (Open / In Progress / Waiting/ Closed): ").lower()
                ticket["Assigned staff member"] = input(
                    "Enter who is dealing with this: ").lower()
                tickets.append(ticket)
                print("Ticket successfulyl created.")
            elif staff_choice2 == "3":
                if tickets:
                    print("\n===== All Tickets =====")
                    for i, t in enumerate(tickets, start=1):
                        print(f"\nTicket #{i}")
                        for key, value in t.items():
                            print(f"{key.capitalize()}: {value}")
                    print("=======================\n")
                else:
                    print("\nNo tickets available.\n")

        else:
            print("Login denied")


staff_login()
