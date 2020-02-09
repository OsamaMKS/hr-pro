from datetime import datetime

class Employee:
   #Employee class here
   def __init__(self,name,age,salary,employment_year):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_year = employment_year


   def get_working_years(self):

       today = datetime.now()
       yearExp = (today.year) - int(self.employment_year)

       return (int(yearExp))

class Manager(Employee):
    #Manager class here

    def __init__(self,name,age,salary,employment_year,bonus_percentage):
        #super().__init__(name,age,salary,employment_year)
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        x = self.salary * self.bonus_percentage
        return (float(x))


def main():


    emp=[]
    mang=[]
    x=""
    while x != 5:
        print("Options:")
        print("1. Show Employees")
        print("2. Show Managers")
        print("3. Add An Employee")
        print("4. Add A Manager")
        print("5. Exit")
        print()
        x = int(input("What would you like to do?"))
        if x == 1:
            for i in emp :
                print(i)

        elif x == 2 :
            for i in mang:
                print(i)

        elif x == 3 :
            name = input("Name: ")
            age = int(input("Age: "))
            salary = float(input("Salary: "))
            employment_year = int(input("Employment year: "))
            r = Employee(name,age,salary,employment_year)
            emp.append({"name":str(r.name),"age":r.age,"salary":r.salary,"Work Experience":Employee.get_working_years(r)})
            print("Employee added succesfully")
            print()

        elif x == 4 :
            name = input("Name: ")
            age = int(input("Age: "))
            salary = float(input("Salary: "))
            employment_year = int(input("Employment year: "))
            bouns = float(input("Bouns Percentage: "))
            t = Manager(name,age,salary,employment_year,bouns)
            mang.append({"name":t.name,"age":t.age,"salary":t.salary,"Work Experience":Employee.get_working_years(t),"Bouns":Manager.get_bonus(t)})
            print("Manager added succesfully")
            print()

        elif x == 5:
            break

if __name__ == '__main__':
    main()
