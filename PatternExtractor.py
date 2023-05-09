import requests
import re #Regular Expression
import csv #To store the output in the csv file

def extract_emails(text):
	#Extract all email addresses from the given text
	pattern=r'[\w.+-]+@[\w-]+\.[\w.-]+'
	return re.findall(pattern,str(text)) #To find all the text which matches the pattern



def extract_phone(text):
	#Extract all phone numbers from the given text
	pattern=r'\d{3}-\d{3}-\d{4}'
	return re.findall(pattern,str(text)) #To find all the text which matches the pattern


def read_text_file(file_path):
	#Reads the text from the given file path

	try:

		with open(file_path, 'r') as f:
			text=f.read()
		return text

	except IOError:
		print(f"Error: Could not read this file.")
		return ""

# Define function to validate extracted data

def validate_data(data):
	#validates extracted data

	valid_data=[]
	for d in data:
		if d not in valid_data:
			valid_data.append(d)
	return valid_data


