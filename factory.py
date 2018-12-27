from abc import ABCMeta, abstractmethod

# 单例模式和工厂模式都属于创建型模式

# 简单工厂模式   允许接口创建对象，但不会暴露对象的创建逻辑
# class Animal(metaclass = ABCMeta):
# 	@abstractmethod
# 	def do_say(self):
# 		pass

# class Dog(Animal):
# 	def do_say(self):
# 		print("Bhow Bhow!!")

# class Cat(Animal):
# 	def do_say(self):
# 		print("Meow Meow!!")

# class ForestFactory(object):
# 	def make_sound(self, object_type):
# 		return eval(object_type)().do_say()

# if __name__ == '__main__':
# 	ff = ForestFactory()
# 	animal = input()
# 	ff.make_sound(animal)

# 工厂方法模式 允许接口创建对象, 但使用哪个类来创建对象，则是交由子类决定

# from abc import ABCMeta, abstractmethod

# class Section(metaclass = ABCMeta):
# 	@abstractmethod
# 	def describle(self):
# 		pass

# class PersonalSection(Section):
# 	def describle(self):
# 		print("Personal Section")

# class AlbumSection(Section):
# 	def describle(self):
# 		print("Album Section")

# class PatenSection(Section):
# 	def describle(self):
# 		print("Patent Section")

# class PublicationSection(Section):
# 	def describle(self):
# 		print("Publication Section")


# class Profile(metaclass=ABCMeta):
# 	def __init__(self):
# 		self.sections = []
# 		self.createProfile()

# 	@abstractmethod
# 	def createProfile(self):
# 		pass

# 	def getSections(self):
# 		return self.sections

# 	def addSections(self, section):
# 		self.sections.append(section)

# class linkedin(Profile):
# 	def createProfile(self):
# 		self.addSections(PersonalSection())
# 		self.addSections(PatenSection())
# 		self.addSections(PublicationSection())

# class facebook(Profile):
# 	def createProfile(self):
# 		self.addSections(PersonalSection())
# 		self.addSections(AlbumSection())

# if __name__ == '__main__':
# 	profile_type = input()
# 	profile = eval(profile_type.lower())()
# 	print("Creating Profile..", type(profile).__name__)
# 	print("Profile has sections --", profile.getSections())

# 抽象工厂模式  抽象工厂是一个能够创建一系列相关对象而无需指定/公开其具体类的接口。
# 			   该模式能够提供其他工厂的对象, 在其内部创建其他对象。

from abc import ABCMeta, abstractmethod

class PizzaFactory(metaclass=ABCMeta):
	@abstractmethod
	def createVegPizza(self):
		pass

	@abstractmethod
	def createNonVegPizza(self):
		pass

class IndianPizzaFactory(PizzaFactory):
	def createVegPizza(self):
		return DeluxVeggiePizza()

	def createNonVegPizza(self):
		return ChickenPizza()

class USPizzaFactory(PizzaFactory):
	def createVegPizza(self):
		return MexicanVegPizza()

	def createNonVegPizza(self):
		return HamPizza()


class VegPizza(metaclass=ABCMeta):
	@abstractmethod
	def prepare(self, VegPizza):
		pass

class NonVegPizza(metaclass=ABCMeta):
	@abstractmethod
	def serve(self, VegPizza):
		pass

class DeluxVeggiePizza(VegPizza):
	def prepare(self):
		print("Prepare ", type(self).__name__)

class ChickenPizza(NonVegPizza):
	def serve(self, VegPizza):
		print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
	def prepare(self):
		print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza):
	def serve(self, VegPizza):
		print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)



class PizzaStore:
	def __init__(self):
		pass

	def makePizzas(self):
		for factory in [IndianPizzaFactory(), USPizzaFactory()]:
			self.factory = factory
			self.NonVegPizza = self.factory.createNonVegPizza()
			self.VegPizza = self.factory.createVegPizza()
			self.VegPizza.prepare()
			self.NonVegPizza.serve(self.VegPizza)

pizza = PizzaStore()
pizza.makePizzas()
