# 模板方法模式

# from abc import ABCMeta, abstractmethod

# class Compiler(metaclass=ABCMeta):
# 	@abstractmethod
# 	def collectSource(self):
# 		pass

# 	@abstractmethod
# 	def compileToObject(self):
# 		pass

# 	@abstractmethod
# 	def run(self):
# 		pass

# 	def compileAndRun(self):
# 		self.collectSource()
# 		self.compileToObject()
# 		self.run()

# class iOSCompiler(Compiler):
# 	def collectSource(self):
# 		print("Collecting Swift Source Code")

# 	def compileToObject(self):
# 		print("Compiling Swift code to LLVM bitcode")

# 	def run(self):
# 		print("Program runing on runtime environment")

# iOS = iOSCompiler()
# iOS.compileAndRun()

# from abc import ABCMeta, abstractmethod

# class AbstractClass(metaclass=ABCMeta):
# 	def __init__(self):
# 		pass

# 	@abstractmethod
# 	def operation1(self):
# 		pass

# 	@abstractmethod
# 	def operation2(self):
# 		pass

# 	def template_method(self):
# 		print("Defining the Algorithm. Operation1 follows Operation2")
# 		self.operation2()
# 		self.operation1()

# class ConcreteClass(AbstractClass):
# 	def operation1(self):
# 		print("My Concrete Operation1")

# 	def operation2(self):
# 		print("Operation 2 remains same")

# class Client:
# 	def main(self):
# 		self.concreate = ConcreteClass()
# 		self.concreate.template_method()

# client = Client()
# client.main()

from abc import abstractmethod, ABCMeta

class Trip(metaclass=ABCMeta):
	@abstractmethod
	def setTransport(self):
		pass

	@abstractmethod
	def day1(self):
		pass

	@abstractmethod
	def day2(self):
		pass

	@abstractmethod
	def day3(self):
		pass


	@abstractmethod
	def returnHome(self):
		pass

	def itinerary(self):
		self.setTransport()
		self.day1()
		self.day2()
		self.day3()
		self.returnHome()

class VeniceTrip(Trip):
	def setTransport(self):
		print("Take a boat and find your way in the Grand Canal")

	def day1(self):
		print("Visit St Mark's Basilica in St Mark's Square")

	def day2(self):
		print("Appreciate Doge's Palace")

	def day3(self):
		print("Enjoy the food near the Rialto Bridge")

	def returnHome(self):
		print("Get souvenirs for friends and get back")

class MaldivesTrip(Trip):
	def setTransport(self):
		print("On foot, on any island, Wow!")

	def day1(self):
		print("Enjoy the marine life of Banana Reef")

	def day2(self):
		print("Go for the water sports and snorkelling")

	def day3(self):
		print("Relax on the beach and enjoy the sun")

	def returnHome(self):
		print("Dont't feel like leaving the beach..")

class TravelAgency:
	def arrange_trip(self):
		choice = input("What kid of place you'd like to go historical or to a beach?")
		if choice == 'historical':
			self.trip = VeniceTrip()
			self.trip.itinerary()
		if choice == 'beach':
			self.trip = MaldivesTrip()
			self.trip.itinerary()

TravelAgency().arrange_trip()