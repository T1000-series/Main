
class Employee:

    raise_amt = 1.04
    num_employees = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

                
        
#class Manager(Employee):
#    def __init__(self, first, last, pay, employees=None):
  #      Employee.__init__(self, first, last, pay)
        #super().__init__(first, last, pay) (doesn't work in this version of python. 
        #print ('RIGHT HERE')
        #if employees is None:
            #self.employees = []
        #else:
            #self.employees = employees

        #def add_emp(self, emp):
           # if emp not in self.employees:
            #    self.employees.append(emp)

       # def remove_emp(self, emp):
     #       if emp in self.employees:
    #            self.employees.remove(emp)

     #   def print_emps(self):
       #     for emp in self.employees:
         #       print('-->', emp.fullname())

 
    

import datetime
my_date =datetime.date(2016, 7, 11)



emp_str_1 = 'John-Doe-70000' 
emp_str_2 = 'Stan-Smith-30000'
emp_str_1 = 'Jane-Doe-90000'
dev_1 = Developer('Corey', 'Schafer', 50000, 'python')
dev_2 = Developer(('Test', 'User', 60000, 'java')
#emp_1 = Employee('Chase', 'Austin', 60000)

#mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
#Manager.add_emp(dev_2)
#Manager.print_emps(mgr_1)

                  
#dev_2 = Employee('Test', 'User', 60000)

new_emp_1 == Employee.from_string(emp_str_1)
Employee.set_raise_amt(1.05)



#print (mgr_1.email)

#print (dev_1.email)
#print (dev_1.prog_lang)

#print (dev_1.pay)
#dev_1.apply_raise()
#print (dev_1.pay)

#print (help(Developer))
#print (Employee.is_workday(my_date))
#print(Employee.raise_amt)
#print (new_emp_1.fullname())
#print (emp_1.raise_amt)
#print (emp_1.pay, emp_2.pay)

