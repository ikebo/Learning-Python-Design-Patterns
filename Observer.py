# 观察者模式

# class Subject:
# 	def __init__(self):
# 		self.__observers = []

# 	def register(self, observer):
# 		self.__observers.append(observer)

# 	def notifyAll(self, *args, **kwargs):
# 		for observer in self.__observers:
# 			observer.notify(self, *args, **kwargs)


# class Observer1:
# 	def __init__(self, subject):
# 		subject.register(self)

# 	def notify(self, subject, *args):
# 		print(type(self).__name__, ":: Got", args, "From", subject)

# class Observer2:
# 	def __init__(self, subject):
# 		subject.register(self)

# 	def notify(self, subject, *args):
# 		print(type(self).__name__, ':: Got', args, 'From', subject)


# subject = Subject()
# observer1 = Observer1(subject)
# observer2 = Observer2(subject)
# subject.notifyAll('notification')

class NewsPublisher:
	def __init__(self):
		self.__subscribers = []
		self.__latestNews = None

	def attach(self, subscriber):
		self.__subscribers.append(subscriber)

	def detach(self):
		return self.__subscribers.pop()

	def subscribers(self):
		return [type(x).__name__ for x in self.__subscribers]

	def notifySubscribers(self):
		for sub in self.__subscribers:
			sub.update()

	def addNews(self, news):
		self.__latestNews = news

	def getNews(self):
		return "Got News: ", self.__latestNews


from abc import ABCMeta, abstractmethod

class Subscriber(metaclass=ABCMeta):

	@abstractmethod
	def upate(self):
		pass

class SMSSubscriber:
	def __init__(self, publisher):
		self.publisher = publisher
		self.publisher.attach(self)

	def update(self):
		print(type(self).__name__, self.publisher.getNews())

class EmailSubscriber:
	def __init__(self, publisher):
		self.publisher = publisher
		self.publisher.attach(self)  

	def update(self):
		print(type(self).__name__, self.publisher.getNews())

class AnyOtherSubscriber:
	def __init__(self, publisher):
		self.publisher = publisher
		self.publisher.attach(self)

	def update(self):
		print(type(self).__name__, self.publisher.getNews())

if __name__ == '__main__':
	news_publisher = NewsPublisher()
	for Subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
		Subscriber(news_publisher)

	print("Subscriber:", news_publisher.subscribers())

	news_publisher.addNews("Hello, World!")
	news_publisher.notifySubscribers()

	print("Detached:", type(news_publisher.detach()).__name__)
	print("Subscribers:", news_publisher.subscribers())

	news_publisher.addNews("My Second news!")
	news_publisher.notifySubscribers()