class Person:
    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age

    def __call__(self):
        print('ここはcall関数です')
    
    def say_hello(self,name):
        print('こんにちは、{}さん。私は{}です。'.format(name,self.name))

imanishi = Person('今西','日本',25)
imanishi()

print(imanishi.nationality)

print(imanishi.age)

mike = Person('マイク','アメリカ',13)
print(mike.name)
print(imanishi.say_hello('佐藤'))
print(mike.say_hello('佐藤'))