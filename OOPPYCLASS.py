class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Cat name " + abc.name)

p1 = Person("Garfield", 36)

p1.myfunc()