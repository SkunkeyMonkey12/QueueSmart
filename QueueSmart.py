# sets time for making tickets
from datetime import datetime
import hashlib
import pandas as pd
import matplotlib.pyplot as plt

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Setting variables
staff_usernames = {
    "Simon":hash_password("pass123"),
    "Tony": hash_password("qwerty456"),
    "Paul": hash_password("letmein789"),
    "Greg": hash_password("admin000")
}
staff_members = ["Simon", "Tony", "Paul", "Greg"]

created_time = datetime.now()

tickets = []
appointments = []

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

        while (user_name in staff_usernames and staff_usernames[user_name] == hash_password(password)):

            print("================================")
            print("      Welcome to QueueSmart     ")
            print("================================")
            print(f"Welcome {user_name}. ")
            print("1. Create ticket")
            print("2. Create appointments")
            print("3. View tickets")
            print("4. View appointments")
            print("5, Update ticket status")
            print("6. View Chart of Tickets")
            print("7. Exit")

            staff_choice2 = input("Enter choice from above: ")
            if staff_choice2 == "1":
                ticket = {}
                ticket["Customer Name"] = input("Enter customer name: ")

                ticket["Category"] = input(
                    "Enter category of ticket (Housing / Benefits / Digital Support / Wellbeing/ Other): ").lower()
                ticket["Description"] = input("Enter description of ticket: ")
                ticket["Urgency Level"] = input(
                    "Enter level of urgency (Low / Medium / High / Critical): ").lower()
                ticket["Created Date"] = datetime.now().strftime(
                    "%d/%m/%y, %H:%M:%S")
                ticket["Status"] = input(
                    "Enter status (Open / In Progress / Waiting/ Closed): ").lower()
                ticket["Vulnerable Customer"] = input(
                    "Is this a vulnerable customer? (Yes / No): ").lower()
                ticket["Assigned staff member"] = input(
                    "Enter who is dealing with this: ").lower()
                tickets.append(ticket)
                print("Ticket successfully created.")

                if ticket["Urgency Level"] == "critical":
                    ticket["Priority"] = "50"
                elif ticket["Urgency Level"] == "critical" and ticket["Category"] == "housing":
                    ticket["Priority"] = "60"
                elif ticket["Urgency Level"] == "high":
                    ticket["Priority"] = "30"
                elif ticket["Urgency Level"] == "high" and ticket["Category"] == "housing":
                    ticket["Priority"] = "40"
                elif ticket["Urgency Level"] == "medium":
                    ticket["Priority"] = "Complete higher priority tickets first."
                elif ticket["Urgency Level"] =="low":
                    ticket["Priority"] = "Complete higher priority tickets first."
                
                

            elif staff_choice2 == "2":
                appointment = {}
                appointment["customer name"] = input("Enter customer name: ")
                appointment["appointment_date"] = input("Enter appointment date (DD/MM/YY): ")
                appointment["appointment time"] = input("Enter appointment time (HH:MM): ")
                
                appointment["appointment duration"] = input("Enter appointment duration (in minutes): ")
                appointment["Assigned staff member"] = input("Enter who is dealing with this: ")
                appointment["Reason for appointment"] = input("Enter reason for appointment: ")
                appointments.append(appointment)
                print(f"Appointment successfully created for {appointment['customer name']}.")
                

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

            elif staff_choice2 == "4":
                if appointments:
                    print("\n===== All Appointments =====")
                    for i, t in enumerate(appointments, start=1):
                        if "appointment_date" in t:
                            print(f"\nAppointment #{i}")
                            for key, value in t.items():
                                print(f"{key.capitalize()}: {value}")
                    print("============================\n")
                else:
                    print("\nNo appointments available.\n")


            elif staff_choice2 == "5":
                if tickets:
                    print("\n==== Update Ticket Status ====")
                    for i, t in enumerate(tickets, start=1):
                        print(f"\nTicket #{i}")
                        for key, value in t.items():
                            print(f"{key.capitalize()}: {value}")
                    print("==============================\n")
                else:
                    print("\nNo tickets available to update.\n")


            elif staff_choice2 == "6":
                df = pd.read_csv("m:\\Queuesmart qork\\queuesmart csv.txt")
                print(df)

            elif staff_choice2 == "7":
                print("Exiting...")
                break

        else:
            print("Login denied")


staff_login()
