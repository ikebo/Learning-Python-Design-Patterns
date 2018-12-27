# 单例模式

#  __new__

# class Singleton(object):
# 	def __new__(cls):
# 		if not hasattr(cls, 'instance'):
# 			cls.instance = super(Singleton, cls).__new__(cls)
# 		return cls.instance

# s = Singleton()
# print("Object created", s)
# s1 = Singleton()
# print("Object created", s1)

# 单例模式中的懒汉式实例化

# class Singleton:
# 	__instance = None
# 	def __init__(self):
# 		if not Singleton.__instance:
# 			print("__init__ method called..")
# 		else:
# 			print("Instance already created:", self.getInstance())

# 	@classmethod
# 	def getInstance(cls):
# 		if not cls.__instance:
# 			cls.__instance = Singleton()
# 		return cls.__instance

# s = Singleton()
# print(id(s))
# s1 = Singleton()
# print(id(s1))
# s2 = Singleton()
# print(id(s2))

# print("Object created", Singleton.getInstance(), id(Singleton.getInstance()))
# print("Object created", Singleton.getInstance(), id(Singleton.getInstance()))

# Monostate 单例模式

# __dict__

# class Borg:
# 	__shared_state = {"1":"2"}
# 	def __init__(self):
# 		self.x = 1
# 		print(self.__dict__)
# 		self.__dict__ = self.__shared_state

# b = Borg()
# b1 = Borg()
# b.x = 4
# print("Borg Object 'b': ", b)
# print("Borg Object 'b1': ", b1)
# print("Object State 'b':", b.__dict__)
# print("Object State 'b1':", b1.__dict__)

# # 另:
# class Borg(object):
# 	_shared_state = {}
# 	def __new__(cls, *args, **kwargs):
# 		obj = super(Borg, cls).__new__(cls, *args, **kwargs)
# 		obj.__dict__ = cls._shared_state
# 		return obj


# 单例和元类
# __call__
# class MyInt(type):
# 	def __call__(cls, *args, **kwargs):
# 		print("***** Here's My int *****", args)
# 		print("Now do whatever you want with these objects...")
# 		return type.__call__(cls, *args, **kwargs)

# class int(metaclass=MyInt):
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y

# i = int(4,5)

# 元类的单例实现
class MetaSingleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
		print(cls._instances)
		return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
	pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)


			