from random import *
# №1
class Student:
  def __init__(self, name):
    self.name = name
    self.gladness = 30
    self.progress = 0
    self.money = 100
    self.figure = 60
    self.alive = True
  def study(self):
    print('Stude time')
    self.progress +=0.15
    self.gladness -= 3
    self.money -= 10
    self.figure += 1
  def sleep(self):
    print('Sleep time')
    self.gladness += 2
    self.figure += 0.5
  def chill(self):
    print('Cheel time')
    self.progress -=0.12
    self.gladness += 5
    self.money -= 40
  def work(self):
    print('work time')
    self.gladness -= 2
    self.money += 60
    self.figure -=1.5
  def sport(self):
    print('sport time')
    self.figure -=2.5
    self.money -5
    self.gladness += 5
  def is_alive(self):
    if self.progress < -0.5:
      print('So bad. Studyless!')
      self.alive = False
    elif self.gladness <= 0:
      print('Depression...')
      self.alive = False
    elif self.progress > 5:
      print('Passed the exam!')
      self.alive = False
    elif self.money < 0:
      print('Homeless! Studyless!')
      self.alive = False
    elif self.money <= 10:
      print('No money')
      print('work time')
      self.gladness -= 6
      self.money += 30
    elif self.figure >= 120:
      print('Fatty!')
      self.alive = False
  def end(self):
    print ('Gladness',self.gladness)
    print ('Progress',self.progress)
    print ('Money',self.money)
    print ('figure',self.figure)
  def live(self, day):
    print('Day', day)
    live_cube = randint(1,4)
    if live_cube == 1:
      self.study()
    elif live_cube == 2:
      self.sleep()
    elif live_cube == 3:
      self.chill()
    elif live_cube == 4:
      self.work()
    elif live_cube == 4:
      self.sport()
    self.end()
    self.is_alive()
    
obj = Student('Bob')
for day in range(365):
  if obj.alive == False:
    break
  obj.live(day)


# №2


class holidayer:
  def __init__(self, name):
    self.name = name
    self.gladness = 30
    self.money = 100
    self.figure = 60
    self.alive = True
  def study(self):
    print('Stude time')
    self.gladness -= 3
    self.figure += 1
  def sleep(self):
    print('Sleep time')
    self.gladness += 2
    self.figure += 1
  def chill(self):
    print('Cheel time')
    self.gladness += 5
    self.money -= 50
  def work(self):
    print('work time')
    self.gladness -= 2
    self.money += 60
    self.figure -=1.5
  def sport(self):
    print('sport time')
    self.figure -=4
    self.money -10
    self.gladness += 5
  def is_alive(self):
    if self.gladness <= 0:
      print('Depression...')
      self.alive = False
    elif self.money < 0:
      print('Homeless! Studyless!')
      self.alive = False
    elif self.money <= 10:
      print('No money')
      print('work time')
      self.gladness -= 6
      self.money += 30
    elif self.figure >= 120:
      print('Fatty!')
      self.alive = False
  def live(self, day):
    print('Day', day)
    live_cube = randint(5,8)
    if live_cube == 5:
      self.sleep()
    elif live_cube == 6:
      self.chill()
    elif live_cube == 7:
      self.work()
    elif live_cube == 8:
      self.sport()
    self.end()
    self.is_alive()
obj = Student('Bob')
for day in range(90):
  if obj.alive == False:
    break
  obj.live(day)
