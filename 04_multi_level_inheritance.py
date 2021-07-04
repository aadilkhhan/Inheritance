class Person:
    country = "India"

    def takeBreath(self):
        print("I am Breathing....")


class Employee:
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am a Employee so I am luckily Breathing.")


class Proggrammer(Employee):
    commpaqny = "Fiver"

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        print("I am a programmer so I am Breathing ++ ..")


p = Person()
p.takeBreath()
# print(p.company) ---> Throws an error

e = Employee()
e.takeBreath()
print(e.company)
pr = Proggrammer()
pr.takeBreath()
print(pr.company)
print(p.country)
