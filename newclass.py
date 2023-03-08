class Person:
  def __init__(self, name):
    self.name = name
    print(self.name)

  def say_something(self):
    print('I am {} ,hello'. format(self.name))


person = Person('ken')
person.say_something()
