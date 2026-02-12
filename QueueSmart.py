# QueueSmart Full Program with Ticket Priority & Staff Appointments

# Importing necessary libraries
from datetime import datetime
import hashlib
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk


# Password hashing function for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Staff passwords
staff_usernames = {
    "Simon": hash_password("pass123"),
    "Tony": hash_password("qwerty456"),
    "Paul": hash_password("letmein789"),
    "Greg": hash_password("admin000")
}
staff_members = ["Simon", "Tony", "Paul", "Greg"]

colours = ["red", "blue", "green", "grey"]


# Load csv data
df = pd.read_csv("QueueSmartwork/Queuesmart data(in)(in).csv", skiprows=1)
ticket_data = pd.read_csv("QueueSmartwork/Ticket data.csv", skiprows=1)

# Removes "NaN" and untitled values from the tables
columns_to_keep = [
    "Customer_Name",
    "Category",
    "Appointment_Date",
    "Appointment_Time",
    "Appointment_Duration",
    "Urgency_Level",
    "Status",
    "Vulnerable_Customer",
    "Staff_Name"
]

df = df[columns_to_keep]

columns_to_keep2 = [
    "Customer_Name",
    "Category",
    "Description",
    "Urgency_Level",
    "Created_Date",
    "Status",
    "Vulnerable_Customer",
    "Assigned_Staff_Member",
    "Priority_Score"
]

ticket_data = ticket_data[columns_to_keep2]

# Convert to list of dictionaries and normalize key for staff
appointments = df.to_dict(orient="records")
for appt in appointments:
    if "Staff_Name" not in appt:
        appt["Staff_Name"] = appt.get("Assigned staff member", "Unknown")

# Tickets list
tickets = ticket_data.to_dict(orient="records")


# Priority calculation function
def calculate_ticket_priority(ticket):
    score = 0
    urgency = ticket.get("Urgency Level", "").lower()
    category = ticket.get("Category", "")
    vulnerable = ticket.get("Vulnerable Customer", "").lower()

    # Urgency points
    if urgency == "critical":
        score += 50
    elif urgency == "high":
        score += 30

    # Category points
    if category == "housing":
        score += 10

    # Vulnerable customer
    if vulnerable == "yes":
        score += 15

    return score


# Update weekly appointment count
def update_weekly_count():
    staff_counts = {}
    for appt in appointments:
        staff = appt["Staff_Name"]
        staff_counts[staff] = staff_counts.get(staff, 0) + 1

    for appt in appointments:
        staff = appt["Staff_Name"]
        appt["Weekly_Appointment_Count"] = staff_counts[staff]


# Tkinter modal for staff login
def tkinter_login_screen():
    logged_in_user = {"name": None}

    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()

        if username in staff_usernames and staff_usernames[username] == hash_password(password):
            logged_in_user["name"] = username
            root.destroy()
        else:
            error_label.config(text="Invalid username or password")

    root = tk.Tk()
    root.title("QueueSmart Login Page")
    root.geometry("320x200")
    root.resizable(False, False)

    tk.Label(
        root,
        text="Welcome to the QueueSmart Login Screen!",
        font=("Arial", 11, "bold")
    ).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    error_label = tk.Label(root, text="", fg="red")
    error_label.pack()

    tk.Button(root, text="Login", command=attempt_login).pack(pady=10)

    root.mainloop()
    return logged_in_user["name"]


# Staff login interface
def staff_login(user_name):

    while True:
        print("================================")
        print(f"Welcome {user_name} to QueueSmart")
        print("================================")
        print("1. Create ticket")
        print("2. Create appointment")
        print("3. View tickets (sorted by priority)")
        print("4. View appointments")
        print("5. Update ticket status")
        print("6. View weekly staff chart")
        print("7. View Ticket Created per Week")
        print("8. Exit")

        staff_choice2 = input("Enter choice from above: ")

        # Create ticket
        if staff_choice2 == "1":
            ticket = {}
            ticket["Customer Name"] = input(
                "Enter customer name: ").capitalize()
            ticket["Category"] = input(
                "Enter category (Housing/Benefits/Digital Support/Wellbeing/Other): ").capitalize()
            ticket["Description"] = input(
                "Enter description: ").capitalize()
            ticket["Urgency Level"] = input(
                "Enter urgency (Low/Medium/High/Critical): ").capitalize()
            ticket["Created Date"] = datetime.now().strftime(
                "%d/%m/%y %H:%M:%S")
            ticket["Status"] = input(
                "Enter status (Open/In Progress/Waiting/Closed): ").capitalize()
            ticket["Vulnerable Customer"] = input(
                "Is customer vulnerable? (Yes/No): ").capitalize()
            ticket["Assigned staff member"] = input(
                "Assign staff member (Simon/Paul/Tony/Greg): ").capitalize()
            ticket["Priority_Score"] = calculate_ticket_priority(ticket)
            tickets.append(ticket)
            print("Ticket successfully created.")

        # Create appointment
        elif staff_choice2 == "2":
            appointment = {}
            appointment["customer name"] = input(
                "Enter customer name: ").capitalize()
            appointment["Category"] = input("Enter category: ").capitalize()
            appointment["appointment_date"] = input(
                "Enter appointment date (DD/MM/YY): ")
            appointment["appointment time"] = input(
                "Enter appointment time (HH:MM): ")
            appointment["appointment duration"] = input(
                "Enter appointment duration (minutes): ")
            appointment["Staff_Name"] = input(
                "Assign staff member (Simon/Paul/Tony/Greg): ").capitalize()
            appointment["Reason for appointment"] = input(
                "Enter reason: ").capitalize()
            appointments.append(appointment)
            update_weekly_count()
            print(
                f"Appointment created for {appointment['customer name']}.")

        # View tickets sorted by priority
        elif staff_choice2 == "3":
            if tickets:
                sorted_tickets = sorted(
                    tickets,
                    key=lambda x: x.get("Priority_Score", 0),
                    reverse=True
                )

                print("\n===== Tickets (Sorted by Priority) =====")
                for i, t in enumerate(sorted_tickets, start=1):
                    print(f"\nTicket #{i}")
                    for key, value in t.items():
                        print(f"{key}: {value}")
                print("========================================\n")
            else:
                print("\nNo tickets available.\n")

        # View appointments
        elif staff_choice2 == "4":
            if appointments:
                print("\n===== Appointments =====")
                for i, t in enumerate(appointments, start=1):
                    print(f"\nAppointment #{i}")
                    for key, value in t.items():
                        print(f"{key}: {value}")
                print("=========================\n")
            else:
                print("\nNo appointments available.\n")

        # Update ticket status
        elif staff_choice2 == "5":
            if tickets:
                # List ticket numbers and customer names for easy selection
                print("\nTickets:")
                for i, t in enumerate(tickets, start=1):
                    print(
                        f"{i}. {t.get('Customer Name')} - Status: {t.get('Status', 'N/A')}")

                # Ask user which ticket to edit
                index = int(input("\nEnter ticket number to update: ")) - 1

                if 0 <= index < len(tickets):
                    ticket = tickets[index]

                    # Show only the selected ticket
                    print("\nSelected Ticket:")
                    for key, value in ticket.items():
                        print(f"{key}: {value}")

                    # Update status
                    ticket["Status"] = input(
                        "\nEnter new status: ").capitalize()
                    print("\nTicket status updated successfully!")
                else:
                    print("Invalid ticket number.")
            else:
                print("\nNo tickets available to update.\n")

        # Weekly staff chart
        elif staff_choice2 == "6":
            if appointments:
                update_weekly_count()
                staff_names = [appt["Staff_Name"] for appt in appointments]
                counts = [appt["Weekly_Appointment_Count"]
                          for appt in appointments]
                plt.figure(figsize=(10, 6))
                plt.bar(staff_names, counts, color=colours)
                plt.title("Weekly Appointments per Staff Member",
                          fontname="Times New Roman")
                plt.xlabel("Staff Members", fontname="Times New Roman")
                plt.ylabel("Number of appointments",
                           fontname="Times New Roman")
                plt.grid(axis="y")
                plt.show()
            else:
                print("No appointments to display.")

        # Tickets per category chart
        elif staff_choice2 == "7":
            print("Loading Ticket Data...")
            if not tickets:
                print("No tickets to display.")
            else:
                df_tickets = pd.DataFrame(tickets)
                if "Category" not in df_tickets:
                    print("No 'Category' column found in ticket data.")
                else:
                    df_tickets["Category"] = df_tickets["Category"].str.strip(
                    ).str.capitalize()
                    counts = df_tickets["Category"].value_counts().sort_index()
                    plt.figure(figsize=(10, 6))
                    plt.bar(counts.index, counts.values, color=colours)
                    plt.title("Number of Tickets Created per Category",
                              fontname="Times New Roman")
                    plt.xlabel("Category")
                    plt.ylabel("Number of Tickets")
                    plt.grid(axis="y")
                    plt.show()

        # Exit
        elif staff_choice2 == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


# Runs program
user = tkinter_login_screen()
if user:
    staff_login(user)
else:
    print("Login Denied. Exiting program.")
