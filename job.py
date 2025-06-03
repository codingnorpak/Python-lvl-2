
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, job):
        super().__init__(name, salary)  
        self.job = job

    def display_welcome_message(self):
        
     print("we would like to welcome you to the airline,", self.name, "and we give you a salary of", self.salary, "every month!")

manager1 = Manager("Arham", 85000, "Piloting")
manager1.display_welcome_message()
