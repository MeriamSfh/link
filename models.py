class Person():
	def __init__(self,name,job_title,postes,societes,descriptions,universites,linkedin_url):
		self.name = name
		self.job_title = job_title
		self.postes = postes
		self.societes = societes
		self.descriptions = descriptions
		self.universites = universites
		self.linkedin_url = linkedin_url

	def __str__(self):
		data = {}
		data["name"] = self.name
		data["job title"] = self.job_title
		data["postes"] = self.postes
		data["societes"] = self.societes
		data["description des postes"] = self.descriptions
		data["universites"] = self.universites
		data["linkedin_url"] = self.linkedin_url
		return str(data)