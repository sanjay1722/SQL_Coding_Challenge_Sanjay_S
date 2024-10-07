'''1. Accept Empid,EmpName,Monthly_Salary,Tot_Deductions, Tot_Allowances
and Display Employee Name and Salary in hand'''
Empid = int(input('Enter Empid: '))
EmpName = input('Enter name: ')
Monthly_Salary = int(input('Enter Salary: '))
Tot_Deductions = int(input('Enter Deductions: '))
Tot_Allowances =  int(input('Enter Total allowances: '))
print('Employee name is {}'.format(EmpName))
print('Employee salary is {}'.format(Monthly_Salary - Tot_Deductions + Tot_Allowances))