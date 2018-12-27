# 复合模式, MVC

# class Model:
# 	services = {
# 		'email': {'number': 1000, 'price': 2},
# 		'sms': {'number': 1000, 'price': 10},
# 		'voice': {'number': 1000, 'price': 15},
# 	}

# class View:
# 	def list_services(self, services):
# 		for svc in services:
# 			print(svc, ' ')

# 	def list_pricing(self, services):
# 		for svc in services:
# 			print("For", Model.services[svc]['number'],
# 								svc, "message you pay $",
# 							Model.services[svc]['price'])

# class Controller:
# 	def __init__(self):
# 		self.model = Model()
# 		self.view = View()

# 	def get_services(self):
# 		services = self.model.services.keys()
# 		return (self.view.list_pricing(services))

# 	def get_pricing(self):
# 		services = self.model.services.keys()
# 		return (self.view.list_pricing(services))

# class Client:
# 	controller = Controller()
# 	print("Services Provided: ")
# 	controller.get_services()
# 	print("Pricing for Services: ")
# 	controller.get_pricing()

# Client()

# class Model:
# 	def logic(self):
# 		data = 'Got it!'
# 		print("Model: Crunching data as per business logic")
# 		return data

# class View:
# 	def update(self, data):
# 		print("View: Updating the view with results: ", data)

# class Controller:
# 	def __init__(self):
# 		self.model = Model()
# 		self.view = View()

# 	def interface(self):
# 		print("Controller: Relayed the Client asks")
# 		data = self.model.logic()
# 		self.view.update(data)

# class Client:
# 	print("Client: asks for certain information")
# 	controller = Controller()
# 	controller.interface()

# Client()

import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		query = "select * from task"
		todos = _execute(query)
		self.render('index.html', todos=todos)

class NewHandler(tornado.web.RequestHandler):
	def post(self):
		name = self.get_argument('name', None)
		query = "create table if not exists task (id INTEGER \
					PRIMARY KEY, name TEXT, status NUMERIC)"
		_execute(query)
		query = "insert into task (name, status) \
			values ('%s', %d) " % (name, 1)
		_execute(query)
		self.redirect('/')

	def get(self):
		self.render('new.html')

class UpdateHandler(tornado.web.RequestHandler):
	def get(self, id, status):
		query = "update task set status=%d where id=%s" % (int(status), id)
		_execute(query)
		self.redirect('/')

class DeleteHandler(tornado.web.RequestHandler):
	def get(self, id):
		query = "delete from task where id=%s" % id
		_execute(query)

class RunApp(tornado.web.Application):
	def __init__(self):
		Handlers = [
			(r'/', IndexHandler),
			(r'/todo/new', NewHandler),
			(r'/todo/update/(\d+)/status/(\d+)', UpdateHandler),
			(r'/todo/delete/(\d+)', DeleteHandler),
		]
		settings = dict(
			debug=True,
			template_path='templates',
			static_path="static",
			)
		tornado.web.Application.__init__(self,Handlers,**settings)

if __name__ == '__main__':
	http_server = tornado.httpserver.HTTPServer(RunApp())
	http_server.listen(5000)
	tornado.ioloop.IOLoop.instance().start()

