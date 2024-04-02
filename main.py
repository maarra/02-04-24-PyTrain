class Student:

  spec = 'devOps'  # spolecna vlastnost pro vsechny objekty
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_msg(self):
    print(f'\nMoje jméno je {self.name} a můj věk je {self.age}')

  def say_hi(self, pozdrav):
    print(f'\n{pozdrav}, já jsem {self.name}')


student1 = Student('Adam', 55)
student1.show_msg()

student2 = Student('Osel', 99)
student1.say_hi('Ahoj')
student2.say_hi('Dobrý den')

# student1 = Student('Pavel', 2000)
#
# print(student1.name)
#
# student2 = Student('Adam', 1999)
# print(student2.age)
# print(student2.name)
# print(student2.spec)
#
# student2.name = 'Petr'
# print(f'Nové jméno je {student2.name}')

