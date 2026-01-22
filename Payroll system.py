class Employee:
    def __init__(self, name, salary):
        """Initialize an employee with name and salary."""
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        """Calculate and return the employee's pay."""
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        """Initialize a manager with name, salary, and bonus."""
        super().__init__(name, salary)  # Call parent class constructor
        self.bonus = bonus

    def calculate_pay(self):
        """Calculate and return the manager's pay including bonus."""
        # Get base salary from parent class method
        base_pay = super().calculate_pay()
        return base_pay + self.bonus


# Example
# Create regular employees
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

# Create managers
manager1 = Manager("Charlie", 80000, 15000)
manager2 = Manager("Diana", 90000, 20000)

# Calculate pays
print(f"{employee1.name}'s pay: ${employee1.calculate_pay():,}")      # $50,000
print(f"{employee2.name}'s pay: ${employee2.calculate_pay():,}")      # $60,000
# $95,000 (80,000 + 15,000)
print(f"{manager1.name}'s pay: ${manager1.calculate_pay():,}")
# $110,000 (90,000 + 20,000)
print(f"{manager2.name}'s pay: ${manager2.calculate_pay():,}")

# Demonstrate inheritance relationships
# True
print(f"\nManager is a subclass of Employee: {issubclass(Manager, Employee)}")
# True
print(f"manager1 is an Employee: {isinstance(manager1, Employee)}")
# False
print(f"employee1 is a Manager: {isinstance(employee1, Manager)}")

# Access inherited attributes
print(f"\nManager's inherited attributes:")
# Accessible from parent class
print(f"{manager1.name}'s base salary: ${manager1.salary:,}")
# Manager-specific attribute
print(f"{manager1.name}'s bonus: ${manager1.bonus:,}")
# $80,000
print(
    f"Base salary via parent method: ${super(Manager, manager1).calculate_pay():,}")

# List with mixed employee types
print(f"\nCompany payroll:")
employees = [employee1, employee2, manager1, manager2]
total_payroll = 0

for emp in employees:
    pay = emp.calculate_pay()  # Polymorphism: correct calculate_pay() called for each type
    total_payroll += pay
    print(f"{emp.name}: ${pay:,}")

print(f"\nTotal payroll: ${total_payroll:,}")  # Total: $315,000
