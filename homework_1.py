#create an list
info=[]

#5 values received from the user and added to the list
name = input("Please enter your name : ")
info.append(name)

lastname = input("Please enter your lastname : ")
info.append(lastname)

#control was done. If the expected value is not entered, it has been requested to be re-entered.
try:
    age = int(input("please enter your age : "))
    info.append(age)
except ValueError:
    age = int(input("Please enter your age in integer type : "))
    info.append(age)


job = input("Please enter your job : ")
info.append(job)

try: 
    salary = float(input("Please enter your salary :"))
    info.append(salary)
except ValueError:
    salary = float(input("Please enter your salary in float type. :"))
    info.append(salary)

#Printing to the screen with the "f-string" method
print(f"Name : {name} \nLast Name : {lastname} \nAge : {age} \nJob : {job} \nSalary : {salary}")

#Value types are print to the screen with the ".format" method.
print("Name type : {} \nLastname type : {} \nAge type : {} \nJob type : {} \nSalary type : {}".format(type(info[0]), type(info[1]), 
                                                                                                      type(info[2]), type(info[3]), 
                                                                                                      type(info[4])))