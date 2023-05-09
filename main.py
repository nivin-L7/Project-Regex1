
from PatternExtractor import extract_emails
from PatternExtractor import extract_phone
from PatternExtractor import read_text_file
from PatternExtractor import validate_data




def main():
	#Read text from file

	text=read_text_file('file.txt')

	#Extract Emails and Phones from the text

	emails=extract_emails(text)
	phone_numbers=extract_phone(text)

	print(emails)



	#Validate extracted data
	valid_emails=validate_data (emails)
	valid_phone_numbers=validate_data(phone_numbers)

	#print the extracted and validated data

	print("Valid Email Addresses:", valid_emails)
	

	
	print("\nValid phone numbers:",valid_phone_numbers)
	
	contacts={'valid emails':', '.join(valid_emails),
		  'valid phones':', '.join(valid_phone_numbers)
			  }
	
	print(contacts)

	#store data to csv file
	with open('contacts.csv', 'a') as f:
		#create csv writer
		writer=csv.DictWriter(f,fieldnames=contacts.keys())

		#append row to the csv

		writer.writerow(contacts)
	

if __name__=='__main__':
	main()
