employee_id,basic_salary,allowance=1001,15000,6000
gross_salary=basic_salary+allowance
if gross_salary<5000:
    income_tax='nil'
elif gross_salary<5000 and gross_salary>1000:
    income_tax=gross_salary*10/100
elif gross_salary<10000 and gross_salary>20000:
    income_tax=gross_salary*20/100
else:
    income_tax=gross_salary*30/100
net_salary=gross_salary-income_tax
print("employee_id:",employee_id)
print("\nbasic_salary:",basic_salary)
print("\nallowance:",allowance)
print("\ngross_salary:",gross_salary)
print("\nincome_tax:",income_tax)
print("\nnet_salary:",net_salary)
    
