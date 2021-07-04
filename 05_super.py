class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am Breathing....")


class Employee:
    company = "Honda"


    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        # super().takeBreath()
        print("I am a Employee so I am luckily Breathing.")


class Proggrammer(Employee):
    commpaqny = "Fiver"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am a programmer so I am Breathing ++ ..")


# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Proggrammer()
# pr.takeBreath()

