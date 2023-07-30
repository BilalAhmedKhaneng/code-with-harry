class Employee:
    def __int__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"the name of employee: {self.id}is{self.name}")

        class programmer(Employee):
            def showlanguage(self):
                print("the default laguage")


        a=Employee("bilal,220")
