class Student:
    def __init__(self, name, score):
        """Initialize a student with name and score."""
        self.name = name
        self.score = score


class Gradebook:
    def __init__(self):
        """Initialize an empty gradebook."""
        self.students = []  # Composition: Gradebook contains Students

    def add_student(self, student):
        """Add a student object to the gradebook."""
        self.students.append(student)

    def get_average(self):
        """Calculate and return the average score of all students."""
        if not self.students:  # Handle empty gradebook
            return 0

        total_score = 0
        for student in self.students:
            total_score += student.score

        return total_score / len(self.students)


# Create a gradebook
math_class = Gradebook()

# Add students to the gradebook
math_class.add_student(Student("Alice", 95))
math_class.add_student(Student("Bob", 87))
math_class.add_student(Student("Charlie", 92))
math_class.add_student(Student("Diana", 78))

# Calculate average
average = math_class.get_average()
print(f"Class average: {average:.2f}")  # Class average: 88.00

# Test with more students
math_class.add_student(Student("Eve", 100))
new_average = math_class.get_average()
# Updated class average: 90.40
print(f"Updated class average: {new_average:.2f}")

# Test empty gradebook
empty_gradebook = Gradebook()
# Empty gradebook average: 0
print(f"Empty gradebook average: {empty_gradebook.get_average()}")

# Alternative way to add students (chaining)
history_class = Gradebook()
history_class.add_student(
    Student("Frank", 85)).add_student(Student("Grace", 91))

# History class average: 88.00
print(f"History class average: {history_class.get_average():.2f}")

# Access individual students
print("\nStudent details:")
for student in math_class.students:
    print(f"{student.name}: {student.score}")
