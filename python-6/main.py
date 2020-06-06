from abc import abstractmethod, ABC

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return 8  
    
    def set_department(self, department):
        self.__department.name = department
    
    def get_department(self):
        return self.__department.name
 
class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers',500))


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers',600))
        self.__sales = 0
    
    def calc_bonus(self):
        return self.__sales * 0.15
        
    def get_sales(self):
        return self.__sales
    
    def set_sales(self, sales):
        self.__sales = sales

    def put_sales(self,sales):
        self.__sales += sales
