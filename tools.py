#import parameters
from models import Person
import simplejson as json
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

people = []

def validate_field(field):
    # if field is present pass if field:
    if field:
        pass
    # if field is not present print text else:
    else:
        field = 'No results'
    return field
	
def linkedin(screen_name):
	for person in people:
		if person.screen_name == screen_name:
			return person.__dict__
	
	chromedriver = 'C:/Users/DELL/chromedriver_win32/chromedriver.exe'
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	
	
	driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

	# driver.get method() will navigate to a page given by the URL address
	driver.get('https://www.linkedin.com')

	# locate email form by_class_name
	username = driver.find_element_by_class_name('login-email')

	# send_keys() to simulate key strokes
	username.send_keys('meriam.sfaihi@etudiant-isi.utm.tn')

	# sleep for 0.5 seconds
	sleep(0.5)

	# locate password form by_class_name
	password = driver.find_element_by_class_name('login-password')

	# send_keys() to simulate key strokes
	password.send_keys('meriam12345')
	sleep(0.5)

	# locate submit button by_xpath
	sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

	# .click() to mimic button click
	sign_in_button.click()
	sleep(0.5)

	# driver.get method() will navigate to a page given by the URL address
	driver.get('https:www.google.com')
	sleep(3)

	# locate search form by_name
	search_query = driver.find_element_by_name('q')

	# send_keys() to simulate the search text key strokes
	nn='site:linkedin.com/in/ AND '+screen_name
	search_query.send_keys(nn)#a changer avec parametre de la fonction
	sleep(0.5)

	# navigate to the URL address specified by search_query in parameters.py
	driver.get(nn)#a changer avec parametre de la fonction

	# .send_keys() to simulate the return key
	search_query.send_keys(Keys.RETURN)
	sleep(3)

	# locate URL by_class_name
	linkedin_urls = driver.find_elements_by_class_name('iUh30')

	# variable linkedin_url is equal to the list comprehension
	linkedin_urls = [url.text for url in linkedin_urls]
	sleep(0.5)

	# For loop to iterate over each URL in the list returned from the google search query

	linkedin_url=linkedin_urls[0]
		# get the profile URL
	driver.get(linkedin_url)
	sleep(5)

		# assigning the source code for the web page to variable sel
	sel = Selector(text=driver.page_source)

		# xpath to extract the text from the class containing the name
	name = sel.xpath('//*[starts-with(@class, "pv-top-card-section__name")]/text()').extract_first()

		# if name exists
	if name:
			# .strip() will remove the new line /n and white spaces
		name = name.strip()

		# xpath to extract the text from the class containing the job title
	job_title = sel.xpath('//*[starts-with(@class, "pv-top-card-section__headline")]/text()').extract_first()

	if job_title:
		job_title = job_title.strip()
		
	postes = sel.xpath('//*[starts-with(@class, "t-16 t-black t-bold")]/text()').getall()
	for poste in postes:
		if poste:
			poste = poste.strip()
		
	societes = sel.xpath('//*[starts-with(@class, "pv-entity__secondary-title")]/text()').getall()
	for societe in societes:
		if societe:
			societe = societe.strip()
		
	
	descriptions = sel.xpath('//*[starts-with(@class, "lt-line-clamp__line")]/text()').getall()
	for description in descriptions:
		if description:
			description = description.strip()
			
	universites = sel.xpath('//*[starts-with(@class, "pv-entity__school-name t-16 t-black t-bold")]/text()').getall()
	for universite in universites:
		if universite:
			universite = universite.strip()
		

    
	linkedin_url = driver.current_url

    
	name = validate_field(name)
	job_title = validate_field(job_title)
	postes = validate_field(postes)
	societes = validate_field(societes)
	descriptions = validate_field(descriptions)
	universites = validate_field(universites)
	linkedin_url = validate_field(linkedin_url)

	driver.quit()
	person = Person(name,job_title,postes,societes,descriptions,universites,linkedin_url)
	people.append(person)
	return person.__dict__