from datetime import datetime

class Employee:
   #Employee class here
   Emp=[]
   def __init__(self,name,age,salary,employment_year):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_year = employment_year

       self.Emp.append({"name":self.name,"age":self.age,"salary":self.salary,"Work Experience":Employee.get_working_years(self)})

   def get_working_years(self):

       today = datetime.now()
       yearExp = (today.year) - int(self.employment_year)

       return (int(yearExp))

class Manager(Employee):
    #Manager class here
    Mang=[]
    def __init__(self,name,age,salary,employment_year,bonus_percentage):
        #super().__init__(self,name,age,salary,employment_year)
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
        self.bonus_percentage = bonus_percentage
        self.Mang.append({"name":self.name,"age":self.age,"salary":self.salary,"Work Experience":Employee.get_working_years(self),"Bouns":Manager.get_bonus(self)})

    def get_bonus(self):
        x = self.salary * self.bonus_percentage
        return (float(x))


def main():

    print("Options:")
    print("1. Show Employees")
    print("2. Show Managers")
    print("3. Add An Employee")
    print("4. Add A Manager")
    print("5. Exit")
    print()


    x = int(input("What would you like to do?"))
    if x == 1:
        for i in Employee.Emp :
            print(i)
        main()
    elif x == 2 :
        for i in Manager.Mang:
            print(i)
        main()
    elif x == 3 :
        name = input("Name: ")
        age = int(input("Age: "))
        salary = float(input("Salary: "))
        employment_year = int(input("Employment year: "))
        Employee(name,age,salary,employment_year)
        print("Employee added succesfully")
        print()
        main()

    elif x == 4 :
        name = input("Name: ")
        age = int(input("Age: "))
        salary = float(input("Salary: "))
        employment_year = int(input("Employment year: "))
        bouns = float(input("Bouns Percentage: "))
        Manager(name,age,salary,employment_year,bouns)
        print("Manager added succesfully")
        print()
        main()
    elif x == 5:
         print()

if __name__ == '__main__':
    main()
