class A:

    def feature1(self):
        print("Feacher 1 is working")

    def feature2(self):
        print("Feacher 2 is working")


class B(A):

    def feature3(self):
        print("Feacher 3 is working")

    def feature4(self):
        print("Feacher 4 is working")

class C(B):

    def feature5(self):
        print("Feacher 3 is working")

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature2()
b1.feature1()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature2()
c1.feature1()
c1.feature3()
c1.feature4()
c1.feature5()
