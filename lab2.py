class Student:
    def __init_(self,name,age,usn):
        self.name=name
        self.age=age
        self.usn=usn

    def getdata(self):
        try: 
            self.name=input("enter name")
        except Exception as e:
            print(e)
        try:
            self.age=input("enter age")
        except Exception as e:
            print(e)
        try:
            self.usn=input("enter usn")
        except Exception as e:
            print(e)


class derived(Student):
    def __init__(self):
        super().__init__()
        self.s1=0
        self.s2=0
        self.s3=0

    def getmarks(self):
        super().getdata()   
        try:
            self.s1=int(input("enter s1"))
            self.s2=int(input("enter s2"))
            self.s3=int(input("enter s3"))
        except Exception as e:
            print(e)


class derived2(derived):
    def __init__(self):
        super().__init__()
    
    def display(self):
        super().getmarks()
        self.total=self.s1+self.s2+self.s3
        self.percentage=self.s1+self.s2+self.s3
        #(self.name)
        print(self.total/2)
        print(self.total)



d=derived2()
d.getmarks()
d.display()

#s=10 s=0
#s=s.upper()
#s1=hello