class CommissionEmployee:
    def __init__(self, first_name, last_name, sales, commission_rate):
        self.first_name = first_name
        self.last_name = last_name
        self.sales = sales
        self.commission_rate = commission_rate

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value.isalpha():
            raise ValueError("First name must contain only alphabetic characters.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value.isalpha():
            raise ValueError("Last name must contain only alphabetic characters.")
        self._last_name = value

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        if value < 0:
            raise ValueError("Sales cannot be negative.")
        self._sales = value

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        if value < 0:
            raise ValueError("Commission rate cannot be negative.")
        self._commission_rate = value

    def earnings(self):
        return self.sales * self.commission_rate

    def __repr__(self):
        return f"CommissionEmployee({self.first_name}, {self.last_name}, Sales: {self.sales}, Commission Rate: {self.commission_rate})"


try:
    employee = CommissionEmployee("John", "Doe", 5000, 0.10)
    print(f"Earnings of {employee.first_name} {employee.last_name}: ${employee.earnings()}")

    employee.sales = 6000
    print(f"Updated Earnings of {employee.first_name} {employee.last_name}: ${employee.earnings()}")

    employee.sales = -1000
except ValueError as e:
    print(f"Error: {e}")

try:
    employee.commission_rate = -0.05
except ValueError as e:
    print(f"Error: {e}")