_storage = {}

class database:
	def _get(table, key):
		return _storage.get(table,  {}).get(key, {})
	
	def _set(table, key, value):
		if table in _storage:
			_storage[table][key] = value
		else:
			_storage[table] = {}
			_storage[table][key] = {}
	
	def _del(table, key):
		if table in _storage:
			del _storage[table][key]

	def _list(table):
		return _storage.get(table, {}).keys()