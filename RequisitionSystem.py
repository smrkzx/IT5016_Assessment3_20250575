"""
Author : Porsor Pattansiri
Student ID : 20250575
Course : IT5016
Assignment 2 : Part B Task 1
Due Date : 11th April 2025
Due Time : 11:59 PM
"""



# Single Responsibility Principle (SRP)
    # init > gathering requisition imforamtions
    # add_or_remove_items > Uses for Items management
    # evaluate_approval > Uses for approval process
    # display_requisition > Print out requisition summary
        # Why it matters? : If I need to change the item logic or approval system, I only update one method. This would help me keeping my code clean as easy to maintain

# Modularity
    # EG. add_or_remove_items & evalutate_approval > these codes split into distinct methods, each block is modular.
        # Why it matters? : Modular code is easiest to test, reuse, and debug. I can reuse these functions in another system without rewriting

# DRY (Don't Repeat Yourself)
    # Instead of me repeating, I used loops and shared methods:
        # I use one loop to handle both adding and removing items
        # The requisition ID is Auto incremented with a counter
        # Data is updated in on place
            # Why it matters? : Implementing this reduces bugs and make updates much easier. Change one peice of logic, and it works all around

# Encapsulation 
    # I used a class *RequisitionSystem* to group data and what happens:
        # Variables like self.items, self.total, and self.status are protected inside the object
        # the class also stores all requisition using *RequisitionSystem* more reliable and secure

# Maintainability
    # I used variables which have clear and straight foward names eg. staff_name, approval_refrence, and requisition_id) and my code flow is quit logical
        # I used:
            # .title to format names
            # try/except to validate user's input
            # class level list to keep track of all the requisition
        # Why it matters? : In the future if i'm willing to collab or get help from other developer, they can easily read, understand, and edit/improves my code

# Readability
    # I used :
        # Clear mothod and variable names
        # Spaced out code with comments 
        # Logical prompt
        # Why it matters? : Readible code is obvoiusly easier to look at, debug, and extend this would help me alot for training to become a professional development

# Error handling
    # from : try:
    #            price = float(input(f"Cost of {item}:$ "))
    # this catches most invalid inputs so that my program doesn't crash easily
        # Why it matters? : Good programs should be able to hand mistakes properly



#   Import RegEx
#   for staff ID validation

import re

#   RequisitionSystem class
#   this class will be used to create a requisition system
#   and also to store the requisition data
#   and to display the requisition statistics

class RequisitionSystem:
    
    #   requisition counter starts at 10000
    #   this will be used to generate the requisition ID
    #   requisitions list will be used to store all the requisitions
    #   this will be used to store the requisition data
    
    requisition_counter = 10000
    requisitions = []
    
#   requisition system
    # SRP v
    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name.title()
        self.requisition_id = RequisitionSystem.requisition_counter + 1
        RequisitionSystem.requisition_counter += 1
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"
        RequisitionSystem.requisitions.append(self)

#   start of requisiton system, for approval
#   changed this from my part A now you're able to add and remove items from the requisition
#   also
    # SRP v
    def add_or_remove_items(self):
        
        self.current_items = 0
        
        print("\nAdd or Remove Requisition Items:")
        
        while True:
            print("\nOptions: [add] Add Item, [remove] Remove Item, [done] Finish")
            action = input("Choose action: ").lower()

            if action == "add":
                item = input("\nItem name: ")
                try:
                    price = float(input(f"Cost of {item}: $"))
                    if price <= 0:
                        raise ValueError
                    self.items.append((item, price))
                    self.total += price
                    self.current_items += 1
                    print(f"\n{item} added with cost of ${price}")
                    print(f"You have entered {self.current_items} items")
                    print(f"Current item(s): {', '.join([i[0] for i in self.items])}")
                    print(f"Total cost: ${self.total:.2f}")
                except ValueError:
                    print("Invalid price. Must be a positive number.")

            elif action == "remove":
                if not self.items:
                    print("No items to remove.")
                    continue
                for i, (item, price) in enumerate(self.items):
                    print(f"\n{i + 1}. {item} - ${price}")
                try:
                    index = int(input("\nEnter item number to remove: ")) - 1
                    print(f"\nRemoving item number {index + 1}...\n")
                    if 0 <= index < len(self.items):
                        removed_item = self.items.pop(index)
                        self.total -= removed_item[1]
                        print(f"{removed_item[0]} has been removed.")
                        print(f"Current item(s): {', '.join([i[0] for i in self.items])}")
                        print(f"Total cost: ${self.total:.2f}")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Please enter a valid number.")

            elif action == "done":
                if not self.items:
                    print("Please add at least one item before finishing.")
                    continue
                break
            else:
                print("Invalid option. Type 'add', 'remove', or 'done'.")
    # SRP v     
    def evaluate_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
        else:
            self.status = "Pending"
#   end of requisiton system, for approval

#   respond to requisition            
    def respond_requisition(self):
        if self.status == "Pending":
            print(f"\nRequisition {self.requisition_id} is pending.")
            response = input("Manager response (A = Approved / NA = Not Approved / leave blank status will remain as 'Pending'): ").lower()
            if response == "A":
                self.status = "Approved"
                self.approval_reference = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
            elif response == "NA":
                self.status = "Not approved"
                self.approval_reference = "Not available"
            else:
                print("Status will remain as pending!")
                
#   display requisition
#   also imported most of display print features from my Part A code
    # SRP v
    def display_requisition(self):
        print("\nPrinting Requisition:")
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference}")
        print("-" * 30)

#   static method to display statistics
#   this method will display the total number of requisitions the exact same as what output was in Canvas
    @staticmethod
    def display_statistics():
        total = len(RequisitionSystem.requisitions)
        approved = sum(1 for r in RequisitionSystem.requisitions if r.status == "Approved")
        pending = sum(1 for r in RequisitionSystem.requisitions if r.status == "Pending")
        not_approved = sum(1 for r in RequisitionSystem.requisitions if r.status == "Not approved")
        print("\nDisplaying the Requisition Statistics")
        print(f"The total number of requisitions submitted: {total}")
        print(f"The total number of approved requisitions: {approved}")
        print(f"The total number of pending requisitions: {pending}")
        print(f"The total number of not approved requisitions: {not_approved}")

#   staff info start of process>
#   took the get_valid_date code from Part A and added somemore function to it
def get_valid_date():
    while True:
        try:
            while True:
                day = input("\nPlease enter the date (1-31): ")
                if day.isdigit() and 1 <= int(day) <= 31:
                    break
                else:
                    print("Invalid date. Please enter a valid date between 1 and 31.")
            while True:
                month = input("Please enter the month (1-12): ")
                if month.isdigit() and 1 <= int(month) <= 12:
                    break
                else:
                    print("Invalid month. Please enter a valid month between 1 and 12.") 
            while True:
                year = input("Please enter the year: ")
                if year == "2024":
                    break
                else:
                    print("Invalid year. This year is 2024.")
                    continue
                
            date = f"{int(day):02}/{int(month):02}/{year}"
            return date
        except ValueError:
            print("Invalid input. Please try again.")

#   Get staff ID now only accepts 2 letters followed by 2 numbers
#   and also added a while loop to check if the input is valid
#   and if not it will ask the user to try again

def get_valid_staff_id():
    while True:
        staff_id = input("\nEnter staff ID (2 letters followed by 2 numbers): ").upper()
        if re.match(r'^[A-Z]{2}[0-9]{2}$', staff_id):
            return staff_id
        else:
            print("Invalid Staff ID. please try again using 2 letters followed by 2 numbers.")


def staff_info():
    print("Welcome to the Fully Interactive Requisition System")
    while True:
        print("\nNew Requisition")
        date = get_valid_date()
        staff_id = get_valid_staff_id()
        first_name = input("\nEnter staff first name: ").capitalize()
        last_name = input("Enter staff last name: ").capitalize()
        staff_name = f"{first_name} {last_name}"

        req = RequisitionSystem(date, staff_id, staff_name)
        req.add_or_remove_items()
        req.evaluate_approval()
        req.display_requisition()

        again = input("Do you want to add another requisition? (yes/no): ").lower()
        if again != "yes":
            break

    for req in RequisitionSystem.requisitions:
        if req.status == "Pending":
            req.respond_requisition()

    for req in RequisitionSystem.requisitions:
        req.display_requisition()

    RequisitionSystem.display_statistics()
    
staff_info()
#   <staff info end of process
