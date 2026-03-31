# Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name
# object initializes id and name dynamically for every Employee object created.
#
# emp = Employee(1, "coder")
# Use del property to first delete id attribute and then the entire object

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.__name = name

    def display(self, id):
        print(f"your id is {self.id}")

    def get_info(self, name):
        return self.__name

emp = Employee(1, "santosh")
emp.display(12)
print(emp.get_info("samuel"))

