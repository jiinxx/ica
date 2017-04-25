import json
from icaconnection import ICAConnection
from icaconfig import ICAConfig

class ICAInfo:
	minasidorParsed = None
	def __init__(self):
		self.config = ICAConfig()
		self.conn = ICAConnection(self.config.get('Credentials','user'), self.config.get('Credentials','password'))

	def getSaldo(self):
		if self.minasidorParsed is None:
			minasidor = self.conn.getMinasidor()
			self.minasidorParsed = json.loads(minasidor)
		return self.minasidorParsed['Saldo']
