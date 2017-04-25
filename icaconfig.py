import ConfigParser

class ICAConfig:
	def __init__(self):
		self.config = ConfigParser.RawConfigParser()
		self.config.read('icaconfig.properties')

	def get(self, section, value):
		return self.config.get(section, value)
