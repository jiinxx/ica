import requests

class ICAConnection(object):
	url_0="https://api.ica.se/api/login/"
	url ="https://api.ica.se/api/user/minasidor/"

	session = 0

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def createSession(self):
		self.session = requests.Session()
		self.session.auth = (self.username, self.password)
		r = self.session.get(self.url_0)
		self.session.headers.update({'AuthenticationTicket': r.headers['AuthenticationTicket']})

	def getMinasidor(self):
		if self.session == 0:
			self.createSession()
		response = self.session.get(self.url)
		return(response.content)


