class Animal:
	def __init__(self, name, age):
		self.name= name
		self.age= age
	def sleep(self):
		print self.name , "of" , self.age , "years old is sleeping"
	def eat(self):
		print self.name ,  "of" , self.age , "years old is having Mansaf for lunch"

class Bird(Animal):
	def __init__(self, wings_color, name, age):
		Animal.__init__(self, name, age)		
		self.wings_color = wings_color
	def fly(self):
		print self.name , "of" , self.age , "years old" , "who has" , self.wings_color , "wings is flying!" 



class Dog(Animal):
	def __init__(self, num_legs, name, age):
		Animal.__init__(self, name, age)
		self.num_legs = num_legs
	def bark(self):
		print self.name, "of" , self.age , "years old" , "who has" , self.num_legs , "legs is busy barking"






a = Bird("blue", "Aseel", 3)
b= Dog(101, "Khadeejeh", 22)
a.fly() 
b.sleep()
b.bark()
a.sleep()
b.eat()
a.eat()

