class property:
	def __init__(self, key, default):
		self.key = key
		self.default = default
		self._aura = True

	def __get__(self, instance, owner):
		d = database.GET(instance.__class__.__name__.lower(), instance.id)
		if d is None:
			d = self.default
		return d

	def __set__(self, instance, value):
		database.SET(instance.__class__.__name__.lower(), instance.id, value)
		
# demo shit database lmao
class database:
	_storage = {}
	
	def GET(table, key):
		return database._storage.get(table,  {}).get(str(key))
	
	def SET(table, key, value):
		if table in database._storage:
			database._storage[table][str(key)] = value
		else:
			database._storage[table] = {}
			database._storage[table][str(key)] = value
	
	def DELETE(table, key):
		if table in database._storage:
			del database._storage[table][str(key)]

	def LIST(table):
		return database._storage.get(table, {}).keys()