import aura

uuid = aura.db.property('uuid', default='')
username = aura.db.property('username', default='')
exp = aura.db.property('exp', default=0)
dono = aura.db.property('donations', default=0)

def yo(self):
	print("yo", self.name)