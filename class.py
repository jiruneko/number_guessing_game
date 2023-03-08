class Person:
    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age

imanishi = Person('今西', '日本', 25)
print(imanishi.name)
print(imanishi.age)

mike = Person('マイク', 'アメリカ', 13)
print(mike.nationality)
