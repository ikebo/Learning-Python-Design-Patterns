#  命令模式

# class Wizard:
# 	def __init__(self, src, rootdir):
# 		self.choices = []
# 		self.rootdir = rootdir
# 		self.src = src

# 	def preferences(self, command):
# 		self.choices.append(command)

# 	def execute(self):
# 		for choice in self.choices:
# 			if list(choice.values())[0]:
# 				print("Copying binaries --", self.src, " to ", self.rootdir)
# 			else:
# 				print("No Operation")

# if __name__ == '__main__':
# 	wizard = Wizard("python3.5.gzip", "/usr/bin")
# 	wizard.preferences({'python': True})
# 	wizard.preferences({'java':False})
# 	wizard.execute()

# from abc import ABCMeta, abstractmethod

# class Command(metaclass=ABCMeta):
# 	def __init__(self, recv):
# 		self.recv = recv

# 	def execute(self):
# 		pass

# class ConcreteCommand(Command):
# 	def __init__(self, recv):
# 		self.recv = recv
# 	def execute(self):
# 		self.recv.action()

# class Receiver:
# 	def action(self):
# 		print("Receiver Action")

# class Invoker:
# 	def command(self, cmd):
# 		self.cmd = cmd

# 	def execute(self):
# 		self.cmd.execute()

# if __name__ == '__main__':
# 	recv = Receiver()
# 	cmd = ConcreteCommand(recv)
# 	invoker = Invoker()
# 	invoker.command(cmd)
# 	invoker.execute() 

from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
	@abstractmethod
	def execute(self):
		pass

class BuyStockOrder(Order):
	def __init__(self, stock):
		self.stock = stock

	def execute(self):
		self.stock.buy()


class SellStockOrder(Order):
	def __init__(self, stock):
		self.stock = stock

	def execute(self):
		self.stock.sell()

class StockTrade:
	def buy(self):
		print("You will buy stocks")

	def sell(self):
		print("You will sell stocks")

class Agent:
	def __init__(self):
		self.__orderQueue = []

	def placeOrder(self, order):
		self.__orderQueue.append(order)
		order.execute()

if __name__ == '__main__':
	stock = StockTrade()
	buyStock = BuyStockOrder(stock)
	sellStock = SellStockOrder(stock)

	agent = Agent()
	agent.placeOrder(buyStock)
	agent.placeOrder(sellStock)
