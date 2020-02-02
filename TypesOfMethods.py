
class student:

    school = 'Euroschool'

    def __int__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1,self.m2,self.m1)/3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print('this is stuedent class')


s1 = student()

print(s1.avg())
print(student.getschool())
student.info()