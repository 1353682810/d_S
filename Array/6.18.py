class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print('{} can study hardly'.format(self.name))


stu = student('xiaoming', 20)
print(stu.name)
print(stu.age)
stu.study()
