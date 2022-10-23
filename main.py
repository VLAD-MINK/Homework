# from random import *

# class University:
#   def __init__(self, title, faculty):
#     self.title = title
#     self.faculty = faculty
#     self.budget = False;
#   def check_progress(self, student):
#     if student > 3:
#       self.budget = True 
#       student.money += 20
#   def isbudget(self):
#     if self.budget == True:
#       print('Are you on budget&')
  
# # №1
# class Student:
#   def __init__(self, name):
#     self.name = name
#     self.gladness = 30
#     self.progress = 0
#     self.money = 100
#     self.figure = 60
#     self.alive = True
    
#   def study(self):
#     print('Stude time')
#     self.progress +=0.15
#     self.gladness -= 3
#     self.money -= 10
#     self.figure += 1
#   def ask_budget(self, university):
#     university.check_progress(self.progress)
    
#   def sleep(self):
#     print('Sleep time')
#     self.gladness += 2
#     self.figure += 0.5
    
#   def chill(self):
#     print('Cheel time')
#     self.progress -=0.12
#     self.gladness += 5
#     self.money -= 40
    
#   def work(self):
#     print('work time')
#     self.gladness -= 2
#     self.money += 60
#     self.figure -=1.5
    
#   def sport(self):
#     print('sport time')
#     self.figure -=2.5
#     self.money -5
#     self.gladness += 5
    
#   def is_alive(self):
#     if self.progress < -0.5:
#       print('So bad. Studyless!')
#       self.alive = False
#     elif self.gladness <= 0:
#       print('Depression...')
#       self.alive = False
#     elif self.progress > 5:
#       print('Passed the exam!')
#       self.alive = False
#     elif self.money < 0:
#       print('Homeless! Studyless!')
#       self.alive = False
#     elif self.money <= 10:
#       print('No money')
#       print('work time')
#       self.gladness -= 6
#       self.money += 30
#     elif self.figure >= 120:
#       print('Fatty!')
#       self.alive = False
#   def end(self):
#     print ('Gladness',self.gladness)
#     print ('Progress',self.progress)
#     print ('Money',self.money)
#     print ('figure',self.figure)
#   def live(self, day):
#     print('Day', day)
#     live_cube = randint(1,4)
#     if day % 10 == 0:
#       self.ask_budget(univer)
#     if live_cube == 1:
#       self.study()
#     elif live_cube == 2:
#       self.sleep()
#     elif live_cube == 3:
#       self.chill()
#     elif live_cube == 4:
#       self.work()
#     elif live_cube == 4:
#       self.sport()
#     self.end()
#     self.is_alive()
    
# obj = Student('Bob')
# univer = University('Step univer', 'comp')
# for day in range(270):
#   if obj.alive == False:
#     break
#   obj.live(day)


# # №2


# class Holidayer:
#   def Student(self):
#     if Student.alive == False:
#       self.Holidayer = False
#   def __init__(self, name):
#     self.name = name
#     self.gladness = 30
#     self.money = 100
#     self.figure = 60
#     self.alive = True
#   def study(self):
#     print('Stude time')
#     self.gladness -= 3
#     self.figure += 1
#   def sleep(self):
#     print('Sleep time')
#     self.gladness += 2
#     self.figure += 1
#   def chill(self):
#     print('Cheel time')
#     self.gladness += 5
#     self.money -= 50
#   def work(self):
#     print('work time')
#     self.gladness -= 2
#     self.money += 60
#     self.figure -=1.5
#   def sport(self):
#     print('sport time')
#     self.figure -=4
#     self.money -10
#     self.gladness += 5
#   def is_alive(self):
#     if self.gladness <= 0:
#       print('Depression...')
#       self.alive = False
#     elif self.money < 0:
#       print('Homeless! Studyless!')
#       self.alive = False
#     elif self.money <= 10:
#       print('No money')
#       print('work time')
#       self.gladness -= 6
#       self.money += 30
#     elif self.figure >= 120:
#       print('Fatty!')
#       self.alive = False
#   def live(self, day):
#     print('Day', day)
#     live_cube = randint(5,8)
#     if live_cube == 5:
#       self.sleep()
#     elif live_cube == 6:
#       self.chill()
#     elif live_cube == 7:
#       self.work()
#     elif live_cube == 8:
#       self.sport()
#     self.is_alive()
# obj = Holidayer('Bob')
# for day in range(90):
#   if obj.alive == False:
#     break
#   obj.live(day)





# class Human:
#   def __init__(self, name):
#     self.name = name
#     self.gender = 'None'
#     self.age = 0
#   def happybirthday(self):
#     self.age += 1
#     print('I am', self.age)
#   def live(self):
#     print(self.name, 'is alive')
#   def eat():
#     print('i am eating')
    
# class Parent(Human):
#   def work(self):
#     print(self.name, 'i can work')
#   def eat(self):
#     print(self.name, 'i am eating')
    
    
# class Child(Human):
#   def happybirthday(self):
#     self.age += 1
#     print('I am', self.age)
#   def study(self):
#     print(self.name, 'I can study')

# obj = Child('Bob')
# obj.study()
# obj.live()
# obj.happybirthday()
# obj.happybirthday()
# obj.happybirthday()

# obj2 = Parent('Janu')
# obj2.eat()
# obj2.work()
# for i in range(30):
#   obj2.happybirthday()



class Animal:
  def __init__(self, name):
    self.name = name
    self.gender = 'None'
    self.age = 0
  def happybirthday(self):
    self.age += 1
    print('one year more' ,self.age)
  def toilet(self):
    print(self.name,'owner i want go to a toilet')
  def eat(self):
    print(self.name,'owner, i want eat')
    
class Cat(Animal):
  def lazy(self):
    self.lazy
    print(self.name,'i want sleep')
    
  def madness(self):
    self.madness
    print(self.name,'maaaaaaay!!!!!!!!!!!error!')

class Dog(Animal):
  def attachment1(self):
    self.attachment += 1
    print(self.name,'Gav Gav!')
    if self.attachment >= 15:
      print('Fell in love')
  def angry1(self):
    self.angry -= 1
    print('GAV GAV GAV!!!!!!')
    if self.angry <=5:
      print('i am not angry')
  def play(self):
    print(self.name,'Plaing!!!')
  def __init__(self,name):
        super().__init__(name)
        self.attachment = 0
        self.angry = 20
  

class Hamster(Animal):
  def run_in_the_circle1(self):
    self.run_in_the_circle += 5
    print(self.name, 'Run Run!')
    if self.run_in_the_circle >= 50:
      print('I want cill')
  def __init__(self,name):
        super().__init__(name)
        self.run_in_the_circle = 0


obj = Cat('Rygic')
obj.lazy()
obj.madness()

for i in range(20):
  obj.happybirthday()

obj1 = Dog('Bobby')

for i in range(20):
  obj1.happybirthday()
  obj1.attachment1()
  obj1.angry1()

obj2 = Hamster('Dolboybic')

for i in range(20):
  obj2.happybirthday()
  obj2.run_in_the_circle1()