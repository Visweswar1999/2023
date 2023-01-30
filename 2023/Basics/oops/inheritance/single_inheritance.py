#single inheritance

#parent class

class Organization:
    def org_details(self,name,number):
        self.name = name
        self.number = number
    def org_show(self):
        print("organization name is",self.name,"organization number is",self.number)
#parent class
class Employee():
    def Emp_details(self,name,id):
        self.name = name
        self.id = id
    def emp_show(self):
        print("employee name is ",self.name,"employee id is",self.id)

#child class
class Kiran(Organization,Employee):
    def kiran_class(self):
        print("inside the kiran class")

object1 = Kiran()
object1.org_details("dell","2345")
object1.Emp_details("ramesh","876")
object1.emp_show()
object1.org_show()



