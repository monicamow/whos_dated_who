# -*- coding: utf-8 -*-
"""
Project:Scrape dating data

"""

import pandas as pd
import numpy as np
import os
import requests


#PATH = ""
#os.chdir(PATH)

####################################
# Define Variables
####################################


####################################
# Load Data
####################################
def get_relationships(name):
	"""
	Input celebrity name, function will return a list of all their partners
	courtesy of whosdatedwho.com.
	It's important to make sure the spelling of the celebrities name matches what is on 
	the website.
	Returns a dataframe containing partner details
	"""
	name_cleaned = name.replace(' ', '-')	
	name_cleaned = name_cleaned.replace('.', '')
	URL = 'https://www.whosdatedwho.com/dating/%s' %name_cleaned
	response = requests.get(URL)
	html = response.text
	tbls = pd.read_html(html)
	
	col_names = ['#', 'Partner', 'Type', 'End']
	counter = 0			 
	for df in tbls:
		if df.columns.isin(col_names).sum() == len(col_names):					
			relationship_deets = df
			counter+=1
			if counter >1:
				print("FOUND TOO MANY MATCHING TABLES, DOUBLE CHECK")

	try:
		relationship_deets.rename(columns ={'Unnamed: 3': 'Rumored'}, inplace =True)
		relationship_deets.drop(columns ={'Unnamed: 7'}, inplace=True)
	except KeyError:
		pass
	
	return relationship_deets

####################################
# Clean Data
####################################




####################################
# Analyze Data
####################################




####################################
# Create Charts
####################################




####################################
# Save Data
####################################




