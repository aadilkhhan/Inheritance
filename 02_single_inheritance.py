# DRYT = Do not Repeat Yourself

class Employee:
    commpany = "Google"

    def showDetails(self):
        print("This is an employee")

class Proggrammer(Employee):
    language = "Python"
    # commpany = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an Programmer")

e = Employee()
e.showDetails()
p = Proggrammer()
p.showDetails()
print(p.commpany)
    