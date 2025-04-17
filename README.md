# IT5016_Assessment3_20250575

Commentary on Programming Principles and Design Concepts

Based from my Requisition 2.py program, the script represents a practical implementation of several core software design principles within the real world task management context. The purpose of the system is to allow staff to create and manage requisitions for items, with the ability to track details like staff names, requisition IDs, total costs, and statuses. The program is built  using object oriented programming, which is a widely recommended approach for designing scalable and maintainable applications.

1. Single Responsibility Priciple (SRP)
My codes follows the SRP quite well. The priciple suggests that each class or function of my code should have only one reason to change. The *RequisitionSystem* class is focused on a single responsibility, managing requisition. Each method within the class (add_or_remove_items, evaluate_approval, and display_requisition) handles their own task. This seperation improves maintainability, if any of the parts of the item handling process needs to change in the future, it can be done within the isolation without affecting unrelated functionality like approval or display logic.

2. Modularity
Modularity is another strength of my implemetation. The entire system is encapsulated inside a single class, and the methods within that class each deal with specific action. The use of modular functions not only makes the code easier to understand but also easier to test and debug. For example, the logic to add or remove requisition items is to contained within its own loop driven method, reducing code duplication and making sure the code is clear and simple for reader to understand. This makes the system much is easier to extend/expand in the future if needed, for example adding a method for saving data to a file wouldn't interfere with the rest if the programs actions/behavior.

3. DRY (Don't Repeat Yourself)
My program mostly follows the DRY principle, where common logic is reused rather than repeated. For instance, rather than writing seperate logic to handle user inputs and total calculations multiple times, these operations are cleanly grouped in loop inside the add_or_remove_items method, however I do see some place where it could be improves. For instance, Validation logic could be extracted into seperate utility functions to reduce anymore duplication and this would improve testability.

4. Encapsulation
The program uses class level and instance level variables effecively. The use of self.items, self.status, and self.total encapsulates each requisition's state within its own object. This aligns with the Encapsulation principle, one of the key pillars of object oriented design. It hides the internal implementation details of each requisition from the user or other part of the program, which improves reliability and reduces unintended side effects.

5. Maintainability & Readability
I'd say my code is fairly readable, especially me adding in comments would help a little bit for user/co-worker to understand the purpose of the code. I made sure all of my variables name are clear and simple (for example : staff_name, requisition_id, approval_refrence), and method names describe exactly what it's for based from what they do. The use of title() to format staff names adds a nice touch of data standardisation, which is crucial in real industry / real world system.
The use of class level variables like *requisition_counter* and *requisition* also helps with the maintainability. For Example, it would be pretty easy to generate reports or track all requistions in the future since they're stored in shared list.

6. Error Handling
I tried my best to use *try* except blocks to validate user input for prices and ensures that only valid numbers will be accepted. This helps towards the robustness of the system. While it could be improved with more comprehensive validation functions or regular expressions for feild like *staff id*, the existing logic demonstrates a strong foundation.

7. Things that could be improved
- Based from the feedback I got from Ciar after summiting the assestment 2 part b : unfortunately the "respond_requisitions" didn't work as the manager was unable to change status from *Pending*
    From that the possible out come is to remove ".lower"
- Reusability : some logic for example adding items, and calculating totals. Those could be turned into a smaller helper methods.
- Testing : The code could benefit from being wrapped in functions to allow for unit testing

Conclusion
In conslusion, I think overall, the *RequisitionSystem* class showcase thoughful application of software design priciples. It is modular, readable, and quite structured in a way that makes it easy to maintain and expand. With a few improvements around reusability and utility funtions, it honestly could be more optimised for real world / real industry deployment. This code demonstrates a solid understanding of OOP and core programming practices, So this would be perfect for this Assessment (Assessment 3).
