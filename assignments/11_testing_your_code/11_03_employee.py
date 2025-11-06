class Employee:
    """A class to represent an employee."""
    
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee with first name, last name, and annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, amount=5000):
        """Give the employee a raise. Default is $5,000."""
        self.annual_salary += amount


def test_give_default_raise():
    """Test that default raise works correctly."""
    employee = Employee('John', 'Doe', 50000)
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise():
    """Test that custom raise amount works correctly."""
    employee = Employee('Jane', 'Smith', 60000)
    employee.give_raise(10000)
    assert employee.annual_salary == 70000